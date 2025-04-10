import os 
import datetime
import json

def crear_tarea():
    #Obtener datos de la tarea
    titulo = input("ingrese el nombre de la tarea: ")
    descripcion = input ("ingrese la descripcion de la tarea: ")
    fecha_limite = input("ingresa la fecha limite de la tarea (Año-Mes-Dia): ")
    estado = ("pendiente")
    
    #Crear un diccionario para modificar
    tarea = {
        "titulo": titulo,
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "estado": estado,
    }
    
    #Crear el json si no existe
    if not os.path.exists ("tareas.json"):
        with open ("tareas.json", "w") as lista_tareas:
            json.dump([], lista_tareas)
    
    #Confirmar si existen mas tareas
    with open ("tareas.json", "r") as lista_tareas:
        tareas = json.load(lista_tareas)
        #Cargar nuevo tarea a la lista
        tareas.append(tarea,)

    
    #Guarda los datos en un json
    with open("tareas.json", "w") as lista_tareas:
        json.dump(tareas, lista_tareas, indent = 2)
        
        
    print("Tarea creada con exito")
    #Imprimir la tarea creada
    print(f"Tarea: {titulo}")
    
    
if __name__ =="__main__":
    crear_tarea()

    