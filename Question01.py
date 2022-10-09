a = int(input("Informe o primeiro valor:"))
b = int(input("Informe o segundo valor:"))
c = int(input("Informe o terceiro valor:"))
soma = a + b + c

if a <= 0 or b <= 0 or c <= 0:
    print("Os valores de entrada não podem ser negativos (<0)")

print("A Soma: ", a + b + c)

print("A Média: ", (a + b + c)/3)

if soma <= 50:
    print("O valor é menor que 50!")