# if = é usada para executar um código somente se uma determinada condição que definimos for True
#      caso contrário iremos fazer Else, é uma forma básica de tomar decisão, baseada em "Ture" e "False"
# If = se
# else = se não
# elif = senão se (caso contrário, faça outra coisa completamente diferente.)

idade = int(input("Qual a sua idade: "))

if idade >= 100:
    print("Eu acho que Deus gostou de você aqui na terra, parabéns, mas você é muito Svelho pra se inscrever!")

elif idade >= 18:
    print("Você esta cadastrado!")
elif idade < 0:
    print("Você ainda esta no saco do seu pai!")
elif idade <= 0:
    print("Você ainda esta no saco do seu pai ou ta na barriga da mãe!")

else:
    print("Você precisa ser maior de idade com >= 18 anos!")