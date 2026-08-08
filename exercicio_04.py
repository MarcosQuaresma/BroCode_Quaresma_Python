## Exercícios: calculando a circunferencia de um círculo: C = 2*pi*r
import math

r = float(input("Digite o raio do círculo em cm: "))

C = 2 * math.pi * r

print(f"Portanto a cicunferencia do cículo é de ~{round(C, 2)} cm")