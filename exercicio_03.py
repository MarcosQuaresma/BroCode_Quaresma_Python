# Programa de carrinho de compras.
item = input ("Qual item você gostaria de comprar? ")
price = float(input ("Qual é o preço? "))
quantidade = int(input ("Quantos você gostaria? "))

total = price * quantidade

desconto = total * 0.10
Ftotal = total - desconto

print(f"Voce comprou {quantidade} x {item} Total: R$ {round(total), 2} \n Com 10% de desconto: ")
print(f"Total a ser pago: R$ {round(Ftotal), 2}")
