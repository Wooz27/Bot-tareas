import json
import os 
from logica.lista_de_tareas import ver_tareas

def completar_tareas():
    
    # leer las tareas del json
    with open("tareas.json", "r") as lista_tareas:
        tareas = json.load(lista_tareas)
        
        #visualizar tareas con la funcion de forma directa
        if tareas == []:
            print ("No hay tareas para completar")
            return
        else:
            ver_tareas()
            tarea_completada = int(input("Que tarea deseas completar? (Ingrese el numero de la tarea): "))
    
        # completar la tarea seleccionada
        for i in range(len(tareas)):
            if tarea_completada == i + 1:
                tareas[tarea_completada - 1]["estado"] = "completado"
                print(f"La tarea '{tareas[tarea_completada - 1]['titulo']}' ha sido marcada como completada.")
                break
            
            elif tarea_completada == ["completado"]:
                print ("Esta tarea ya ha sido completada")
                break
        else:
            print ("Este numero no corresponde a ninguna tarea")
 
        # guardar los cambios en el json
        with open("tareas.json", "w") as lista_tareas:
            json.dump(tareas, lista_tareas, indent=2)

        
        
if __name__ == "__main__":
    completar_tareas()
                