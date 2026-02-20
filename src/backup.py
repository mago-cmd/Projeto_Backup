import os
from tkinter import Tk, ttk, messagebox
from tkinter.filedialog import askdirectory, asksaveasfilename
import shutil
import datetime
import sys
import time
import threading


def calcular_tamanho(caminho):
    """Calcula o tamanho total de uma pasta em bytes"""
    tamanho_total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(caminho):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                try:
                    tamanho_total += os.path.getsize(filepath)
                except (OSError, IOError):
                    pass
    except Exception as e:
        print(f"Erro ao calcular tamanho: {e}")
    return tamanho_total


def formatar_tamanho(bytes_size):
    """Converte bytes para formato legível (KB, MB, GB)"""
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unidade}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} TB"


def formatar_tempo(segundos):
    """Formata segundos para MM:SS"""
    try:
        segundos = int(max(0, segundos))
        m = segundos // 60
        s = segundos % 60
        return f"{m:02d}:{s:02d}"
    except Exception:
        return "--:--"


def sanitize_filename(name: str) -> str:
    """Remove caracteres inválidos para nomes de arquivos no Windows."""
    invalid = '<>:"/\\|?*'
    for ch in invalid:
        name = name.replace(ch, '_')
    return name


def mostrar_estatisticas(tamanho_info):
    """Mostra uma janela com estatísticas do backup"""
    if not tamanho_info:
        return
    
    tamanho_original, tamanho_comprimido, tempo_decorrido = tamanho_info
    taxa_compressao = (1 - tamanho_comprimido / max(tamanho_original, 1)) * 100

    stats_window = Tk()
    stats_window.title("Estatísticas do Backup")
    stats_window.geometry("400x300")
    stats_window.resizable(False, False)
    
    # Define ícone
    icon_path = os.path.join(os.path.dirname(__file__), "backup_icone.ico")
    if os.path.isfile(icon_path):
        try:
            stats_window.iconbitmap(icon_path)
        except Exception:
            pass
    
    # Conteúdo
    info_text = f"""
✓ BACKUP CONCLUÍDO COM SUCESSO!

Tamanho Original:        {formatar_tamanho(tamanho_original)}
Tamanho Comprimido:  {formatar_tamanho(tamanho_comprimido)}
Taxa de Compressão:  {taxa_compressao:.1f}%

Tempo Gasto:              {tempo_decorrido:.1f} segundos

    """
    
    label = ttk.Label(stats_window, text=info_text, font=("Consolas", 10), justify='left')
    label.pack(padx=15, pady=15, expand=True)
    
    botao_ok = ttk.Button(stats_window, text="OK", command=stats_window.destroy)
    botao_ok.pack(pady=10)
    
    stats_window.mainloop()


