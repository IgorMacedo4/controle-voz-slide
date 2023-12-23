#import das bibliotecas necessarias
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
from PIL import Image, ImageTk
import os
from VoiceController import VoiceController

class SlideShowApp:
     # Inicializa a aplicação de apresentação de slides com interface Tkinter e suporte a controle de voz.
    def __init__(self, root):
        self.root = root
        self.root.title('Apresentação de Slides com Controle de Voz')
        self.create_initial_buttons_and_instructions()
        self.slides = []
        self.current_slide = 0
        self.zoom_level = 1.0
        self.default_zoom_level = 1.0
        self.display = tk.Label(root)

    def create_initial_buttons_and_instructions(self):
        # Código para criar botões e instruções iniciais
        self.btn_open_file = tk.Button(self.root, text='Abrir Arquivo', command=self.open_pdf_file)
        self.btn_open_file.pack(pady=10)
        instruction_text = (
            "Instruções de Comandos de Voz:\n\n"
            "Próximo Slide: 'próximo slide', 'avance', 'próxima'\n"
            "Slide Anterior: 'slide anterior', 'volte', 'anterior'\n"
            "Aumentar Zoom: 'aumentar zoom', 'mais zoom', 'ampliar'\n"
            "Diminuir Zoom: 'diminuir zoom', 'menos zoom', 'reduzir'\n"
            "Apresentar: 'tela cheia' 'modo apresentação', 'apresentação normal', 'resetar zoom'\n"
            "Maximizar Tela: 'maximizar tela', 'aumentar janela'\n"
            "Fechar Janela: 'fechar janela', 'sair', 'encerrar'\n"
            "Minimizar Tela: 'minimizar tela', 'reduzir janela'"
        )
        self.instructions = tk.Label(self.root, text=instruction_text, justify=tk.LEFT, font=("Arial", 10), padx=10)
        self.instructions.pack(pady=10)

    def open_pdf_file(self):
        # Código para abrir e processar o arquivo PDF
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        self.pdf_file = filedialog.askopenfilename(initialdir=downloads_path, title="Selecionar Arquivo PDF", filetypes=[("PDF Files", "*.pdf")])
        if self.pdf_file:
            self.slides = convert_from_path(self.pdf_file)
            self.display.pack(expand=True, fill='both')
            self.voice_controller = VoiceController(self)
            self.root.after(100, self.update_slide)
            self.btn_open_file.pack_forget()
            self.instructions.pack_forget()

    def update_slide(self, zoom_adjust=False):
        # Código para atualizar o slide atualmente visível
        if self.root.winfo_width() <= 1 or self.root.winfo_height() <= 1:
            return

        max_width = self.root.winfo_width()
        max_height = self.root.winfo_height()

        image = self.slides[self.current_slide].convert('RGB')
        original_width, original_height = image.size

        if zoom_adjust:
            new_width = int(original_width * self.zoom_level)
            new_height = int(original_height * self.zoom_level)
        else:
            scale = min(max_width/original_width, max_height/original_height)
            new_width = int(original_width * scale)
            new_height = int(original_height * scale)

        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        tk_image = ImageTk.PhotoImage(resized_image)

        self.display.config(image=tk_image)
        self.display.image = tk_image

    def next_slide(self):
        # Código para avançar para o próximo slide
        if self.current_slide < len(self.slides) - 1:
            self.current_slide += 1
            self.update_slide()

    def prev_slide(self):
        # Código para voltar para o slide anterior
        if self.current_slide > 0:
            self.current_slide -= 1
            self.update_slide()

    def zoom_in(self):
        # Código para aumentar o zoom
        self.zoom_level *= 1.02
        self.update_slide(zoom_adjust=True)

    def zoom_out(self):
        # Código para diminuir o zoom
        self.zoom_level /= 1.02
        self.update_slide(zoom_adjust=True)

    def reset_zoom(self):
        # Código para resetar o zoom
        self.zoom_level = self.default_zoom_level
        self.update_slide()

    def toggle_fullscreen(self):
        # Alterna entre tela cheia e tamanho normal
        self.root.attributes("-fullscreen", not self.root.attributes("-fullscreen"))
        # Atualiza o slide imediatamente para refletir a mudança
        self.update_slide()

    def close_window(self):
         # Código para fechar a janela
        self.root.destroy()

    def minimize_window(self): 
        # Código para minimizar a janela 
        self.root.attributes("-iconic", True)