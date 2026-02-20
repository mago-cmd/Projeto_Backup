# Programa de Backup com Ícone Personalizado

## 📦 Arquivos Principais

- **backup.py** - Script principal de backup (com ícone integrado)
- **gerar_exe.py** - Script para gerar o executável (.exe)
- **backup_icone.ico** - Ícone personalizado
- **backup_icone.png** - Versão PNG do ícone
- **criar_icone.py** - Script para customizar o ícone
- **dist/Backup.exe** - ✅ Executável pronto para distribuição

---

## 🚀 Como Usar

````markdown
# Programa de Backup com Ícone Personalizado

## 📦 Arquivos Principais (atualizados)

- **backup.py** - Script principal de backup (GUI, ícone integrado)
- **gerar_exe.py** - Script para gerar o executável (.exe) via PyInstaller
- **criar_icone.py** - Script para gerar/editar o ícone (`backup_icone.png` / `.ico`)
- **backup_icone.ico** / **backup_icone.png** - Ícone do aplicativo
- **dist/Backup.exe** - Executável gerado (quando criado)
- **build/**, **spec/** - Pastas de build do PyInstaller
- **backup.spec** - Spec gerado pelo PyInstaller
- **release/** e **Backup_release.zip** - pacote de distribuição que criei (opcional)



---

## 🚀 Como Usar

### Opção 1 — Usar o Executável (Recomendado)
### Programa de Backup com Ícone Personalizado

## 📦 Arquivos Principais (atualizados)

- **backup.py** - Script principal de backup (GUI, ícone integrado)
- **gerar_exe.py** - Script para gerar o executável (.exe) via PyInstaller
- **criar_icone.py** - Script para gerar/editar o ícone (`backup_icone.png` / `.ico`)
- **backup_icone.ico** / **backup_icone.png** - Ícone do aplicativo
- **dist/Backup.exe** - Executável gerado (quando criado)
- **build/**, **spec/** - Pastas de build do PyInstaller
- **backup.spec** - Spec gerado pelo PyInstaller
- **release/** e **Backup_release.zip** - pacote de distribuição que criei (opcional)

---

## 🚀 Como Usar

### Opção 1 — Usar o Executável (Recomendado)
Abra o arquivo em `dist/Backup.exe` (duplo clique).

### Opção 2 — Executar com Python
```powershell
python backup.py
```

### Recriar o Executável
```powershell
python gerar_exe.py
```

Obs: o `gerar_exe.py` usa `PyInstaller` e o `backup_icone.ico` para embutir o ícone.

---

## ✨ Funcionalidades Principais

1. Seleciona a pasta de origem para backup
2. Escolhe local de destino do ZIP (padrão: Área de Trabalho)
3. Nome padrão gerado: `<nome_da_pasta>_Backup_YYYY-MM-DD_hh-mm-ss.zip`
4. Janela com progresso responsivo e estimativa de tempo restante (ETA)
5. Estatísticas ao final (tamanho original, comprimido, tempo)

---

## 📤 Distribuição

Gerei um pacote `Backup_release.zip` contendo o executável e o README:

- `Backup_release.zip` — pronto para enviar/compartilhar

---

## 🎨 Personalizar o Ícone

Edite `criar_icone.py` para alterar cores ou desenho; gere o `.ico` e em seguida rode `gerar_exe.py`:

```powershell
python criar_icone.py
python gerar_exe.py
```

---

## 📁 Estrutura do Projeto (atual)

```
rotina_backup/
├── backup.py
├── gerar_exe.py
├── criar_icone.py
├── backup_icone.ico
├── backup_icone.png
├── dist/                 # contém Backup.exe depois de gerar
├── build/                # gerado pelo PyInstaller
├── spec/                 # gerado pelo PyInstaller
├── backup.spec
├── release/              # cópias para release (opcional)
├── Backup_release.zip    # pacote pronto para envio
└── README.md
```

---

## 🔧 Requisitos

- Para `backup.py`: Python 3.7+ com Tkinter
- Para modificar ícone: Pillow (`pip install Pillow`)
- Para gerar `.exe`: PyInstaller (`pip install pyinstaller`)

---

## ❓ Dicas Rápidas

- Se o `.exe` não abrir: execute via PowerShell para ver erros: `.\dist\Backup.exe`
- Para testes rápidos, use uma pasta pequena e verifique o nome do ZIP gerado

---

## English version (below)

---

## Program README — English

### Main files

- `backup.py` — main GUI backup script (includes icon)
- `gerar_exe.py` — helper script to build a single-file Windows exe using PyInstaller
- `criar_icone.py` — creates/edits `backup_icone.png` and `backup_icone.ico`
- `backup_icone.ico` / `backup_icone.png` — application icons
- `dist/Backup.exe` — produced executable (after building)
- `Backup_release.zip` — optional release zip produced

### Quick usage

1. Run the executable (recommended): `dist\Backup.exe` (double-click)
2. Or run with Python for development: `python backup.py`
3. Rebuild exe after changes: `python gerar_exe.py`

### Main features

- Choose source folder to backup
- Choose destination file (default: Desktop)
- Default ZIP name: `<folder>_Backup_YYYY-MM-DD_hh-mm-ss.zip`
- Progress window with ETA and final statistics

### Build / Icon

1. Optionally customize icon with `criar_icone.py` (requires Pillow)
2. Rebuild exe with `python gerar_exe.py` (requires PyInstaller)

---

If you want I can also:

- remove the release files when releasing a clean source tree.

```
