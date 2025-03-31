import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from pytubefix import YouTube


def progress_function(stream, chunk, bytes_remaining):
    global file_size
    downloaded = file_size - bytes_remaining
    percent = (downloaded / file_size) * 100

    # Atualizar a interface gráfica
    progress_label.config(
        text=f"Baixando: {int(percent)}% ({downloaded / (1024 ** 2):.2f} MB / {file_size / (1024 ** 2):.2f} MB)"
    )
    progress_bar['value'] = percent
    tk_root.update_idletasks()


def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida do YouTube.")
        return

    folder = folder_entry.get().strip() or os.path.join(os.path.expanduser("~"), "Videos")

    try:
        yt = YouTube(url, on_progress_callback=progress_function)

        if audio_var.get():
            stream = yt.streams.filter(only_audio=True).first()
            file_path = stream.download(output_path=folder)

            # Renomear para MP3.
            base, ext = os.path.splitext(file_path)
            new_file = base + ".mp3"
            os.rename(file_path, new_file)
        else:
            resolution = resolution_var.get()
            if resolution:
                stream = yt.streams.filter(res=resolution).first()
            else:
                stream = yt.streams.get_highest_resolution()

        global file_size
        file_size = stream.filesize

        # Resetando a barra de progresso antes de iniciar o download
        progress_bar['value'] = 0
        progress_label.config(text="Iniciando download...")

        stream.download(output_path=folder)

        # Atualizando para 100% após o download ser concluído
        progress_label.config(text="Download Completo!")
        progress_bar['value'] = 100

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo:\n{e}")


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)


def exit_app():
    tk_root.quit()
    tk_root.destroy()


tk_root = tk.Tk()
tk_root.title("YouTube Downloader")
tk_root.geometry("800x600")
tk_root.resizable(False, False)

# Campos e botões
tk.Label(tk_root, text="URL do vídeo:").pack(pady=5)
url_entry = tk.Entry(tk_root, width=50)
url_entry.pack(pady=5)

tk.Label(tk_root, text="Pasta de destino (opcional):").pack(pady=5)
folder_entry = tk.Entry(tk_root, width=50)
folder_entry.pack(pady=5)

browse_button = tk.Button(tk_root, text="Selecionar Pasta", command=select_folder)
browse_button.pack(pady=5)

# Opções de resolução
resolution_var = tk.StringVar()
tk.Label(tk_root, text="Escolha a resolução (opcional):").pack(pady=5)
resolutions = ["144p", "360p", "480p", "720p", "1080p"]
resolution_menu = tk.OptionMenu(tk_root, resolution_var, *resolutions)
resolution_menu.pack(pady=5)

# Opção de áudio (MP3)
audio_var = tk.BooleanVar()
audio_checkbox = tk.Checkbutton(tk_root, text="Baixar como MP3", variable=audio_var)
audio_checkbox.pack(pady=5)

# Botõe
download_button = tk.Button(tk_root, text="Baixar Vídeo", command=download_video)
download_button.pack(pady=10)

exit_button = tk.Button(tk_root, text="Sair", command=exit_app)
exit_button.pack(pady=5)

# Label para exibir o progresso
progress_label = tk.Label(tk_root, text="Progresso: 0%")
progress_label.pack(pady=10)

# Barra de progresso
progress_bar = ttk.Progressbar(tk_root, length=400, mode='determinate')
progress_bar.pack(pady=10)

# Inicia a interface gráfica
tk_root.mainloop()
