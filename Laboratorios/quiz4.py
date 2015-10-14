def  Proceso(nombre = '',quiz1 = 0,quiz2 = 0,quiz3 = 0,quiz4 = 0,quiz5 = 0):
	 nombre = (input("Ingrese el nombre del estudiante: "))
	 quiz1 = int (input("Ingrese la nota del quiz1 :"))
	 quiz2 = int (input("Ingrese la nota del quiz2 :"))
	 quiz3 = int (input("Ingrese la nota del quiz3 :"))
	 quiz4 = int (input("Ingrese la nota del quiz4 :"))
	 quiz5 = int (input("Ingrese la nota del quiz5 :"))
	 PROM = (quiz1+quiz2+quiz3+quiz4+quiz5) / 5
	 print("El pormedio del estudiante es:  "+str(PROM))
	 archivo = open(nombre, "w+")
	 archivo.write(str(quiz1)+","+str(quiz2)+","+str(quiz3)+","+str(quiz4)+","+str(quiz5)+"\n el promedio total es:  "+str(PROM))
	 archivo.close()




CO = 0 
PROM = 0



while  CO < 3:
 Proceso()


 CO +=1
