"""
iNICIAR COM LETRA, PODE CONTER NÚMEROS, SEPARAR _, LETRAS MINÚSCULAS

"""

nome = "Joaquim Carvalho"
idade= 2  #int
altura= 0.98  # float
peso= 20
e_maior = idade > 18 # boll
data_1 = True  # boll
data_nas= 2020
imc = peso / altura


print("Nome: ", nome)
print("idade: ", idade, "anos")
print("Altura: ", altura, "cm")
print("É maior: ", e_maior)
print("O ano do seu nascimento é: ", data_nas)


print(nome, "tem", idade, "anos de idade, tem ", altura, "cm e pesa ", peso, "KG")
print("O imc de", nome, " é de:" , imc)
print(nome, "nasceu em " ,data_nas)