#import das bibliotecas necessarias
import tkinter as tk
from SlideShowApp import SlideShowApp

def main():
    # Cria a janela principal do aplicativo
    root = tk.Tk()
    root.geometry("800x600")

    # Instancia a aplicação de slideshow
    app = SlideShowApp(root)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == '__main__':
    main()
