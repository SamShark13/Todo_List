import os
# Crear una lista vacía para almacenar las tareas
tareas = []
#Obtener fecha y hora
import datetime
#Declaracion de Funciones
def nueva_tarea():
    nombre_tarea = input('Ingrese el nombre de la tarea: ')
    fecha_limite = input('Ingrese la fecha límite (formato DD-MM-YYYY): ')
    prioridad = input("Ingrese la prioridad (Alta / Media/ Baja): ")
    tarea = {"nombre": nombre_tarea, "fecha_limite": fecha_limite, "prioridad": prioridad,  "terminada": False}
    tareas.append(tarea)
    print("Tarea agregada exitosamente.")
def tareas_pendientes():
    print("\nLista de tareas:")
    tareas_pendientes = False  # Variable de bandera para verificar si hay tareas pendientes
    
    for tarea in tareas:
        if tarea["terminada"]:
            print("[X]", tarea["nombre"],' | Fecha limite:', tarea["fecha_limite"],'| Prioridad:' ,tarea["prioridad"])
        else:
            print("[ ]", tarea["nombre"],' | Fecha limite:', tarea["fecha_limite"],'| Prioridad:' ,tarea["prioridad"])
            tareas_pendientes = True  # Actualizamos la bandera si hay tareas pendientes

    if not tareas_pendientes:  # Si no hay tareas pendientes, mostramos el mensaje
        print("\n(No hay tareas pendientes)")
def eliminar_tarea():
    tarea_borrar = input("Ingrese el nombre de la tarea a borrar: ")
    global tareas
    tareas = [tarea for tarea in tareas if tarea["nombre"] != tarea_borrar]
    print("Tarea eliminada exitosamente.")
def marcar_tarea_terminada():
    nombre_tarea=input('Ingrese el nombre de la tarea terminada: ')
    global tareas
    for tarea in tareas:
        if tarea["nombre"] == nombre_tarea:
            tarea["terminada"] = True
            print(f"Tarea '{nombre_tarea}' marcada como terminada.")
            return
    print(f"Tarea '{nombre_tarea}' no encontrada en la lista de tareas.")
while True:
    tiempo_actual = datetime.datetime.now()
    dia = tiempo_actual.day
    mes = tiempo_actual.month
    año = tiempo_actual.year
    hora = tiempo_actual.hour
    minutos = tiempo_actual.minute

    print('\t  To-Do List')
    print('  Fecha: '+ str(dia) + '-'+str(mes) + '-'+ str(año) +' | Hora: '+ str(hora) + ':' + str(minutos))
    tareas_pendientes()
    print('\n   Opciones:')
    print('1. Subir Nueva Tarea')
    print('2. Marcar Tarea Completada')
    print('3. Borrar Tarea')
    print('4. Salir')
    opcion = int(input('Ingrese su opcion: '))
    if opcion == 1:
        nueva_tarea()
        os.system('cls')
    elif opcion == 2:
        marcar_tarea_terminada()
        os.system('cls')
    elif opcion == 3:
        eliminar_tarea()
        os.system('cls')
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print('Opcion no disponible')