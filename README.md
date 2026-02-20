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
ROTINA_BACKUP/
│
├── src/
│   ├── backup.py          # Script principal
│   ├── criar_icone.py     # Script auxiliar para ícones
│   └── gerar_exe.py       # Script para empacotar em .exe
│
├── assets/                # Ícones e recursos visuais
├── build/                 # Artefatos de build (PyInstaller)
├── dist/                  # Executáveis gerados
├── release/               # Pacotes finais
├── spec/                  # Arquivos .spec do PyInstaller
├── .venv/                 # Ambiente virtual (não versionar)
├── .gitignore             # Ignora arquivos desnecessários
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação

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



