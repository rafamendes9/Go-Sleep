import pygetwindow as gw
import pyautogui
import time

def fechar(programa):
    try:
        # Procura todas as janelas do programa na bandeja do sistema
        janelas = [window for window in gw.getWindowsWithTitle(programa) if programa.lower() in window.title.lower()]

        # Caso não encontre programas que atuam em segundo plano e/ou estão minimizados
        if not janelas:
            raise IndexError(f"Não foi possível encontrar janelas do programa {programa} na bandeja do sistema.")

        # Fecha cada janela do programa
        for janela in janelas:
            # Restaura a janela antes de fechar
            janela.restore()
            time.sleep(1)  # Aguarda um momento para a janela ser restaurada

            # Foca na janela do programa
            janela.activate()

            # Pressiona Alt + F4 para fechar a janela
            pyautogui.hotkey('alt', 'f4')

        print(f"Todas as janelas do programa {programa} foram fechadas.")
    except Exception as e:
        print(f"Erro ao fechar as janelas do programa {programa}: {e}")

# Coloque o "programa" que deseja fechar aqui em baixo
# (por padrão, estão listados meus programas, mas você pode personalizar a sua escolha)
fechar("Discord")
fechar("Firefox")

# Adiciona uma pausa para que o console não se feche imediatamente
input("Pressione Enter para fechar o console e DURMA BEM o7")