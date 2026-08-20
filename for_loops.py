# for loops = executa um bloco de código em um numero fixo de vezes.
#                       Voce pode interagir com intervalo, string, sequencia, etc. Qualquer coisa interagivel.

# for x in reversed(range(1, 11, )): # estrututra simples de "for loop"
#     print(x)

# cartao_de_credito = "1234-5678-9012-3456"
# for  x in (cartao_de_credito):
#    print(x)

for x in range(1, 21):
    if x == 13:
        #~~ continue # palavra chave para "ignorar" algo
        break #~~ nesse caso se houver a identificação positiva para uma linha de código designada no "if"
              #~~ ele para a continuidade ou sequencia. "sairemos do loop"
    else:
        print(x)