# Funções matemáticas integradas.
# x = 3.14
# y = 4
# z = 5

## Função "round" é uma função integrada:
# resultado = round(x) ## neste caso o "round" irá arredondar para o número inteiro mais próximo (< ou > que 5 após ".")

## Função "abs" é uma função integrada:
# resultado = abs(y) ## neste caso o "abs" irá dar o valor absoluto de "y", significa a distancia de "y" até Zero com um
                     ## número inteiro. a variável erá (y = -4).

## Função "pow" é uma função integrada:
# resultado = pow (y, 3 ) ## neste caso "pow" ele é orientado da seguinte forma: dentro de "pow(a, b)", "a" é a variável
                        ## que será a base, a protencia é representada pela letra "b", nesse exemplo ficaria: y³.
                        ## seria: pow(a, b) -> a^b.

## Função "max" e "min" é uma função integrada:
# resultado = max(x, y, z) ## neste caso "max" irá mostrar o maior valor entre as variáveis. Resultado: 5
# resultado = min(x, y, z) ## neste caso "min" irá mostrar o menor valor entre as variáveis. Resultado: 3.14


# print (resultado)

## Constantes e Funções de classes:
import math

# print(math.pi)
# print(math.e)

# Caso precise, invoque uma funçao sem precisar realizar operações matematicas artezanalmente dentro da linha de código
# por exemplo a raiz quadrada de um número: math.sqrt(n). "n" é uma variável ou um valor.

x = 9.9

# resultado = math.sqrt(x)
# Rint = int(resultado) # print (Rint)
# resultado = math.ceil(x) # neste caso x = 9.1, "math.ceil" arredonda o número pra cima. Resultado = 10
resultado = math.floor(x) # neste caso x = 9.9, "math.floor" arredonda o número pra baixo. Resultado = 9

print (resultado)

