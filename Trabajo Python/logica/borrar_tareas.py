import os
import json
from logica.lista_de_tareas import ver_tareas

def eliminar_tareas ():
    # Cargar tareas
    with open ("tareas.json", "r") as lista_tareas:
        tareas = json.load(lista_tareas)
        
        #ver tareas
    ver_tareas()
    if not tareas:
        print ("No hay tareas para eliminar")
        return
         
    #Respuesta del usario
    respuesta = int(input ("Que tarea deseas eliminar? (Ingrese el numero de la tarea): "))
    
    #Eliminar la tarea seleccionada
    for i in range(len(tareas)):
        if respuesta == i + 1:
            del tareas[respuesta - 1]
            print(f"La tarea {respuesta} ha sido eliminada.")
            break
        else: 
            print ("Ese numero no corresponde a ninguna tarea")
            break
    #guardar los cambios en el json
    with open ("tareas.json", "w") as  lista_tareas:
        json.dump(tareas, lista_tareas, indent =2 )

if __name__ == "__main__":
    eliminar_tareas()