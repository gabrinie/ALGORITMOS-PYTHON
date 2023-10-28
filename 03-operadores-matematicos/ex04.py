#4
#Dado um número inteiro representando um tempo em segundos, qual é o tempo em horas, minutos e segundos?
# 1h = 3600segundos ou 60 minutos / 1 minuto = 60 segundos 

segundos = int(input("Informe os segundos \n"))

horas = segundos // 3600
resto = horas%3600
minutos = resto // 60
segundos = segundos%60

print("{} horas {} minutos {} segundos".format(horas, minutos, segundos))



