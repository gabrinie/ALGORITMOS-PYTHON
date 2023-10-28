# Exercicio 5
# Dada uma data, qual é o seu dia juliano?
# FÓRMULA = J=(1461⋅(Y+4800+(M−14)/12))/4+(367⋅(M−2−12⋅((M−14)/12)))/12−(3⋅((Y+4900+(M−14)/12)/100))/4+D−32075

dia = int(input("Informe o dia \n"))
mes = int(input("Informe o mes \n"))
ano = int(input("Informe o ano \n"))



j =(1461*(ano+4800+(mes-14)//12))//4+(367*(mes-2-12*((mes-14)//12)))//12-(3*((ano+4900+(mes-14)//12)//100))//4+dia-32075

print("Estamos no {} dia Juliano".format(j))