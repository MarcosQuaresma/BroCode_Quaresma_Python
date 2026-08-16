#                 Indexação de String(str)
# Indexação = permite acessar elementos de uma sequencia usando um conjunto de colchetes [] (operador de indexação)
#             [start : end : step]

num_credito = "1234-5678-9012-3456"

print(num_credito[0])  # se eu quiser o primero caractere da Str. (start)
print(num_credito[1])  # se eu quiser o segundo caractere da Str. (start)
print(num_credito[4])  # se eu quiser o quinto caractere da Str. (start)

print(num_credito[0:4])  # se eu quiser-mos os 4 primeiros caractere da Str. (start : end)
print(num_credito[5:9])  # se eu quiser mostar do 5° ao 9° caractere na Str. (start : end)
print(num_credito[7:])   # se eu quiser que mostre todos os caracteres na Str depois do 7° (start : end)

print(num_credito[-1])   # se eu quiser que mostre o ultimo caracteres na Str. ( : end)
print(num_credito[-2])   # se eu quiser que mostre o penultimo caracteres na Str. (: end)

print(num_credito[::2])  # Isso imprimirá com um intervalo de 2 caracteres. ( :: step)
print(num_credito[::3])  # Isso imprimirá com um intervalo de 3 caracteres. ( :: step)