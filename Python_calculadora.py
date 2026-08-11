# Python Calculadora:
import math

print("Escolher um operador (+ - * / ^ sqrt)")
print("+ = soma \n - = subtração \n * = multiplicação \n / = divisão\n ^ = potenciação\n sqrt = raiz quadrada")

operadores = input("Operador: ")
num1 = float(input("Primeiro numero: "))
num2 = float(input("Segundo numero: "))

if operadores == "+":
    resultado = num1 + num2
    print (resultado)

elif operadores == "-":
    resultado = num1 - num2
    print (resultado)

elif operadores == "*":
    resultado = num1 * num2
    print (resultado)

elif operadores == "/":
    resultado = num1 / num2
    print (round(resultado, 3))

elif operadores == "^":
    resultado = pow(num1, num2)
    print (round(resultado, 3))

elif operadores == "sqrt":
    resultado = round((math.sqrt(num1)), 3), round(math.sqrt(num2), 3)
    print (resultado)
else:
    print(f"{operadores} não é um operador válido")
