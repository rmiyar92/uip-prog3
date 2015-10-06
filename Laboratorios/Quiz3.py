#Inicio 

Minutos = 60 
Minr = 0
Ser = 0
SF = 0 
co = 0

while co < 5:

	segundos = int (input ("Ingrese Segundos: "))
	if segundos > Minutos:
		Minr = segundos // Minutos
		Ser = segundos % Minutos
		SF = Minutos - Ser

	print("Los segundos faltantes son:"+str(SF))

	if segundos < Minutos:
		SF = Minutos - segundos
		print("Los segundos faltantes son:"+str(SF))
	co += 1;
