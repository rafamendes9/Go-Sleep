import pygetwindow as gw
import pyautogui
import time

def fechar(programa):
    try:
        # Procura a janela na bandeja do sistema (Metodo para programas que atuam em segundo plano e/ou estao minimizados)
        janela = None
        for window in gw.getAllTitles():
            if programa.lower() in window.lower():
                janela = gw.getWindowsWithTitle(window)[0]
                break
        
        # Caso não encontre programas que atua em segundo plano e/ou esta minimizado
        if not janela:
            raise IndexError(f"Não foi possível encontrar o programa {programa} na bandeja do sistema.")

        # Restaura a janela antes de fechar
        janela.restore()
        time.sleep(1)  # Aguarda um momento para a janela ser restaurada

        # Foca na janela do programa
        janela.activate()

        # Pressiona Alt + F4 para fechar a janela
        pyautogui.hotkey('alt', 'f4')

        print(f"Programa {programa} foi fechado.")
    except Exception as e:
        print(f"Erro ao fechar o programa {programa}: {e}")

# Coloque o "programa" que deseja fechar aqui em baixo
# (por padrao está os meus programas mas voce pode personalizar a sua escolha)
fechar("Discord")
fechar("Steam")
fechar("Firefox")

# Adiciona uma pausa para que o console não se feche imediatamente
input("Pressione Enter para fechar o console e DURMA BEM o7")
