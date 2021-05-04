from os import system
import random
import time
from tittle import *
from draw import *

#TRAER ALEATORIAMENTE UNA PALABRA DEL ARCHIVO DATA.txt
def word_random():
    make_list = []
    my_list = []
    
    #Añado todas las palabras de la base de datos DATA.txt con renombre 'f'...
    #... hacia una LISTA llama makelist.
    with open("./DATA.txt", "r", encoding="utf-8") as f:
        for words in f:
            make_list.append(str(words)) 
    #Selecciono aleatoriamente una palabra de la LISTA creada.
    random_word = random.choice(make_list) 
    
    #Convierto la palabra seleccionada en una LISTA llamada mylist para poder trabajar
    for i in range(len(random_word) - 1):
        my_list.append(random_word[i])
    
    #Retorno la lista
    return(my_list)
    
def run():
    #Convierto Lista "my_list" en Diccionario con funcion ENUMERATE     
    my_dict = dict(enumerate(word_random(), start=1))
    
    #BORRAR ESTO AL FINALIZAR, SOLO ES PARA VIZUALIZAR LA PALABRA
    # for value in my_dict.values():
    #     print(value, end='')
    # print("\n")
    #print()


    #Creo un diccionario cuyos VALUES sean: "_" (guiones bajos)...
    # ...cuya longitud o numero de KEYS sean las del diccionario random 
    mi_dict_vacio = {i: "_" for i in range(1, len(my_dict)+1)}  #USE UN COMPREHENSION PARA GENERAR UNA LISTA VACIA

    #Imprimo el diccionario vacío, que en realidad está lleno con "_"
    for filas in range(17):
        print()

    for value in mi_dict_vacio.values():
        print(value, end='')
    print("\n")
    
#BUCLES
    contador = 0
    while 1:
        
        #Creo un bucle que genera los ciclos hasta hallar la palabra correcta ...
        #... hasta que el contador sea igual a la longitud de la palabra aleatoria.
        c2 = 0
        while contador != len(my_dict):
            
                       
            # Pido letra a jugador y creo un control para detectar palabras repetidas
            r = 0      
            cont_r = 0
            
            while r !=1:
                #Pido letra
                letra = input("Ingresa una letra: ")
                system("clear")
                for repe in mi_dict_vacio.values():
                    if repe == letra:               
                        cont_r = cont_r + 1
                    
                #Control de letra repetida
                if cont_r >= 1:
                    cont_r = 0
                    ejecutar(c2)
                    print("Ouch! Letra Repetida")
                    
                    ##Imprimir diccionario vacío con cada letra válida
                    for value in mi_dict_vacio.values():
                        print(value, end='')
                    print("\n")
                else:
                    r = 1           
            
            
            # Ingreso de letras válidas al diccionario vacio
            a = 0
            
            for key, value in my_dict.items():                
                if value == letra:
                    mi_dict_vacio[key] = value
                    a+=1
                    contador += 1   #Para terminar acaba con todo el bucle                   
                else:
                    pass
            #Control de letra incorrecta
            if a>0 and a<=2:
                ejecutar(c2)
                print("Ok!")
                
            else:
                if c2<10:
                    c2 = c2 +1
                    print("el contafor es : ", c2)
                    ejecutar(c2)#BORRAR SYSTEM CLEAR
                    print("Bad! ")
                else:
                    contador = len(my_dict)
                                    
                

            #Imprimir diccionario vacío con cada letra válida
            for value in mi_dict_vacio.values():
                print(value, end='')
            print("\n")
            

        print("Lo lograste!")
        time.sleep(1)
        break   
        
        
        
if __name__ == "__main__":
    system("clear")
    while 1:
        system("clear")
        run()
        #Para seguir jugando
        system("clear")
        print("Desea seguir jugando?")
        enter = input("presione la letra 'y' para continuar: ")
        if enter == "y":
            continue
        else:
            print("By Richard Sailema")
            break
    
