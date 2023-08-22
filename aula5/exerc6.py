#Exercicio 6
#Dados um inteiro, qual o seu quadrado e seu cubo? Por exemplo, se o número for 3, a resposta deve ser 9 e 27.

num = int(input("Informe um número \n"))
quad = num ** 2
cubo = num ** 3

print("O cubo de {} é {} e o quadrado de {} é {}.\n".format(num, cubo, num, quad))
