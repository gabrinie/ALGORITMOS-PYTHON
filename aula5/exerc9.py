#Exercicio 9
#Joãozinho fez sua viagem até os Estados Unidos. Porém, chegando lá, descobriu que a temperatura é medida em graus Fahrenheit, e não em Celsius. Dada a temperatura em graus Fahrenheit, qual a temperatura correspondente em graus Celsius?

far = float(input("Informe a temperatura em graus Fahrenheit"))
celsius = (far-32)*5/9
print("A temperatura em Celsius é {:.2f}".format(celsius))
