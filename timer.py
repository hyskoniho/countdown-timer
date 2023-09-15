import tkinter as tk
from tkinter import messagebox

secs = int(input())
# Recebe o tempo de espera em segundos
# (Esta é a parte que você deve alterar no seu código para informar o tempo que você deseja ou capturá-lo de outra forma

def format_time(secs):
    mins, secs = divmod(secs, 60)
    # Acha a quantidade de minutos
    horas, mins = divmod(mins, 60)
    # Acha a quantidade de horas
    dias, horas = divmod(horas, 24)
    # Acha a quantidade de dias

    time_str = ""
    if dias > 0:
        time_str += f"{dias} dias, "
    if horas > 0:
        time_str += f"{horas} horas, "
    if mins > 0:
        time_str += f"{mins} mins, "
    time_str += f"{secs} segundos"
    # Concatena os valores em uma string, exibindo apenas os valores válidos

    return time_str

def countdown():
    global secs
    if secs > 0:
        time_str = format_time(secs)
        # Pega a string que será exibida no momento atual
        label.config(text=f"Tempo restante: {time_str}")
        # Altera o texto exibido na tela do tkinter
        secs -= 1
        root.after(1000, countdown)
        # 1000 = 1 segundo
    else:
        messagebox.showinfo("Contagem Regressiva", "Tempo esgotado!")
        # Exibe um aviso de término de contagem
        # Fim do programa
        root.destroy()

root = tk.Tk()
root.title("Contagem Regressiva")

label = tk.Label(root)
root.pack(pady=10)
# Define o tamanho da janela

root.attributes('-topmost', True)
# Bota a janela no topo, ou seja, na frente
root.resizable(False, False)
# Impede o usuário de mexer nas dimensões da janela

countdown() if secs > 0 else exit()
# Chama a execução do contador se a quantidade de segundos for válida (maior que 0)
root.mainloop()
# Mantém a janela aberta 
