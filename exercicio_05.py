## Calculando a área de um círculo: A = pi*r²

import math

r = float(input("Digite o valor do raio em cm: " ))

A = math.pi * pow(r, 2)   # math.pi * r**2

print(f"Portando a Area do cículo é: ~ {round(A, 2)}cm²")