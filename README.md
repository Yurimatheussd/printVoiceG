# PrintVoiceG - Leitor de Tela Inteligente

PrintVoiceG é uma ferramenta que utiliza captura de tela, reconhecimento óptico de caracteres (OCR), inteligência artificial e síntese de voz para transformar imagens em áudio. Com um simples atalho de teclado, você pode capturar qualquer área da tela, extrair o texto, aprimorá-lo com o Gemini Pro e ouvi-lo em áudio.

## Funcionalidades

* **Captura de Tela:** Captura qualquer área da tela usando o atalho `Ctrl+Shift+V`.
* **Reconhecimento de Texto (OCR):** Extrai o texto da imagem capturada usando o Tesseract OCR.
* **Aprimoramento de Texto com Gemini Pro:** Utiliza o modelo Gemini Pro do Google para corrigir e aprimorar o texto extraído, garantindo uma leitura mais clara e precisa.
* **Síntese de Voz (TTS):** Converte o texto aprimorado em áudio usando o Google Text-to-Speech (gTTS).
* **Copia o texto tratado para a área de transferência:** Após o tratamento do texto, o mesmo é copiado para a área de transferência.
* **Reprodução Automática de Áudio:** Reproduz o áudio automaticamente e simula o atalho `Ctrl+Shift+K` para fechar o reprodutor de mídia.

## Pré-requisitos

Antes de executar o PrintVoiceG, certifique-se de ter os seguintes pré-requisitos instalados:

* **Python 3.x:** [Download Python](https://www.python.org/downloads/)
* **Tesseract OCR:** [Download Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (Certifique-se de adicionar o diretório de instalação do Tesseract ao PATH do sistema.)
* **Bibliotecas Python:** Instale as bibliotecas necessárias usando o pip:

    ```bash
    pip install pyautogui keyboard pytesseract gTTS Pillow google-generativeai python-dotenv pyperclip
    ```

* **Chave de API do Gemini Pro:** Obtenha uma chave de API do Google Gemini Pro e salve-a em um arquivo `.env` na raiz do projeto:

    ```
    GENAI_API_KEY=sua_chave_api_aqui
    ```

## Instalação

1.  Clone o repositório para o seu computador:

    ```bash
    git clone [https://github.com/Yurimatheussd/printVoiceG.git](https://github.com/Yurimatheussd/printVoiceG.git)
    cd printVoiceG
    ```

2.  Instale as dependências (caso ainda não tenha feito):

    ```bash
    pip install -r requirements.txt
    ```

3.  Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API do Gemini Pro:

    ```
    GENAI_API_KEY=sua_chave_api_aqui
    ```

## Como Usar

1.  Execute o script `printVoiceG.py`:

    ```bash
    python printVoiceG.py
    ```

2.  Pressione `Ctrl+Shift+V` para capturar a tela.
3.  Selecione a área da tela que deseja capturar usando o atalho `Win+Shift+S` (o script automatiza esse passo).
4.  O texto será extraído, aprimorado e reproduzido em áudio automaticamente.
5.  O texto tratado será copiado para a área de transferência.

## Estrutura de Pastas

* `dados/print`: Armazena as capturas de tela.
* `dados/audio`: Armazena os arquivos de áudio gerados.
* `.env`: Armazena a chave de API do Gemini Pro.
* `printVoiceG.py`: O script principal do projeto.
* `requirements.txt`: Lista as dependências do projeto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o PrintVoiceG.

