# from tkinter import *
# class Janela:
#     def __init__(self,toplevel):
#         self.fr1=Frame(toplevel)
#         self.fr1=Pack()
#         self.botao=Button(self.fr1,text='bem-vindo',background='green')
#         self.botao.pack()
# raiz=Tk()
# # Janela(raiz)
# # raiz.mainloop()        

import tkinter as tk
import time

def atualizar_horario():
    relogio = time.strftime('%H:%M:%S')
    label.config(text=relogio)
    label.after(1000, relogio)  # Atualiza a cada 1000ms (1 segundo)

Gui = tk.Tk()
Gui.title('Relógio Digital')

label = tk.Label(Gui, font=('Helvetica', 48), bg='red', fg='white')
label.pack(padx=20, pady=20)
frame = tk.Frame(Gui, width=200, height=100, borderwidth=2, relief="solid")
frame.pack()

atualizar_horario()

Gui.mainloop()
