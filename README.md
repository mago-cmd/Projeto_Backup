#  ROTINA_BACKUP

## Sobre o projeto
O **ROTINA_BACKUP** é uma aplicação em **Python** com interface gráfica (Tkinter) que permite realizar backups de pastas, gerando arquivos compactados em formato `.zip`.  
O sistema mostra progresso em tempo real, estimativa de tempo restante e estatísticas ao final do processo.

---

## Funcionalidades
- Seleção de pasta de origem para backup.
- Geração automática de arquivo `.zip` com nome seguro e timestamp.
- Barra de progresso com estimativa de tempo (ETA).
- Exibição de estatísticas: tamanho original, tamanho comprimido e taxa de compressão.
- Interface gráfica simples e intuitiva com **Tkinter**.
- Ícone personalizado para janelas.

---

## Tecnologias utilizadas
- **Python 3.10+**
- **Tkinter** (GUI nativa do Python)
- **shutil** (para compactação)
- **threading** (execução em paralelo)
- **datetime / time / os** (manipulação de arquivos e tempo)

---

## Estrutura do projeto

```
Projeto_Backup/
├── src/                # Código-fonte principal do projeto (.py)
├── assets/             # Recursos visuais (ícones e imagens do projeto)
├── Backup_release/     # Pasta contendo o executável final e documentação de uso
│   ├── Backup.exe      # Executável do sistema de backup
│   └── README.md       # Instruções específicas para o usuário final
├── .gitignore          # Define arquivos e pastas ignorados pelo Git (build, spec, etc.)
├── README.md           # Documentação principal do projeto (este arquivo)
├── backup.spec         # Arquivo de configuração para geração do executável
└── requirements.txt    # Lista de dependências Python necessárias para o projeto

```


---

## Instalação e execução

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/ROTINA_BACKUP.git
cd ROTINA_BACKUP
```
### 2. Crie e ative o ambiente virtual
- Windows (PowerShell):
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- Linux/macOS:
```
python3 -m venv .venv
source .venv/bin/activate
```
### 3. Instale dependências
```
pip install -r requirements.txt
```
## Gerar executável (opcional)
Se quiser distribuir como .exe, utilize o PyInstaller:
```
pip install pyinstaller
pyinstaller --onefile --windowed src/backup.py --icon=assets/backup_icone.ico
```
### O executável será gerado dentro da pasta dist/.

Licença
Este projeto é de uso pessoal/educacional.
Sinta-se livre para adaptar e compartilhar conforme necessário.





