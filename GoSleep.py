import tkinter as tk
from tkinter import ttk
import pygetwindow as gw
import pyautogui
import time

def fechar_programa(programa):
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

def fechar_programas_selecionados():
    programas_selecionados = listbox.get(0, tk.END)
    for programa in programas_selecionados:
        fechar_programa(programa)

# Criando a interface gráfica
root = tk.Tk()
root.title("Fechar Programas")

# Adicionando uma lista de programas para o usuário escolher

# colocar programas aqui
programas = ["Discord", "Firefox"]
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for programa in programas:
    listbox.insert(tk.END, programa)
listbox.pack(pady=10)

# Botão para fechar os programas selecionados
fechar_button = ttk.Button(root, text="Fechar Programas Selecionados", command=fechar_programas_selecionados)
fechar_button.pack(pady=10)

# Adiciona uma pausa para que o console não se feche imediatamente
exit_button = ttk.Button(root, text="Fechar", command=root.destroy)
exit_button.pack(pady=10)

root.mainloop()
