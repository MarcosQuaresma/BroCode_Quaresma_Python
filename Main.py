# Talvez 30° programa em Python, justificativa pra aprendizagem... hahaha.
print ("I like Sushi!")
print ("Sushi só é bom cru!")

# Variavel = É um container para um valor (String, Inteitros, Float, Boolean)
#           Uma variavel se comporta com se fosse o valor que contem.

# Strings
primeiro_nome = "Marcos"
comida = "Pizza"
email = "quaresmamarcos@gmail.com"

print(f"Hello {primeiro_nome}!")
print(f"você gostaria de comer {comida}?")
print(f"Seu email é: {email} correto?")

# Inteiros
idade = 25
quantidade = 3
numero_de_estudantes = 10

print(f"Sua iade é {idade} anos.")
print(f"Você esta comprando {quantidade} itens.")
print(f"Sua classe tem {numero_de_estudantes} alunos.")

# Float é um número mas contem uma parte decimal, ex: 3.2
preco = 10.99
media = 8.5
distancia = 3.48

print(f"Preço é {preco}!")
print(f"Sua média anual é: {media}")
print(f"Sua distancia ao trabalho é de {distancia}km.")

# Um Boolean é V ou F, verdadeiro ou falço, "True" or "False" - Primeira letra em Maiúsculo sempre.
#                   Se usa mais internamente, com If e Else, não ficam "expostos"
# e_aluno = False
para_venda = True
esta_online = True

# print(f"Vocé é um aluno? {e_aluno}")
# Resposta: True
# ~~ esse foi um exemplo demonstrativo do Boolean.

# Exemplo usual de boolean com If e Else.
#if e_aluno:
#   print("Você é um aluno!")
#else:
#   print("Você NÃO é um aluno!")
# ~~
if para_venda:
    print("O item esta a venda")
else:
    print("O item NÃO esta a venda")

if esta_online:
    print("Você esta Online")
else:
    print("Você esta Offline")

# Typecasting = O processo de converter um valor de dado para outro tipo de dado.
##              string, inteiro, floa e boolean)
## existem 2 tipos de maneira de fazer isso, a Explicita e a Implicitamente.

# Exemplo Typecasting Explícito:

nome = "Quaresma"
idade = 22
altura = 1.83
estudante = True

ty1 = type(nome)
ty2 = type(idade)
ty3 = type(altura)
ty4 = type(estudante)

print(f"O Typecasting da variável 1 é: {ty1}")
print(f"O Typecasting da variável 2 é: {ty2}")
print(f"O Typecasting da variável 3 é: {ty3}")
print(f"O Typecasting da variável 4 é: {ty4}")

