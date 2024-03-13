bandas = []

#construyendo la interfaz
print("***ALTAVOZ ES TU VOZ***")
print("***********************")

opcion=100 
while (opcion != 5):
    print("1.Registrar Banda")
    print("2.Buscar información de una Banda")
    print("3.Listar agenda del evento")
    print("4.Modificar una Banda")
    print("5.Salir")
   
    opcion = int(input("Digita una opción: "))

    if opcion == 1:
        banda={}
        #Creando los datos del diccionario
        banda["id"] = int(input("Digita el id: "))
        banda["nombre"] = input("Nombre de la banda: ")
        banda["genero"] = input( "Genero :")
        banda["clasificacion"] = input("Clasificación: ")
        banda["tiempo"] = int(input("Tiempo: "))
        banda["costo"] = int(input("Costo: $"))
        
        #Agregando un diccionario a una lista
        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandaAuxiliar  in bandas:
            if bandaAuxiliar["nombre"].lower()==bandaBuscada.lower():
                print(f"id: {bandaAuxiliar['id']} --- nombre:{bandaAuxiliar["nombre"]}")
            else:
                print("Siga buscando")
    elif opcion == 3:
        print(bandas)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        pass