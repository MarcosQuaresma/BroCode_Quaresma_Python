# Calculadora dde juros compostos em PYTHON

capital_inicial = 0
juros = 0
tempo = 0

while capital_inicial <= 0:
    capital_inicial = float(input("Digite seu capital inicial: "))
    if capital_inicial <= 0:
        print("O capital inicial não pode ser menor ou igual a 0")

while juros <= 0:
    juros = float(input("Digite a taxa de juros: "))
    if juros <= 0:
        print("O juros não pode ser menor ou igual a 0")

while tempo <= 0:
    tempo = int(input("Digite quanto tempo: "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual a 0")

total = capital_inicial * pow((1 + juros/100),tempo)
print(f"O balanço apos {tempo} anos é de: R$ {total:.2f} ")