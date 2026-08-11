# Conversor de temperatura de °F, °C e Kelvin (K)

print("Conversor de temperaturas, °F, °C e Kelvin(K)")

valorTempe = float(input("Digite o valor da temperatura: "))
nomTempe = input("(em maiúsculo) - Esta em qual unidade de medida?  (digite: F, C ou K)")
convTempe = input("(em maiúsculo) - Para qual unidade de medida quer converter? (digite: F, C, K)")

seq = nomTempe + convTempe

CparaF = (valorTempe - 32) * 5/9
FparaC = (valorTempe * 9) / 5 + 32

CparaK = valorTempe + 273.15
KparaC = valorTempe - 273.15

FparaK = (valorTempe - 32) * (5/9) + 273.15
KparaF = (valorTempe - 273.15) * (5/9) + 32

if seq == "CF":
    print(f"A conversão de {valorTempe} Celsius para Fahrenheit é °F {round(CparaF, 2)}")
elif seq == "FC":
    print(f"A conversão de {valorTempe} Fahrenheit para Celsius é °C {round(FparaC, 2)}")
elif seq == "CK":
    print(f"A conversão de {valorTempe} Celsius para Kelvin é °K {round(CparaK, 2)}")
elif seq == "KC":
    print(f"A conversão de {valorTempe} Kelvin para Celsius é °C {round(KparaC, 2)}")
elif seq == "FK":
    print(f"A conversão de {valorTempe} Fahrenheit para Kelvin é °K {round(FparaK, 2)}")
elif seq == "KF":
    print(f"A conversão de {valorTempe} Kelvin para Fahrenheit é °F {round(KparaF, 2)}")
else:
    print(f"{valorTempe} é uma unidade de medida inválida para conversão de temperaturas! ")
    print("escolha entre F, C ou K (em maiúsculo)")