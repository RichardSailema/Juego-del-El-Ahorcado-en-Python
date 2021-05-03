   
# mi_dict = {"1": "m", "2": "o", "3": "m", "4": "i", "5": "c", "6": "a"}

# for value in mi_dict.values():
#    print(value, end='')
# print("\n")

# #CREO UN DICCIONARIO LLENO CON "_" guiones bajos, de longitud del diccionario random 
# mi_dict_vacio = {i: "_" for i in range(1, len(mi_dict)+1)}  #USE UN COMPREHENSION PARA GENERAR UNA LISTA VACIA

# #IMPRIMO EN EL MISMO ESPACIO SOLO LOS "VALUES" DEL DICCIONARIO "_________"
# for value in mi_dict_vacio.values():
#    print(value, end='')
# print("\n")

# #PIDO UNA LETRA Y LA COMPARO CON EL DICCIONARI RANDOM HACIENDO 6 CILCOS (DEBIDO A LON DE MI_DICT) POR CADA LETRA
# #SI LA LETRA ES IGUAL A UNA LETRA DEL DICCIONARIO (mi_dict) comienzo a llenar el diccionario vacio (q en realidad no es vacío sino lleno con  "_")
# contador = 0
# while 1:
#    while contador != len(mi_dict):
      
#       r = 0      
#       cont_r = 0
#       while r !=1:
#          letra = input("Ingresa una letra: ")
         
#          for repe in mi_dict_vacio.values():
#             if repe == letra:               
#                cont_r = cont_r + 1
#          if cont_r >= 1:
#             cont_r = 0
#             print("Letra Repetida")
#          else:
#             r = 1


            

         


#       for key, value in mi_dict.items():
#          if value == letra:

#             mi_dict_vacio[int(key)] = value
#             contador += 1
#          else:
#             pass
      
            
   
      
#       for value in mi_dict_vacio.values():
#          print(value, end='')
#       print("\n")
#    print("Lo lograste!")
#    break

#*****************************************

# anchura = int(input("Anchura de la línea: "))
# altura = int(input("Altura de la línea: "))
# numero = int(input("Número de rectángulos"))


# for d in range(numero):
#    for l in range(anchura):
#       print("*",end="")
#    print(" ", end="")
# print()

# for h in range(altura-2):
#    for n in range(numero):
#       print("*",end="")
#       for a in range(anchura-2):
#          print(" ", end="")
#       print("*", end="")
#       print(" ", end="")
#    print()

# for d in range(numero):
#    for l in range(anchura):
#       print("*",end="")
#    print(" ", end="")
# print()

anchura = int(input("Anchura de la línea: "))
altura = int(input("Altura de la línea: "))
grosor = int(input("Número de rectángulos: "))

for i in range(grosor):
   for j in range(anchura):
      print("* ", end="")
   print()

for i in range(altura - 2 * grosor):
   for j in range(grosor):
      print("* ", end="")
   print()

for i in range(grosor):
   for j in range(anchura):
      print("* ", end="")
   print()

      




