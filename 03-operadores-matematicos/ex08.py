#exercicio 08
#Dada uma data, qual é o dia da semana correspondente?

dia = int(input("Informe o dia \n"))
mes = int(input("Informe o mes \n"))
ano = int(input("Informe o a111no \n"))


j =(1461*(ano+4800+(mes-14)//12))//4+(367*(mes-2-12*((mes-14)//12)))//12-(3*((ano+4900+(mes-14)//12)//100))//4+dia-32075

semana = (j+1)%7

match semana:
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
        
