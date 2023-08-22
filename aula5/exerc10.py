#Exercicio10
#Dadas quatro notas de um estudante, qual sua média aritmética?

n1 = float(input("Informe a nota 1 \n"))
n2 = float(input("Informe a nota 2 \n"))
n3 = float(input("Informe a nota 3 \n"))
n4 = float(input("Informe a nota 4 \n"))
           
media = (n1+n2+n3+n4)/4

print("Sua média é {:.2f}".format(media))