import subprocess
import sys
import os

# Muda para o diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Instala PyInstaller se não tiver
try:
    import PyInstaller  # pyinstaller
except ImportError:
    print("Instalando PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

# Verifica se o ícone existe
icon_path = os.path.join(script_dir, "backup_icone.ico")
if not os.path.isfile(icon_path):
    print(f"ERRO: Ícone não encontrado em {icon_path}")
    sys.exit(1)

# Cria o executável com ícone
print("Gerando executável...")
try:
    subprocess.run([
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        f"--icon={icon_path}",
        "--name=Backup",
        "--distpath=dist",
        "--workpath=build",
        "--specpath=spec",
        "backup.py"
    ], check=True)
    
    exe_path = os.path.join(script_dir, "dist", "Backup.exe")
    print(f"\nEXECUTAVEL CRIADO COM SUCESSO!")
    print(f"Caminho: {exe_path}")
    print("Você pode executá-lo diretamente sem abrir o terminal!")
except Exception as e:
    print(f"ERRO ao gerar executável: {e}")
    sys.exit(1)
