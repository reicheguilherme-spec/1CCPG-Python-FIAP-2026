print("hello world top")
print("hello world 2")

print(7 + 4)
print("7 + 4")
print("7" + "4") # concatenando strings

# Comentário de 1 linha
'''
    Comentários de 
    múltiplas   
    linhas
'''

# VARIÁVEIS
nome = "Guilherme" # str
idade = 18 # int
peso = 70.2 #float

print("Corinthians \n", nome, idade, peso)
print(f"Olá, {nome}!!!")


# INPUT -- SIMULAÇÃO DE UM FORMS NO CMD
nome = input("Digite o seu nome: ")
print(nome)
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade}")
