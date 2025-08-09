import pyautogui
import time
import sys

def click_restart_button():
    print("Iniciando o script de reiniciar vídeo automaticamente...")
    print("Posicione o mouse sobre o botão de reiniciar (↻) em 5 segundos para capturar a posição.")
    
    # Tempo para o usuário posicionar o mouse sobre o botão de reiniciar
    time.sleep(5)
    restart_button_pos = pyautogui.position()  # Pega a posição atual do mouse
    print(f"Posição do botão de reiniciar salva: {restart_button_pos}")
    
    try:
        while True:
            # Move o mouse para o botão de reiniciar e clica
            pyautogui.click(restart_button_pos)
            print("Vídeo reiniciado em:", time.strftime("%H:%M:%S"))
            
            # Espera 1 minuto (60 segundos)
            time.sleep(240)
            
    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário.")
        sys.exit()

if __name__ == "__main__":
    print("⚠️ Deixe o YouTube em tela cheia ou em primeiro plano.")
    click_restart_button()