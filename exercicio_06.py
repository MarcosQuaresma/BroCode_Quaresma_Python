## Calculando a hipotenusa de um triangulo: C = sqrt(a²+b²)
import math

a = float(input("Qual o valor de ""a"" em cm? "))
b = float(input("Qual o valor de ""b"" em cm? "))

c = math.sqrt (pow(a, 2) + pow(b, 2)) # math.sqrt(a**2 + b**2)

print(f"Portanto o valor da hipotenusa em cm é de: {round(c, 2)} cm")
