# Métodos úteis para strings

# nome = input("Digite seu nome completo: ")
# telefone = input("Digite seu telefone: ")

# resultado = len(nome) # ele retorna um inteiro(int) com a quantidade
                        # de caracteres tem ums "srt" com espaços e tudo.
# .find() ele retorna a primeira ocorrencia de um determinado caractere.
# resultado = nome.find("M") # no nome "Marcos Pedrosa Quaresma" é no índice 6
                             # porque sempre começamos com ZERO. indice "M" = 0
# resultado = nome.rfind("m") # aqui ele ira procurar a ÚLTIMA vez que ocorreu o
                              # índice "m" minúsculo.
# ~~ caso não encontre nada retornara "-1" no terminal.
# resultado = nome.capitalize() # Primeira letra da frase ficara em Maiúsculo.
# resultado = nome.upper() #Toda a "srt" em MAIÚSCULO.
# resultado = nome.lower() #Tudo em minúsculo.
# resultado = nome.isdigit() # Só retorna True se for apenas Dígitos, else = False
# resultado = nome.isalpha() # só retorna True se conter apenas caractere alfabetico
                             # caso tenha um " " vazio ou algo que não seja somente
                             # "srt" ele devolve False
# resultado = telefone.count("-") # ele conta quantos caracteres existe na srt
# resultado = telefone.replace("-", " ") # ele troca um caractere "x" por um caractere "y".

## LISTA COMPLETA DE TODOS OS METODOS BASTA INVOCAR:
##                         print(help(str))

print(help(str))

# print(resultado)