# Carirnho de compras

comidas = [] # .append precisa estar vinculado a essa variável
precos = []  # .append precisa estar vinculado a essa variável
total = 0

while True:
    comida = input("Digite qual comida você quer comprar ('x' para sair): ")
    if comida.lower() == "x":
        break
    else:
        preco = float(input(f"Digite o valor de(a) {comida} em R$: "))
        comidas.append(comida)
        precos.append(preco)

print("********** Seu Carrinho **********")

for comida in comidas:
    print(f"{comida}")

for preco in precos:
    total += preco
print(f"O total da compra foi R${total:.2f}")