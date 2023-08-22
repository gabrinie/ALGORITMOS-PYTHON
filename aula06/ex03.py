#exercicio 3
#Dados dois números inteiros m e n, qual é o primeiro múltiplo de m maior que n? Por exemplo, para m=17 e n=50, o primeiro múltiplo de 17 após 50 é 51.

m = int(input("Informe M \n"))
n = int(input("Informe N \n"))

resto = n%m
m = m - resto
n = n+m;

print("O próximo multiplo é {}".format(n))
2