from calculo_imposto import calculo_imposto

def main():
    try:
        salario = float(input("Quanto se ganha? "))
        aliquota = float(input("Digite aliquota entre 0 e 1: "))

        # Chamar a função correta
        calculo_imposto = calculo_imposto(salario, aliquota)

        print(f"O roubo sobre seu salário de R${salario} com uma aliquota de {aliquota*100}% é R${calculo_imposto:.2f}.")

    except ValueError as e:
        print(f"Erro: {e}")
    
if __name__ == "__main__":
    main()
