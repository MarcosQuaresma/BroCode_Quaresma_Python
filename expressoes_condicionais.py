# Expressões condicionais = É um atalho de UMA linha para usar uma instrução "if-else" (Operador-Ternário)
#                           Imprimir (print()) ou atribuir valores com base em uma condição
#                   Fórmula: X if condition else Y
#                    Retorna X se a condição for verdadeira(True), Se não(Else) retorna Y.

num = 5
a = -1
b = 1
idade = 17
temperatura = 20
cargo_funcionario = "convidado"

# print(f"o número {num} é par" if num % 2 == 0 else f"O número {num} impar")
# print("Positivo" if num > 0  else "Negativo")
# maior_num = a if a > b else b
# menor_num = a if a < b else b
# estatus = "Adulto" if idade >= 18 else "Criança"
# agua = "Frio" if temperatura < 20 else "Quente"
nivel_de_acesso = "acesso total" if cargo_funcionario == "admin" else "acesso limitado"

print (nivel_de_acesso)
