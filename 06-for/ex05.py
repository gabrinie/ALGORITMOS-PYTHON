#Dado um natural, quais seus divisores? Por exemplo, os divisores de 90 são 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90.

n = int(input())
for i in range(1,n):
    if (n % i == 0):
        print(i)