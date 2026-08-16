# while loop = executa um código enquanto uma determinada condição permanecer verdadeira.

# nome = input("Qual é o seu nome? ")

# while nome == "":
#    print("Você não escreveu seu nome")
#    nome = input("Qual é o seu nome? ")
# else:
#    print(f"Olá {nome}, seja bem vindo!")

nome = input("Qual é seu nome? ")
idade = int(input("Qual é a sua idade? "))

while idade < 18:
    print(f"Você não é maior de idade {nome}!")
    if idade <= 0:
        print("Você não pude nem nascer ainda, relaxa ai campeão! ")
    elif idade <= 5:
        print("Você já comeu seus vegetais hoje garotão??")
    elif idade <= 14:
        print("Calma pequeno gafanhoto, ainda tem tempo de curtir a infancia/adolescencia!")
    nome = input("Tem alguém com maioridade? se sim: Qual é seu nome? ")
    idade = int(input("Qual é a sua idade? "))
else:
    print(f"Olá {nome}, você tem maioridade, seja bem vindo!")