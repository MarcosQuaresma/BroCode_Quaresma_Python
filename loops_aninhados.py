# loops aninhados = um loop aninhado é como um loop dentro de outro loop
#                    loop qualquer:
#                           loop interno:
# ----------------------------------------- EXEMPLOS: ---------------------------------
# while x > 0:
#   while x > 0:
#       print("faça alguma coisa")
# --------------------------------------
# while x > 0:
#     for y in range(9):
#           print("faça alguma coisa")
# --------------------------------------
# for x in range(3):
#   for y in range(9):
#       print("faça alguma coisa")
# --------------------------------------
# for x in range(3):
#   while y > 0:
#       print("faça alguma coisa")

# for x in range(1, 10):
#    print(x, end=" ") # o 'end' na vai separar os caracteres que estiver dentro do 'range()' identificado depois do '='
                      # seja ele qualquer tipo de caractere, ex: espaço vazio; +; ,; etc... Tudo dentro de 1 STR

# Se eu qusier repetir esse loop n(x) vezes, basta por em outro loop (aninhando-o):

for x in range(3):
    for y in range(10): # garanta que o contador do loop INTERNO seja diferente do loop EXTERNO. x & y
        print(y, end="|")
    print(" : ") # a cada rodada do 'range(x)' ele imprimira uma sequnecia do 'print(x)'
