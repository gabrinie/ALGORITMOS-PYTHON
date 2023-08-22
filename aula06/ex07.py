#Exercicio 07 
#Dado um dia juliano, qual é o dia da semana?

j = int(input("Informe o dia juliano\n"))

dia = (j+1)%7


match dia:
    case 0:
        print("Domingo")
    
    case 1:
        print("Segunda-feita")
    
    case 2:
        print("Terça-Feira")
    
    case 3:
        print("Quarta-feira")
        
    case 4:
        print("Quinta-feira")

    case 5: 
        print("Sexta-feira")
    
    case 6: 
        print("Sábado")
        
