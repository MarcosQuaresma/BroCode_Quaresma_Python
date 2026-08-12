# Operadores Lógicos = Usa-se em Condicionais e Declarações

#                   and = checa se duas ou mais Condições são Verdadeiras (True)
#                    or = checa se a Última condição é Verdadeira (True)
#                   not = Verdadeira se a condição for falsa, e, vice e versa

temp = 15
ensolarado = False #boolean pode ser usado como no exemplo.

if temp <= 0 or temp >= 30:
    print("O tempo esta bom hoje!")
# elif temp <=14:
    print ("talves o tempo esteja ficando frio, mas ainda esta bom!")
else:
    print("O tempo não esta bom hoje!")

#if ensolarado:
#    print("O tempo esta ensolarado hoje!")
if not ensolarado:
    print("O dia esta nublado.")
else:
    print("O dia esta ensolarado!")