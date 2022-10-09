nomefuncionario = str(input("Seu nome? "))
vendasq = int(input("Quantas vendas você fez? ")) 
somadev=0

for i in range(1,vendasq+1):
    abc_loop = float(input(f"Valor {i}:"))
    somadev+=abc_loop
    media = somadev/vendasq

if media>=500000:
    print("Muito bem", nomefuncionario,"! Você atingiu a meta! Parabens! ")
else:
    print("Ah que pena" , nomefuncionario,"! Você não atingiu a meta!")