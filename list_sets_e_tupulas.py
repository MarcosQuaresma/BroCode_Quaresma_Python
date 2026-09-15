# Coleções = uma "unica" variável usada pra armazenar vários valores
# List  = [] ordenável e mutável. Duplicatas ATIVADAS
# Set   = {} não ordenável e imutável, mas Addiciona/Remove OK. Duplicatas DESATIVADAS
# Tuple = () ordenado e imutável. Duplicatas ATIVADAS. MAIS RÁPIDO


## list [] = Listas

# listafruta = ["maçã", "banana", "uva", "pera", "laranja", "coco"]

# print(frutas[::-1]) # para por a lista de trás pra frente basta por o indice em ":: -1"]

# for x in listafruta:
#     print(x) # novamente: o X é a variável executável dentro do "for x in y"
# for fruta in listafruta:
#     print(lista) #nesse caso fica bem mais cláro a execução.

# print(help(fruta)) # o "help()" devolve todos os médotos e atribuições disponíveis para essa variável.
# print(len(fruta)) # a função "len()" tem como objetivo, quantificar os itens dentro dessa lista.
# print("uva" in fruta) # o operador "in" ele serve pra verificar se há um ítem nessa lsita.

# listafruta[3] = "abacaxi" # eu posso tanto usar o indice [x] pra mostrar o que há nele no "print()" como eu também
                            # posso invoca-lo para alterar a lista, como eu fiz agora.
# listafruta.append("amora") #usei esse metodo ".append()" para adicionar ao final da lista um item.
# listafruta.remove("laranja") #usei o metodo ".remove()" para remover um ítem da lissta.

# listafruta.insert(0, "carambola") # aqui percebemos que o metodo ".insert(indice, "")" insere um ítem no indice chamado
                                  # não subistituindo o indice já existente, ele soma a lista.
# listafruta.sort() # coloca a lista em ordem alfabetica
# listafruta.reverse() #coloca a lista ao contrário
# listafruta.clear() #limpa todos os ítens dessa lista.

# print(listafruta.index("uva")) # ",index("str")" mostra em qual indice o item invocado esta na lista.
# print(listafruta.count("maçã")) # ".count("str")" mostra a quantidade que esse item aparece na lista.

# obs: ------------------------------ list [] = pode conter duplicatas ------------------------------
#                                    são ordenados e podem ser alterados
#                                    -----------------------------------

## Sets {} = Conjuntos

listafruta = {"maçã", "banana", "uva", "pera", "laranja", "coco"}
# em Conjuntos {}, não podemos alterar os itens atravez de indexação, mas podemos remove-los ou adicionarmos um item


# listafruta.add("ameixa") #como eu havia dito, em conjuntos, não podemos modificar os ítem, mas também quando
# adicionamos ele entra na lista de maneira aleatória.

# listafruta.remove("uva") # o .remove("str") ele remove precisamente o item do conjunto.
# listafruta.pop() #o .pop remove um ítem aleatório do teu conjunto.

# listafruta.clear() # limpa sue conjunto, devolutiva : set()

# vejamos, se no conjunto original eu adicionar 2x o mesmo item ou mais, ela irá preservar somente 1 item ex:
# se no conjunto: listafruta = {"maçã", "banana", "uva", "pera", "laranja", "coco"} adicionarmos + 3 uvas
# o conjunto automaticamente preservará o conjunto mantendo os mesmos itens.

# listafruta = {"maçã", "banana", "uva", "pera", "laranja", "coco", "uva", "uva"} # o conjunto irá preservar somente 1 uva
#                                                                               mesmo que tenha mais itens repetidos
#                                                                               ele irá retornar sem duplicidade.

# obs: ------------------------------ set {} = conjuntos não podem ser alterados ------------------------------
#                                      mas contém duplicatas, porém não ativas
#                                          pode remover e adicionar itens
#                                        -----------------------------------

## Tuple () = tupulas
# em Tuplas () mesmo conceito de List [], só que mais rápido.
# em Tupulas não tantos métodos, somente ".count()" e ".index()"

listafruta = ("maçã", "banana", "uva", "pera", "laranja", "coco",)

# print(listafruta.index("laranja"))
# print(listafruta.count("laranja"))



print(listafruta)