import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

# Criação da tabela de tarefas, se não existir
cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               status TEXT)""")
conexao.commit()

# Função para buscar tarefas no banco de dados
def buscar_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    return cursor.fetchall()

# Função para atualizar a lista de tarefas exibida na interface
def atualizar_lista():
    for row in tree.get_children():
        tree.delete(row)
    tarefas = buscar_tarefas()
    for tarefa in tarefas:
        tree.insert("", "end", values=tarefa)

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    def salvar_tarefa():
        nome = entry_nome.get()
        if nome:
            cursor.execute("INSERT INTO tarefas (nome, status) VALUES (?, ?)", 
                           (nome, "Pendente"))
            conexao.commit()
            atualizar_lista()
            janela_add.destroy()
        else:
            messagebox.showerror("Erro", "O nome da tarefa deve ser preenchido.")

    janela_add = tk.Toplevel(janelaMain)
    janela_add.title("Adicionar Tarefa")
    
    tk.Label(janela_add, text="Nome da Tarefa").grid(row=0, column=0)
    entry_nome = tk.Entry(janela_add)
    entry_nome.grid(row=0, column=1)

    btn_salvar = tk.Button(janela_add, text="Salvar", command=salvar_tarefa)
    btn_salvar.grid(row=1, columnspan=2)

# Função para marcar uma tarefa como concluída
def marcar_concluida():
    item_selecionado = tree.selection()
    if item_selecionado:
        tarefa = tree.item(item_selecionado)['values']
        cursor.execute("UPDATE tarefas SET status=? WHERE id=?", ("Concluída", tarefa[0]))
        conexao.commit()
        atualizar_lista()
    else:
        messagebox.showerror("Erro", "Selecione uma tarefa para marcar como concluída.")

# Função para deletar uma tarefa
def deletar_tarefa():
    item_selecionado = tree.selection()
    if item_selecionado:
        tarefa = tree.item(item_selecionado)['values']
        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir a tarefa?")
        if resposta:
            cursor.execute("DELETE FROM tarefas WHERE id=?", (tarefa[0],))
            conexao.commit()
            atualizar_lista()
        else:
            messagebox.showinfo("Cancelado", "Exclusão cancelada.")
    else:
        messagebox.showerror("Erro", "Selecione uma tarefa para deletar.")

# Configuração da interface gráfica principal
janelaMain = tk.Tk()
janelaMain.title("Gerenciador de Tarefas")

btn_adicionar = tk.Button(janelaMain, text="Adicionar Tarefa", command=adicionar_tarefa)
btn_adicionar.grid(row=0, column=0, padx=10, pady=10)

btn_listar = tk.Button(janelaMain, text="Listar Tarefas", command=atualizar_lista)
btn_listar.grid(row=0, column=1, padx=10, pady=10)

btn_concluir = tk.Button(janelaMain, text="Marcar como Concluída", command=marcar_concluida)
btn_concluir.grid(row=0, column=2, padx=10, pady=10)

btn_deletar = tk.Button(janelaMain, text="Excluir Tarefa", command=deletar_tarefa)
btn_deletar.grid(row=0, column=3, padx=10, pady=10)

# Criação da árvore para exibir as tarefas
tree = ttk.Treeview(janelaMain, columns=("ID", "Nome", "Status"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Status", text="Status")
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Carregar a lista de tarefas inicialmente
atualizar_lista()

# Iniciar a interface gráfica
janelaMain.mainloop()

# Fechar a conexão com o banco de dados ao encerrar a aplicação
conexao.close()
