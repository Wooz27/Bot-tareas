import json
import os
import datetime
from logica.lista_de_tareas import ver_tareas
from logica.crear_tarea import crear_tarea
from logica.completar_tareas import completar_tareas
from logica.borrar_tareas import eliminar_tareas
from logica.modificar_tareas import alterar_tareas

while True:
    print ("Bienvenido al bot de tareas")
    print ("1.Crear una tarea")
    print ("2.Ver tareas")
    print ("3.Completar tareas")
    print ("4.Eliminar tareas")
    print ("5.modificar tareas")
    print ("6.Salir")
    
    opcion = int(input("Seleccione una opcion: "))
    
    if opcion == 1:
        crear_tarea()
    elif opcion == 2:
        ver_tareas()
    elif opcion == 3:
        completar_tareas()
    elif opcion == 4:
        eliminar_tareas()
    elif opcion == 5:
        alterar_tareas()
    elif opcion == 6:
        print ("Gracias por usar el bot")
        break
    else:
        print ("Opcion no valida, por favor seleccione una opcion valida")
        
    input("Presione enter para continuar...")
        
    print ("---------------------------------")
    print ("Volviendo al menu principal")
    print ("---------------------------------")