MIND  = 1440  #Cantidad de minutos  equivalentes para un dia
MINH  = 0     # Variable que almacena  minutos equivalentes para horas 
DIAS = 0      # Variable que almacena los dias 
HORAS = 0     # Variable que almacena las horas  
MINR = 0      # Variavle que almacena los minutos restantes 

MIN = int (input ("Ingrese los minutos: "))

if MIN >= MIND:
	DIAS = MIN // MIND
	MINH = MIN %  MIND
	HORAS = MINH  // 60 
	MINR  = MINH  % 60

if  MIN < MIND:
	MINH = MIN // 60
	HORAS = MINH  // 60
	MINR  = MIN  % 60


print("La cantidad de minutos que ingreso es igual  a "+str(DIAS)+"  dias y "+str(MINH)+" horas  con "+str(MINR)+"  minutos")
