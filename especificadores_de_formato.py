# Especificadores de formato = {valor:indicadores} formatar um valor com base no que?
#                                       nos sinalizadores são inseridos.

# .(numero)f = arredonda para essa quantidade de casas decimais (ponto fixo)
# :(numero) = reserva essa quantidade de espaços
# :03 = reserva espaços e preenche com zeros
# :< = alinha à esquerda
# :> = alinha à direita
# :^ = centraliza
# :+ = usa o sinal de mais para indicar um valor positivo
# := = coloca o sinal na posição mais à esquerda
# :  = insere um espaço antes de números positivos
# :, = separador de milhares

preco1 = 3000.14159
preco2 = -9870.65
preco3 = 1200.34

## .(numero)f = arredonda para essa quantidade de casas decimais (ponto fixo)
# print(f"preço1 é: $ {preco1:.2f}")
# print(f"preço2 é: $ {preco2:.5f}")
# print(f"preço3 é: $ {preco3:.1f}")

## :(numero) = reserva essa quantidade de espaços
# print(f"preço1 é: $ {preco1:10}")
# print(f"preço2 é: $ {preco2:15}")
# print(f"preço3 é: $ {preco3:5}")

## :03 = reserva espaços e preenche com zeros
# print(f"preço1 é: $ {preco1:015}")
# print(f"preço2 é: $ {preco2:030}")
# print(f"preço3 é: $ {preco3:03}")

## :< = alinha à esquerda
# print(f"preço1 é: $ {preco1:< }")
# print(f"preço2 é: $ {preco2:< }")
# print(f"preço3 é: $ {preco3:< }")

## :> = alinha à direita
# print(f"preço1 é: $ {preco1:> }")
# print(f"preço2 é: $ {preco2:> }")
# print(f"preço3 é: $ {preco3:> }")

## :^ = centraliza
# print(f"preço1 é: $ {preco1:^ }")
# print(f"preço2 é: $ {preco2:^ }")
# print(f"preço3 é: $ {preco3:^ }")

## :+ = usa o sinal de mais para indicar um valor positivo
# print(f"preço1 é: $ {preco1:+}")
# print(f"preço2 é: $ {preco2:+}")
#print(f"preço3 é: $ {preco3:+}")

# :  = insere um espaço antes de números positivos
# print(f"preço1 é: $ {preco1: }")
# print(f"preço2 é: $ {preco2: }")
# print(f"preço3 é: $ {preco3: }")

# := = coloca o sinal na posição mais à esquerda
# print(f"preço1 é: $ {preco1:=}")
# print(f"preço2 é: $ {preco2:=}")
# print(f"preço3 é: $ {preco3:=}")

# :, = separador de milhares
# print(f"preço1 é: $ {preco1:,}")
# print(f"preço2 é: $ {preco2:,}")
# print(f"preço3 é: $ {preco3:,}")

## combinação de indicadores
print(f"preço 1 é: $ {preco1:+,.2f}")
print(f"preço 2 é: $ {preco2:+,.2f}")
print(f"preço 3 é: $ {preco3:+,.2f}")