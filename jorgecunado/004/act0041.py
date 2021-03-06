import os
import pickle

def cargar_archivo_notas():
	
	if os.path.isfile("notas"):
		with open("notas", "rb") as archivo_notas:
			lista_cartas = pickle.load(archivo_notas)
	else:
		lista_cartas = []	
	
	return lista_cartas


def guardar_archivo_notas(lista_cartas):

	with open("notas", "wb") as archivo_notas:
		pickle.dump(lista_cartas, archivo_notas)
		return True


def cargar_modelos():

	lista_cartas=[["Señor {0}:",
				  "por la presente comunicamosle que en la fecha prescindios de",
				  "susm servicios. Haberes a su disposicion termino legal.",
				  "firmado: {1}"], 
				  ["A: {0}",
				   "De: {1}",
				   "Asunto: Reporte de fletes",
				   "-------------------------",	
				   "{0} :"
				   "Para el proximo viernes necesitamos los reportes de fletes realizados en el mes.",
				   "Recuerden que deberan anexar el del mes anterior que no se realizo el mes pasado.-",
				   "Saludos,  {1}"]]
	return lista_cartas			   


def imprimir_encabezados(titulo):

	os.system("Cls")
	print()
	print(titulo.center(centrado,"-"))
	print()


def menu_principal(lista_opciones):

	imprimir_encabezados(" Correspondencia ")
	for i , opcion  in enumerate(lista_opciones):
		print("--",i+1, " - ", opcion)
	print("")


def escribir_un_texto():

		imprimir_encabezados("Escribir un texto.")
		texto=[]
		condicion = True
		print("""Escriba el modelo de nota. 
			     Use '{0}' para refernciar al destinaario
			     Use '{1}' para el remitente""")
		print(" ")
		while condicion: 
			renglon = input("Lin: ")
			if len(renglon) > 1:
				texto.append(renglon)
			else:
				condicion = False
				return texto


def cargar_destinatarios(lista_destinatarios):				
	
	imprimir_encabezados("Cargar Destinatarios. Termina con cadena vacia")
	print(" ")
	condicion = True
	while condicion:
		destinatario = input("Destinatario : ")
		if len(destinatario) > 0:
			lista_destinatarios.append(destinatario)
		else:
			condicion = False	


def agregar_cartas(lista_cartas):

	txt=escribir_un_texto()
	lista_cartas.append(txt)
	print(lista_cartas)


def mostrar_cartas(lista_cartas):
	
	imprimir_encabezados("Mostrar cartas")
	for i , cartas in enumerate(lista_cartas):
		print("")
		print("Modelo {}".format(i))
		print("---------")
		print("")
		for renglon in range(len(cartas)):
			print(cartas[renglon])
		print("-"*78)
	a=input("Continuar...")		

	
def imprimir_cartas(lista_destinatarios, lista_cartas):
	
	os.system("cls")
	imprimir_encabezados("Imprimir cartas")
	mostrar_cartas(lista_cartas)

	a_imprimir = int(input("Que modelo va a imprimir :"))

	if not 0 <= a_imprimir < len(lista_cartas):
		mostrar_cartas(lista_cartas)

	texto = lista_cartas[a_imprimir]
	remitente = input("Remitente :")
	os.system("cls")
	for destinatario in lista_destinatarios:
		for i in range(len(texto)):
			if "{0}" in texto[i]:
				print(texto[i].format(destinatario, remitente))
			elif "{1}" in texto[i]:	
				print(texto[i].format(destinatario, remitente))
			else:
				print(texto[i])
		print("")		
		print("-"*79)
		a=input("seguir")


lista_opciones =["Agregar carta",
				"Cargar destinatarios",
				"Imprimir una carta",
				"Mostrar cartas",
				"Guardar notas",
				"salir"]
				
centrado=60

def main():
	
	lista_cartas = cargar_archivo_notas()
	if len(lista_cartas) == 0:
		lista_cartas = cargar_modelos()

	lista_destinatarios=[]
	
	siempre = True
	while siempre:
		
		opcion = 0
		while opcion not in (1,2,3,4,5,6):
			menu_principal(lista_opciones)
			opcion = int(input("       Ingrese opción: "))
			print(" ")
		
		if   opcion == 1:
			agregar_cartas(lista_cartas)
		
		elif opcion == 2:
			cargar_destinatarios(lista_destinatarios)
		
		elif opcion == 3:
			imprimir_cartas(lista_destinatarios, lista_cartas)	
		
		elif opcion == 4:
			mostrar_cartas(lista_cartas)
		
		elif opcion == 5:
			guardar_archivo_notas(lista_cartas)
		
		else:
			siempre = False

if __name__ == "__main__":
	main()
