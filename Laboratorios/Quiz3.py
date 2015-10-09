#Inicio 
#Modifique el codico el error estaba en que tenia 2 impresiones que imprimian la misma vairable  por eso imprimia  los 2 resultados del mismo flujo

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

	



	if segundos < Minutos or segundos == Minutos:
		SF = Minutos - segundos
		


	co += 1;
	print("Los segundos faltantes son:"+str(SF))


	#Ejecute escenarios con un  numero mayor a 60  menos a 60  y  numeros negativos
