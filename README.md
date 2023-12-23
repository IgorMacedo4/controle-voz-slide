# Apresentação de Slides com Controle de Voz

## Descrição
Este projeto é uma aplicação de apresentação de slides controlada por voz, desenvolvida em Python 
com a biblioteca Tkinter e a biblioteca Speech Recognition.
Permite ao usuário abrir um arquivo PDF e navegar pelos slides usando comandos de voz.

## Funcionalidades:
- Abrir arquivos PDF como slides.
- Navegar entre os slides com comandos de voz.
- Ajustar o zoom dos slides.
- Alternar entre o modo tela cheia e o tamanho normal da janela.
- Fechar a aplicação com um comando de voz.

## Requisitos para executar esta aplicação, você precisará de Python instalado em sua máquina
E as seguintes bibliotecas:
- Tkinter (geralmente vem instalado com Python)
- pdf2image
- Pillow
- speech_recognition
- unidecode

## Instalação:
Clone o repositório e instale as dependências
- git clone https://github.com/IgorMacedo4/controle-voz-slide.git
- cd controle-voz-slide
- pip install -r requirements.txt

## Execução:
Para executar a aplicação, navegue até a pasta do projeto e execute:
- python main.py

## Comandos de Voz:
- "Próximo slide": Avança para o próximo slide.
- "Slide anterior": Retorna ao slide anterior.
- "Aumentar zoom": Amplia o slide atual.
- "Diminuir zoom": Reduz o slide atual.
- "Tela cheia": Alterna para o modo tela cheia e reseta o zoom.
- "Fechar janela": Encerra a aplicação.
- "Minimizar tela": Minimiza a janela da aplicação.
