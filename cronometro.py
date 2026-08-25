# Cronômetro em Python
import time
meu_tempo = int(input("Digite em segundos: "))

while meu_tempo < 0 or meu_tempo > 86400:
    print("Digite um valor entre 0 e 86400 segundos\n-> 86400s é equivalente a 24 horas")
    meu_tempo = int(input("Digite em segundos: "))

for x in range(meu_tempo, 0, -1):# poderia usar o "reverse.range(x)" mas ele irá começar do "0". maneira intuitiva
    segundos = x % 60
    minutos = int(x / 60) % 60
    horas = int(x / 3600) % 24 # o " % 24 " é pra um relógio que conte dias na f"n{x}" o While lá em cima define isso!

    print(f"{horas:02}:{minutos:02}:{segundos:02}") # a formatação permite que os "0's" apareçam dentro do contador "00:00:00"
    time.sleep(1)

print("!TEMPO ESGOTADO!")

## cláro, esse relógio não conta DIAS... ainda!