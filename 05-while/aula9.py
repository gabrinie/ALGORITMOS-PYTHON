# while
num = int(input("digite um numero natural: "))
n= 1 

triangular = n* (n+1)*(n+2)

while triangular <num:
    n+= 1 
    triangular = n* (n+1) + (n+2)
    
if triangular == num: 
    print(f"{num} é triangular")
    print(f"{n}*{n+1}*{n+2} = {num} ")
else:
    print(f"{num} Não é triangular")
    