def main():
    root = Tk()
    root.withdraw()
    
    # Adiciona ícone à janela
    icon_path = os.path.join(os.path.dirname(__file__), "backup_icone.ico")
    if os.path.isfile(icon_path):
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Aviso: não foi possível carregar ícone: {e}")
    # Seleciona a pasta de origem
    pasta_origem = askdirectory(
        title="Selecione a pasta que deseja fazer backup"
    )

    if not pasta_origem:
        print("Nenhuma pasta selecionada. Saindo.")
        root.destroy()
        return

    # Nome sugerido com data/hora incluindo o nome da pasta origem
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pasta_base = os.path.basename(os.path.normpath(pasta_origem)) or 'folder'
    pasta_segura = sanitize_filename(pasta_base)
    nome_padrao = f"{pasta_segura}_Backup_{timestamp}.zip"

    # Define Área de Trabalho como local padrão
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    if not os.path.isdir(desktop_dir):
        desktop_dir = os.path.expanduser("~")

    # Seleciona onde salvar o ZIP
    zip_destino = asksaveasfilename(
        title="Escolha onde salvar o backup",
        defaultextension=".zip",
        initialdir=desktop_dir,
        initialfile=nome_padrao,
        filetypes=[("Arquivo ZIP", "*.zip")]
    )

    root.destroy()

    if not zip_destino:
        print("Local de salvamento não escolhido. Saindo.")
        return

    # Cria janela de progresso
    janela_prog = Tk()
    janela_prog.title("Realizando Backup...")
    janela_prog.geometry("420x140")
    janela_prog.resizable(False, False)

    if os.path.isfile(icon_path):
        try:
            janela_prog.iconbitmap(icon_path)
        except Exception:
            pass

    # Container central para centralizar conteúdo verticalmente
    content = ttk.Frame(janela_prog)
    content.pack(expand=True, fill='both', padx=12, pady=8)

    # Label de status (centralizado)
    label = ttk.Label(content, text="Realizando backup... 0%", font=("Arial", 10))
    label.pack(pady=(0, 8))

    # Barra de progresso simples (centralizada no content)
    barra = ttk.Progressbar(content, mode='determinate', length=360, maximum=100)
    barra.pack(pady=(0, 6))
    barra['value'] = 0

    # ETA label
    eta_label = ttk.Label(content, text="Estimativa: --:--", font=("Arial", 9))
    eta_label.pack()

    # Variáveis compartilhadas
    resultado_backup = {'path': None, 'stats': None, 'erro': None, 'progresso': 0, 'tempo_inicio': None}

    def executar_backup():
        """Função que roda em thread separada"""
        try:
            resultado_backup['progresso'] = 10

            # Calcula tamanho original
            tamanho_original = calcular_tamanho(pasta_origem)

            if not zip_destino.lower().endswith(".zip"):
                zip_final = zip_destino + ".zip"
            else:
                zip_final = zip_destino

            dest_dir = os.path.dirname(zip_final)
            if dest_dir and not os.path.isdir(dest_dir):
                os.makedirs(dest_dir, exist_ok=True)

            base_name = zip_final.replace(".zip", "")
            resultado_backup['tempo_inicio'] = time.time()
            tempo_inicio = resultado_backup['tempo_inicio']

            resultado_backup['progresso'] = 40

            # Cria o ZIP
            shutil.make_archive(base_name, 'zip', pasta_origem)

            resultado_backup['progresso'] = 80

            # Verifica arquivo
            if os.path.isfile(zip_final):
                tamanho_comprimido = os.path.getsize(zip_final)
                tempo_decorrido = time.time() - tempo_inicio

                resultado_backup['path'] = zip_final
                resultado_backup['stats'] = (tamanho_original, tamanho_comprimido, tempo_decorrido)
                resultado_backup['progresso'] = 100
            else:
                resultado_backup['erro'] = "Arquivo ZIP não foi criado"

        except Exception as e:
            resultado_backup['erro'] = str(e)

    def atualizar_progresso():
        """Atualiza a barra de progresso simples na thread principal e mostra ETA"""
        progresso = resultado_backup.get('progresso', 0)
        barra['value'] = progresso
        label.config(text=f"Realizando backup... {progresso}%")

        # ETA calculation
        tempo_inicio = resultado_backup.get('tempo_inicio')
        if tempo_inicio and progresso > 0 and progresso < 100:
            elapsed = time.time() - tempo_inicio
            try:
                estimated_total = elapsed * 100.0 / progresso
                remaining = max(0.0, estimated_total - elapsed)
                eta_label.config(text=f"Estimativa: {formatar_tempo(remaining)}")
            except Exception:
                eta_label.config(text="Estimativa: --:--")
        elif progresso >= 100:
            eta_label.config(text="Estimativa: 00:00")
        else:
            eta_label.config(text="Estimativa: --:--")

        # Se ainda está em andamento, agenda próxima atualização
        if progresso < 100 and not resultado_backup.get('erro'):
            janela_prog.after(100, atualizar_progresso)
        else:
            # Fecha a janela após breve atraso
            janela_prog.after(400, janela_prog.destroy)

    # Executa backup em thread separada
    thread_backup = threading.Thread(target=executar_backup, daemon=True)
    thread_backup.start()

    # Agenda atualizações de progresso na thread principal
    janela_prog.after(100, atualizar_progresso)
    janela_prog.mainloop()
    
    if resultado_backup['erro']:
        messagebox.showerror("Erro", f"Falha ao criar backup:\n{resultado_backup['erro']}")
    elif resultado_backup['path']:
        print(f"Arquivo gerado: {resultado_backup['path']}")
        mostrar_estatisticas(resultado_backup['stats'])
    else:
        messagebox.showerror("Erro", "Falha desconhecida ao criar backup!")


if __name__ == '__main__':
    main()
