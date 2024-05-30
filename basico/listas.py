#Python desde cero... Otra vez. 

### LISTS ###
#No es lo mismo una lista que un arreglo. 
#Una lista es una colección ordenada y mutable de elementos. 
my_list=list()

#Solo corchetes es una lista.
my_other_list=[]

print(len(my_list))

my_list=[34,43,23,43,56,57]
print(my_list)
print(len(my_list))

my_other_list=[22, 1.98, "neith","altair"]
#Saber el tipo de dato. 
print(type(my_other_list))
print(len(my_other_list))

#Imprimir una posición específica de la lista. 
# las listas se pueden utilizar como una manera de evitar crear varias variabeles con diferentes valores. 
print(my_other_list[0])

#Igualar la lista con variables, innecesario ???
age, altura, nombre, apodo = my_other_list
print(nombre)

#Se pueden combinar ambas listas para que queden en una sola. 
print(my_list+my_other_list)

#Lo agrega en la última posición.
my_other_list.append("neithaltair")
print(my_other_list)

#Se puede agregar en una posición específica con el insert. 
my_other_list.insert(4, "puestoNuevo")
print(my_other_list)

#eliminar contenido de las listas
my_other_list.remove("neithaltair")
print(my_other_list)

#Se pueden eliminar posiciones específicas, sel pop es el que permite quedarse con el elemento o con la posición que se va a eliminar. 
print("Imprime el elemento de la lista que se elimina == ",my_list.pop())
print("Muestra el contenido de la lista con el elemento ya eliminado == ",my_list)

#se puede asignar el valor del elemento eliminadoa a una variable para no perderlo.
remove_element = my_list.pop(2)
print(remove_element)
print(my_list)

#Para eliminar el elemento sin la necesidad de verlo como con le pop. 
del my_list[2]
print(my_list)

#Se puede copiar el contenido de una lista en otra lista
my_new_list = my_list.copy()
#Limpiar el contenido de la lista.
my_list.clear()
print(my_list)
print(my_new_list)

#Con el parametro de reverse, se puede invertir el orden de la lista..
my_new_list.reverse()
print(my_new_list) 

#Sort para ordenar la lista, cuando es una lista, si es entero queda de menor a mayor, pero se le pueden agregar más parámetros. 
my_new_list.sort()
print(my_new_list)

#Remove quita por el valor que se encuentra en la lista. 
#DEL se encarga de eliminar por indice, por posición. 
#No se pueden establecer constantes en python. 