# Validando o input do usuário
# 1° Usuário não pode ter mias que 12 caracteres
# 2° Usuário naõ pode conter espaços
# 3° Usuário não pode conter dígitos numericos

us = input("Qual o seu nome? ")
us.find(" ")
us.isalpha()

if len(us) > 12:
    print("Seu nome não pode ter mais de 12 caracteres")
elif not us.find(" ") == -1:
    print("Seu usuário contem espaço!! ")
elif not us.isalpha():
    print("Seu usuário não pode conter números")
else:
    print(f"Bem vindo {us}!!")
