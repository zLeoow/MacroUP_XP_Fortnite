import cv2
import numpy as np
import pyautogui
import time

# Carregar a imagem que queremos encontrar
imagem_modelo = cv2.imread('mapa.png', 0)

# Definir um limiar para considerar a correspondência
limiar = 0.8

while True:
    # Capturar a tela
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

    # Usar o método de correspondência de template
    resultado = cv2.matchTemplate(screenshot_gray, imagem_modelo, cv2.TM_CCOEFF_NORMED)
    localizacao = np.where(resultado >= limiar)

    # Verificar se a imagem foi encontrada na tela toda
    if len(localizacao[0]) > 0:
        print("Looping reiniciado novamente...")

        # Soltar as teclas 'W' e 'SHIFT'
        pyautogui.keyUp('w')
        pyautogui.keyUp('shift')

        time.sleep(1)
        pyautogui.press('space')
        
        # Segurar as teclas 'W' e 'SHIFT'
        pyautogui.keyDown('w')
        pyautogui.keyDown('shift')
        
        # Esperar um tempo antes de verificar novamente
        time.sleep(0.5)
        
        # Continuar o loop para verificar novamente
        continue
    else:
        time.sleep(1)