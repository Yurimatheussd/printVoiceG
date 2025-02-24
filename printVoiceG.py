import pyautogui
import keyboard
import pytesseract
from gtts import gTTS
import os
import time
import win32clipboard
from PIL import Image, ImageGrab, ImageEnhance
import google.generativeai as genai
from dotenv import load_dotenv
import pyperclip

load_dotenv()
api_key = os.getenv('GENAI_API_KEY')
genai.configure(api_key=api_key)

# Cria as pastas se não existirem
if not os.path.exists('dados/print'):
    os.makedirs('dados/print')
if not os.path.exists('dados/audio'):
    os.makedirs('dados/audio')

def capture_screenshot():
    print("Atalho pressionado! Capturando com Win + Shift + S...")
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    keyboard.send("win+shift+s")
    time.sleep(5)
    image = None
    for _ in range(10):
        time.sleep(0.5)
        image = ImageGrab.grabclipboard()
        if image:
            break
    if image is None:
        print("Nenhuma imagem encontrada na área de transferência!")
        return None
    filename = f"dados/print/screenshot_{int(time.time())}.png" #salva na pasta print
    image.save(filename)
    print(f"Screenshot salva como {filename}")
    return filename

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert("L")
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)
        text = pytesseract.image_to_string(image, lang="por")
        image.close()
        text = text.strip()
        print(f"Texto extraído: {text if text else 'Nenhum texto encontrado.'}")
        return text
    except Exception as e:
        print(f"Erro ao processar imagem: {e}")
        return ""

def improve_text_with_gemini(text):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Logo em seguida estou te passando um texto, corrija e ajuste para leitura, caso tenha horas, ajuste-as corretamente junto ao texto, mas traga o resto do texto junto. Não altere muito a estrutura do texto. Não traga mais nada na resposta fora o texto: {text}"
    response = model.generate_content(prompt)
    improved_text = response.text.strip()
    print("\nTexto tratado pelo Gemini Pro:\n" + improved_text + "\n")
    return improved_text

def text_to_speech(text):
    if not text:
        print("Nenhum texto para converter em áudio.")
        return
    filename = f"dados/audio/output_{int(time.time())}.mp3" #salva na pasta audio
    tts = gTTS(text=text, lang='pt')
    tts.save(filename)
    print(f"Reproduzindo áudio: {filename}")
    if os.name == "nt":
        os.system(f"start {filename}")
        time.sleep(1) #da um tempo para o reprodutor de midia abrir.
        keyboard.send("ctrl+shift+k") #simula o atalho ctrl+shift+k

def main():
    print("Pressione Ctrl+Shift+V para capturar a tela e ouvir o texto.")
    while True:
        keyboard.wait("ctrl+shift+v")
        screenshot_path = capture_screenshot()
        if screenshot_path:
            text = extract_text_from_image(screenshot_path)
            if text:
                improved_text = improve_text_with_gemini(text)
                text_to_speech(improved_text)
                pyperclip.copy(improved_text)
            else:
                print("Nenhum texto encontrado na imagem.")

if __name__ == "__main__":
    main()