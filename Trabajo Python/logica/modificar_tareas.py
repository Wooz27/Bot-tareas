import json
import os
from logica.lista_de_tareas import ver_tareas


def alterar_tareas ():
    # Cargar tareas
    with open ("tareas.json", "r") as lista_tareas:
        tareas = json.load(lista_tareas)
        
        
    if tareas == []:
        print ("No hay tareas para modificar")
        return
        
    else:
        ver_tareas()
        respuesta = int(input ("Que tarea deseas modificar? (Ingrese el numero de la tarea): "))
    
    #Modificar la tarea seleccionada 
    for i in range(len(tareas)):
        
        if respuesta == i + 1:
            print(f"Esta seguro de que desea modificar la tarea {respuesta} ? (si/no)")
            confirmacion = input()
            if confirmacion.lower() == "si":
                #Modificar la tarea
                print ("Ingrese el nuevo nombre de la tarea: ")
                nuevo_nombre = input()
                tareas[respuesta - 1]["titulo"] = nuevo_nombre
                print ("Ingrese la nueva descripcion de la tarea: ")
                nueva_descripcion = input()
                tareas[respuesta - 1]["descripcion"] = nueva_descripcion
                print ("Ingrese la nueva fecha de la tarea: ")
                nueva_fecha = input()
                tareas[respuesta - 1]["fecha_limite"] = nueva_fecha
                print ("Ingrese el nuevo estado de la tarea: ")
                nuevo_estado = input("Solo puede ser 'pendiente' o 'completado': ")
                tareas[respuesta - 1]["estado"] = nuevo_estado
                print(f"La tarea {respuesta} ha sido modificada.")
                break
            elif confirmacion.lower() == "no":
                print ("No se realizaron cambios")
                break
            else:
                print ("No se realizaron cambios")
                break
        
    #guardar cambios
    with open("tareas.json","w") as lista_tareas:
        json.dump(tareas, lista_tareas, indent=2)
        

    
if __name__ == "__main__":
    alterar_tareas()
                
