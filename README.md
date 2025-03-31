# YoutubeDownPy

Este é um aplicativo de desktop simples para baixar vídeos do YouTube usando Python e a biblioteca `pytubefix`. O programa permite ao usuário escolher entre baixar vídeos com áudio ou apenas o áudio em formato MP3, além de selecionar a resolução desejada.




![Captura de tela 2025-03-30 224012](https://github.com/user-attachments/assets/93c1abaf-0b44-4022-9190-6e453a9cb5fd)

## Funcionalidades

- Baixar vídeos do YouTube em várias resoluções.
- Baixar apenas o áudio em formato MP3.
- Escolher a pasta de destino para o arquivo baixado.
- Barra de progresso para acompanhar o status do download.

## Requisitos

- Python 3.x
- `pytubefix`
- `tkinter` (já incluído no Python por padrão)
- `ttk` (já incluído no Python por padrão)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/amendesz/youtube-downloader.git
   cd youtube-downloader

Instale as dependências necessárias:

Se você estiver usando um ambiente virtual (recomendado), crie e ative o ambiente:

## Para Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate

## Para Windows:
```bash
python -m venv venv
venv\Scripts\activate

Depois de ativar o ambiente virtual, instale as dependências com o seguinte comando:
```bash
pip install -r requirements.txt

Agora, você pode rodar o programa:

```bash
python ytpy.py
Isso irá iniciar a interface gráfica e permitir que você baixe vídeos do YouTube.

