#Dada uma sequência de duplas de números, representando valores e seus respectivos pesos, seguida por uma dupla de zeros, qual a média ponderada desconsiderando a dupla de zeros?

value, weight = input().split()
total_weighted_sum = 0
total_weights = 0

while value != "0" and weight != "0":
    value, weight = int(value), int(weight)
    total_weighted_sum += value * weight
    total_weights += weight
    value, weight = input().split()

if total_weights == 0:
    print("Não há valores para calcular a média ponderada.")
else:
    weighted_average = total_weighted_sum / total_weights
    print(f"A média ponderada é: {weighted_average}")
