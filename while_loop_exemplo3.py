
num = int(input("Digite um número entre 1 a 10: "))

# while num < 1 or num > 10:
#   print(f"{num} não é válido")
#   num = int(input("Digite um número entre 1 a 10: "))
# print(f"Seu número {num} é válido! ")

while num < 1:
    print("Entre 1 a 10")
    num = int(input("Digite um número entre 1 a 10: "))
    if num >10:
        print("Entre 1 a 10")
        num = int(input("Digite um número entre 1 a 10: "))
else:
    print(f"Boa recutra!! pague {num} flexões diamante com punho cerrado! \n -----FACA NA CAVEIRA!-----")