#Exercicio 09
#Dada a data e o número de dias decorridos, qual é a nova data?

dia = int(input("Informe o dia \n"))
mes = int(input("Informe o mes \n"))
ano = int(input("Informe o a111no \n"))
decorridos = int(input("Informe os dias decorridos"))

j =(1461*(ano+4800+(mes-14)//12))//4+(367*(mes-2-12*((mes-14)//12)))//12-(3*((ano+4900+(mes-14)//12)//100))//4+dia-32075

j = j + decorridos

f = j+1401+(4*j+274277)//146097*3//4+(-38)
e = 4*f+3 
g = e%1461//4
h = 5*g+2
d = h%153//5+1
m = (h//153+2)%12+1
y = e//1461-4716+(12+2-m)//12



print("A nova data é {}/{}/{}".format(d,m,y))