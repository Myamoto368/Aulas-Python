import tkinter as tk
from PIL import Image, ImageTk 
from tkinter import ttk 

janela2 = tk.Tk()
janela2.title("Adicionar Funcionário")
janela2.geometry("768x429")

imagemFundo = Image.open("download.gif")
ImageResized = imagemFundo.resize((768, 429), Image.NEAREST)
imagemFundo = ImageTk.PhotoImage(ImageResized)
labelImage = tk.Label(janela2, image=imagemFundo)
labelImage.image = imagemFundo
labelImage.place(x=0,y=0,width=768,height=429)

frame = tk.Frame(janela2)
frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(frame, text="Nome:").grid(row=1, column=0, sticky='n')
entry_nome = tk.Entry(frame)
entry_nome.grid(row=1, column=1)

tk.Label(frame, text="Idade:").grid(row=2, column=0, sticky='n')
entry_idade = tk.Entry(frame)
entry_idade.grid(row=2, column=1)

tk.Label(frame, text="Cargo:").grid(row=3, column=0, sticky='n')
entry_cargo = tk.Entry(frame)
entry_cargo.grid(row=3, column=1)

tk.Label(frame, text="Departamento:").grid(row=4, column=0, sticky='n')
entry_departamento = tk.Entry(frame)
entry_departamento.grid(row=4, column=1)

tk.Label(frame, text="Salário:").grid(row=5, column=0, sticky='n')
entry_salario = tk.Entry(frame)
entry_salario.grid(row=5, column=1)

tk.Label(frame, text="Telefone:").grid(row=6, column=0, sticky='n')
entry_telefone = tk.Entry(frame)
entry_telefone.grid(row=6, column=1)

tk.Label(frame, text="Email:").grid(row=7, column=0, sticky='n')
entry_email = tk.Entry(frame)
entry_email.grid(row=7, column=1)


btn_salvar = tk.Button(janela2, text="Salvar")
btn_salvar.grid(row=2, column=0, padx=10, pady=(10, 10))

janela2.mainloop()