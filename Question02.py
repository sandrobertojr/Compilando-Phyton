from ast import If


aluno=input("Nome do aluno: ")
quant_notas=int(input("Quantas notas ? "))
count=1; media = 0.0
while count <= quant_notas:
    print("Informe a nota ", count, ":")
    nota = float(input())
    if nota >= 0 and nota <= 10: 
      print("----------")        
      media += nota
      count += 1
    else:
      print("###############")        
      print("Nota errada, ", nota, ":")
      print("Informe novamente a nota do aluno ", count, ":")
      nota = float(input() )
      media += nota
      count += 1
print("A media do aluno",aluno,"é de :",(media/quant_notas) )
if media/quant_notas >=7:
    print("APROVADO! VOCÊ PASSOU POR MÉDIA!")
else:
    print("REPROVADO! Vá estudar mais!")