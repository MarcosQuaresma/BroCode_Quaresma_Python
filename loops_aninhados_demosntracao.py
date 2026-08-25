# Um usuário qualquer podera criar um retangulo ou quadrado perfeito. Demonstração em Loop Aninhado:

print("Bem vindo a demonstração de loops aninhados! \nRepresentação retangulos/quadrados.\n ->Valores inteiros.")
largura = int(input("Qual a largura do retangulo? "))
altura = int(input("Qual a altura do retangulo? "))
simbolo = input("Qual o simbolo irá usar para representação? ")

for x in range(largura):
    for y in range(altura):
        print(simbolo, end="")
    print("")
print(f"Portando a Area da sua figura é: {(altura * largura)} cm² !")

# Observe, essa é uma linha de código simples, não é algo tão complexo, mas tem seu valor.