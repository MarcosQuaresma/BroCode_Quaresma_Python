# Como usar o "Input"
nome = input ("Digite sue nome: ")
idade = int(input("Digite sua idade: "))
# a título de concatenação, para realizar operações matemáticas de uma variável que foi interpretada como "srt" é
# necessário que convertemos ela em um úmero inteiro, vejamos:
# se eu quero transformar a soma da minha idade +1, primeiro eu terei que transfromalo em um numero inteiro, segue ex:
# ex errado:
# idade = idade + 1 ~~(nesse exemplo irá dar erro de sintax, pois o dado recebido no:
# idade = input("Digite sua idade: "), seria interpretado com uma "str" não como um "int"
# para isso é nescessário que façamos uma conversão:
# -> idade = int(idade)
# -> idade = idade + 1
# Maas se da pra fazer em uma linha só de cídigo, iremos fazer lá em cima.
idadesoma = idade + 1

print (f"Olá {nome}!")
print (f"Sua idade é de {idade} anos!")
print (f"Sua idade + 12 meses de diferença é de {idadesoma} anos!")

# com base no que foi passado, seguiremos pra o exercício executado no arquivo: exercicio_Mad_Libs.py