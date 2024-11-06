import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Lista para armazenar os horários de entrada e saída
registros = []

def marcar_entrada():
    agora = datetime.now()
    registros.append(("Entrada", agora))
    messagebox.showinfo("Marcação de Ponto", f"Entrada registrada em {agora.strftime('%H:%M:%S')}.")

def marcar_saida():
    if not registros or registros[-1][0] != "Entrada":
        messagebox.showerror("Erro", "Você precisa marcar a entrada antes de marcar a saída.")
        return
    
    agora = datetime.now()
    registros.append(("Saída", agora))
    messagebox.showinfo("Marcação de Ponto", f"Saída registrada em {agora.strftime('%H:%M:%S')}.")
    
    # Calcular horas trabalhadas
    entrada = registros[-2][1]
    saida = registros[-1][1]
    horas_trabalhadas = saida - entrada
    registros.append(("Horas Trabalhadas", horas_trabalhadas))

def exibir_registro():
    texto_registro = ""
    total_horas = timedelta()
    
    for item in registros:
        if item[0] == "Entrada" or item[0] == "Saída":
            texto_registro += f"{item[0]}: {item[1].strftime('%H:%M:%S')}\n"
        elif item[0] == "Horas Trabalhadas":
            texto_registro += f"{item[0]}: {item[1]}\n"
            total_horas += item[1]
    
    texto_registro += f"\nTotal de Horas no Dia: {total_horas}"
    
    # Atualizar o texto no label
    labelResultado.config(text=texto_registro)

# Criar a janela principal
janela = tk.Tk()
janela.title("Sistema de Controle de Ponto")
janela.geometry("500x400")

# Frame para centralizar os widgets
frame = tk.Frame(janela)
frame.pack(expand=True)  # Expande o frame para o centro

# Botões
buttonEntrada = tk.Button(frame, text="Marcar Entrada", command=marcar_entrada)
buttonEntrada.pack(pady=5)

buttonSaida = tk.Button(frame, text="Marcar Saída", command=marcar_saida)
buttonSaida.pack(pady=5)

buttonExibir = tk.Button(frame, text="Exibir Registro do Dia", command=exibir_registro)
buttonExibir.pack(pady=5)

# Label para exibir o registro do dia
labelResultado = tk.Label(frame, text="Registro do Dia:", justify="left")
labelResultado.pack(pady=20)

# Executar a janela
janela.mainloop()
