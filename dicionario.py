biblioteca = {}

def adicionar_livro():
    codigo = input("Qual código do livro você irá adicionar? ")
    if codigo in biblioteca:
        print("Erro: Código do livro duplicado. Esse código já existe.")
        return
    livro = input("Qual livro irá adicionar? ")
    autor = input("Qual o autor do livro? ")
    ano = input("Qual o ano do livro? ")
    biblioteca[codigo] = {"livro": livro, "autor": autor, "ano": ano}
    print("Livro adicionado com sucesso!")

def buscar_livro():
    chave = input("Digite o código do livro que deseja buscar: ")
    if chave in biblioteca:
        print(f"Livro encontrado: {biblioteca[chave]}")
    else:
        print("Livro não encontrado na biblioteca.")

def atualizar_livro():
    codigo = input("Digite o código do livro que deseja atualizar: ")
    if codigo in biblioteca:
        chave = input("Digite o dado que deseja atualizar (livro, autor, ano): ")
        if chave in biblioteca[codigo]:
            novo_valor = input(f"Digite o novo valor para {chave}: ")
            biblioteca[codigo][chave] = novo_valor
            print("\nDicionário após atualização:")
            print(biblioteca[codigo])
        else:
            print(f"O dado '{chave}' não existe para o livro com código {codigo}.")
    else:
        print("Livro não encontrado na biblioteca.")

def remover_livro():
    codigo = input("Digite o código do livro que deseja remover: ")
    if codigo in biblioteca:
        del biblioteca[codigo]
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado na biblioteca.")

def listar_livros():
    if biblioteca:
        print("\nLista de todos os livros:")
        for codigo, dados in biblioteca.items():
            print(f"Código: {codigo}, Título: {dados['livro']}, Autor: {dados['autor']}, Ano: {dados['ano']}")
    else:
        print("A biblioteca está vazia.")

while True:
    print("\nEscolha uma operação:")
    print("1. Adicionar Livro")
    print("2. Buscar Livro")
    print("3. Atualizar Livro")
    print("4. Remover Livro")
    print("5. Listar Todos os Livros")
    print("6. Sair")
    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        buscar_livro()
    elif opcao == "3":
        atualizar_livro()
    elif opcao == "4":
        remover_livro()
    elif opcao == "5":
        listar_livros()
    elif opcao == "6":
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")