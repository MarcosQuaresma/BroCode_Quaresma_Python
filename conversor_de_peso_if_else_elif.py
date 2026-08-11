# Conversor de peso em Python
# Para descobrir o peso em quilos, você divide o valor em libras por 2,2046 (ou multiplica por 0,4536).

peso = float(input("Digite o peso: "))
unidade = input("O seu peso esta em Libras(lbs) ou Kilogramas(Kg)? (lbs ou Kg):")

if unidade == "Kg":
    convert = peso * 0.4536
    print(f"{peso} Kg em Libras é de: {round(convert, 2)} lbs!")
elif unidade == "lbs":
    convert = peso / 2.2046
    print(f"{peso} lbs em Kilogramas é de: {round(convert, 2)} Kg!")
else:
    print(f"{unidade} não é válido! escolha entre (lbs ou Kg)")