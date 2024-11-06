nmr = int(input("Digite um número: "))

soma = 1

for cont in range(1, nmr):
    soma = soma + cont
    print(f"{soma} + {cont} = {soma}")

print(f"Resultado: {soma}")