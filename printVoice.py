import pyautogui
import keyboard
import pytesseract
from gtts import gTTS
import os
import time
import win32clipboard
from PIL import Image, ImageGrab, ImageEnhance

def capture_screenshot():
    print("Atalho pressionado! Capturando com Win + Shift + S...")
    
    # Simula o atalho de captura do Windows
    keyboard.send("win+shift+s")

    # Aguarda o usuário selecionar a área
    time.sleep(3)  # Tempo para ele escolher a região

    # Aguarda a imagem ser copiada para a área de transferência
    image = None
    for _ in range(10):  # Tenta por 10 tentativas (5s no total)
        time.sleep(0.5)  # Aguarda meio segundo entre tentativas
        image = ImageGrab.grabclipboard()
        if image:
            break
    
    if image is None:
        print("Nenhuma imagem encontrada na área de transferência!")
        return None
    
    filename = f"screenshot_{int(time.time())}.png"
    image.save(filename)
    print(f"Screenshot salva como {filename}")
    return filename

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        image = image.convert("L")  # Converte para escala de cinza
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)  # Aumenta o contraste

        text = pytesseract.image_to_string(image, lang="por")
        image.close()

        text = text.strip()
        print(f"Texto extraído: {text if text else 'Nenhum texto encontrado.'}")
        return text
    except Exception as e:
        print(f"Erro ao processar imagem: {e}")
        return ""

def text_to_speech(text):
    if not text:
        print("Nenhum texto para converter em áudio.")
        return
    
    filename = f"output_{int(time.time())}.mp3"
    tts = gTTS(text=text, lang='pt')
    tts.save(filename)
    
    print(f"Reproduzindo áudio: {filename}")
    if os.name == "nt":
        os.system(f"start {filename}")

def main():
    print("Pressione Ctrl+Shift+V para capturar a tela e ouvir o texto.")
    
    while True:
        keyboard.wait("ctrl+shift+v")
        screenshot_path = capture_screenshot()
        if screenshot_path:
            text = extract_text_from_image(screenshot_path)
            text_to_speech(text)

if __name__ == "__main__":
    main()
