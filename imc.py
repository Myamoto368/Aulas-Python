import tkinter as tk
from tkinter import messagebox

def calcularIMC():
    try:
        altura = float(entryaltura.get())
        peso = float(entrypeso.get())
        
        if peso <= 0 or altura <= 0:
            raise ValueError("Todos os valores devem ser maiores que zero. Até porquê nunca vi ninguém com a altura ou peso negativo ou zerado mano... Mais sei lá, cada um tem suas experiências.")
        
        IMC = (peso/(altura**2))
        
        labelResultado.config(text=f"Seu IMC é: {IMC:.2f}")
    
    except ValueError as e:
        messagebox.showerror("Erro, alguém ta fazendo burrice.", f"Entrada inválida: {e}")

janela = tk.Tk()

janela.title("Adivinhamos seu IMC por 2 reais.")
janela.geometry("400x150")

labelValor1 = tk.Label(janela, text="Altura:")
labelValor1.grid(row=0, column=0)
entryaltura = tk.Entry(janela)
entryaltura.grid(row=0, column=1)

labelValor2 = tk.Label(janela, text="Peso:")
labelValor2.grid(row=1, column=0)
entrypeso = tk.Entry(janela)
entrypeso.grid(row=1, column=1)

buttonCalcular = tk.Button(janela,text="Calcular",command=calcularIMC)
buttonCalcular.grid(row=3, column=0, columnspan=2)

labelResultado = tk.Label(janela,text="IMC 0.0")
labelResultado.grid(row=5,column=1,columnspan=2)

janela.mainloop()