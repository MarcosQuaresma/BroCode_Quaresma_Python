# Programa de segmentar emails

email = input("Digite seu email: ")

#                               -ClearCode-
# index = email.index("@")

# usuario = email[:index]
# dominio = email[index +1:] # o "+1" meio que "exclui" o primeiro caractere nesse intervalo da Str.

#                               -ShortCode-
usuario = email[:email.index("@")]
dominio = email[email.index("@") +1:]

print(f"Seu usuário sera: {usuario} \nSeu dominio portanto é: {dominio}")
