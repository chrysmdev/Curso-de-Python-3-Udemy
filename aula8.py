nome = input("Qual o seu primeiro nome? ")
sobrenome = input("Qual o seu sobrenome? ")
idade = input("Qual a sua idade? ")
ano_nascimento = input("Qual o seu ano de nascimento? ")
maior_de_idade = int(idade) >= 18
altura_metros = input("Qual a sua altura (metros)? ")

if maior_de_idade:
    maior_de_idade = "Sim, é maior de idade"
else:
    maior_de_idade = "Não, não é maior de idade"

print()
print("------ Formulario ------")
print("Nome:", nome)
print("Sobrenome:", sobrenome)
print("Idade:", idade)
print("Ano de nascimento:", ano_nascimento)
print("É maior de idade?", maior_de_idade)
print("Altura em metros:", altura_metros, " metros")
