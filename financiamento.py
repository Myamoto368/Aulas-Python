import tkinter as tk
from tkinter import messagebox

def calcularPrestacao():
    try:
        valor_financiamento = float(entryValor.get())
        taxa_juros = float(entryJuros.get()) / 100 
        num_meses = int(entryMeses.get())
        
        if valor_financiamento <= 0 or taxa_juros <= 0 or num_meses <= 0:
            raise ValueError("Todos os valores devem ser maiores que zero.")
        
        prestacao = (valor_financiamento * taxa_juros * (1 + taxa_juros)**num_meses) / ((1 + taxa_juros)**num_meses - 1)
        
        labelResultado.config(text=f"Prestação Mensal: R$ {prestacao:.2f}")
    
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")

janela = tk.Tk()

janela.title("Calculo Financiamento")
janela.geometry("400x150")

labelValor1 = tk.Label(janela, text="Digite o valor do financiamento:")
labelValor1.grid(row=0, column=0)
entryValor = tk.Entry(janela)
entryValor.grid(row=0, column=1)

labelValor2 = tk.Label(janela, text="Juros Mensais:")
labelValor2.grid(row=1, column=0)
entryJuros = tk.Entry(janela)
entryJuros.grid(row=1, column=1)

labelValor3 = tk.Label(janela, text="Digite o número de parcelas:")
labelValor3.grid(row=2, column=0)
entryMeses = tk.Entry(janela)
entryMeses.grid(row=2, column=1)

buttonCalcular = tk.Button(janela,text="Calcular",command=calcularPrestacao)
buttonCalcular.grid(row=3, column=0, columnspan=2)

labelResultado = tk.Label(janela,text="R$ 0.00")
labelResultado.grid(row=5,column=1,columnspan=2)

janela.mainloop()