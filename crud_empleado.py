import os
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)

def menu_gral():
    os.system("cls")
    print("1. Crear empleado")
    print("2. Actualizar Empleado")
    print("3. Eliminar Empleado")
    print("4. Listar Empleado")
    print("5. Salir ")

def seleccionar_opcion(max_opcion):

    opcion = 0
    while True:
        try:
            opcion = int(input("Seleccione una opcion >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opcion invalida, intente nuevamente >> ")
        else:
            return opcion
        

def iniciar_programa():   
    while True: 
        menu_gral()
        opcion = seleccionar_opcion(5)

        if opcion ==1:
            print("Crear empleado")
        elif opcion ==2:
            print("Actualizar empleado")
        elif opcion ==3:
            print("Eliminar empleado")
        elif opcion ==4:
            print("Listar empleado")
        elif opcion == 5:
            print("Salir")

        input()

        empleados = cargar_json('empleados.json')

        print(empleados)


iniciar_programa()