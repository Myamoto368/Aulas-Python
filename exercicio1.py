print("Escolha um número e eu vou adivinhar se ele ímpar ou par.")
nmr = int(input("Meu número é: "))

result = nmr % 2

if result == 0:
    print("É par. hehe")
else:
    print("É impar. hehe")