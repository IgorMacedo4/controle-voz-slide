#import das bibliotecas necessarias
from threading import Thread
import speech_recognition as sr
from unidecode import unidecode



class VoiceController:
    # Inicializa o controle de voz em uma thread separada para a aplicação de slides.
    def __init__(self, app):
        self.app = app
        self.voice_thread = Thread(target=self.initiate_voice_control)
        self.voice_thread.daemon = True
        self.voice_thread.start()

    def initiate_voice_control(self):
        # Código para iniciar o controle de voz
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            while True:
                try:
                    print("Ouvindo...")
                    voice = recognizer.listen(source)
                    command = recognizer.recognize_google(voice, language='pt-BR').lower()
                    command = unidecode(command)
                    self.process_command(command)
                except sr.UnknownValueError:
                    print("Não entendi, por favor repita.")
                except Exception as e:
                    print(f"Ocorreu um erro: {e}")

    def process_command(self, command):
            # Código para processar os comandos de voz recebidos
            if any(term in command for term in ['proximo slide', 'avance', 'próxima']):
                self.app.next_slide()
            elif any(term in command for term in ['slide anterior', 'volte', 'anterior']):
                self.app.prev_slide()
            elif any(term in command for term in ['aumentar zoom', 'mais zoom', 'ampliar']):
                self.app.zoom_in()
            elif any(term in command for term in ['diminuir zoom', 'menos zoom', 'reduzir']):
                self.app.zoom_out()
            elif 'tela cheia' in command:
                # Quando o comando "tela cheia" for detectado, maximiza a tela e reseta o zoom
                self.app.toggle_fullscreen()
                self.app.reset_zoom()
            elif any(term in command for term in ['fechar janela', 'sair', 'encerrar']):
                self.app.close_window()
            elif any(term in command for term in ['minimizar tela', 'reduzir janela']):
                self.app.minimize_window()
