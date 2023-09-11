import tkinter as tk
from tkinter import messagebox

secs = int(input())
# Recebe o tempo de espera em segundos

def format_time(secs):
    mins = secs // 60
    secs = secs % 60
    # Acha a quantidade de minutos

    horas = mins // 60
    mins = mins % 60
    # Acha a quantidade de horas

    dias = horas // 24
    horas = horas % 24
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
        label.config(text=f"Tempo restante: {time_str}")
        secs -= 1
        root.after(1000, countdown)
    else:
        messagebox.showinfo("Contagem Regressiva", "Tempo esgotado!")
        # Exibe um aviso de término de contagem
        # Fim do programa

root = tk.Tk()
root.title("Contagem Regressiva")

label = tk.Label(root, text="")
label.pack(pady=10)

countdown()

root.mainloop()
    
