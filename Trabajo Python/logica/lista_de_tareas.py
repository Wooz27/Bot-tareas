import json
import os
import datetime


def ver_tareas():
    with open("tareas.json", "r") as lista_tareas:
        tareas = json.load(lista_tareas)
        if tareas == []:
            print ("No hay tareas para mostrar")
            return
        else:
            print ("Lista de tareas: ")
        
        #cargar las tareas
        for i, tarea in enumerate(tareas): 
            print(f"""{i + 1}. {tarea['titulo']}:
                  
Descripcion: {tarea['descripcion']}
Fecha Limite: {tarea['fecha_limite']}
Estado: {tarea['estado']}  
    
"""
)
            
if __name__ == "__main__":
    ver_tareas()
    
    
    
    #Esta parte del codigo se podria incluir en el completar tareas, pero lo escribi de forma indidivual para visualizar el proceso de forma separada.

