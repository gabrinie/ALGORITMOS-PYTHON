#Exercicio 6 
#dado um dia juliano, qual é a data correspondente?

j = int(input("Informe o dia juliano"))



f = j+1401+(4*j+274277)//146097*3//4+(-38)
e = 4*f+3 
g = e%1461//4
h = 5*g+2
d = h%153//5+1
m = (h//153+2)%12+1
y = e//1461-4716+(12+2-m)//12

print("Hoje é dia {}/{}/{}".format(d,m,y))

 

