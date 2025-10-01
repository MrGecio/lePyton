
#VARIABLes
'''
En pyhton no existen comandos para declarar varbles como en otros lenguajes de programcaion

Osease no hacemos int x, o bool y
Solo esrbimos el nombre de la variable y la igualamos 

var = 2

EJem
'''

x = 5
y = "Jorge"

print(x)
print(y)

# Las varible pueden cambiar de type en el proipio codigo al declarlas 

u=4
u="Pepe"
print(u)

#CASTING
'''

Para especificar el tipo de dato de la varible se puede utilizar casting 

'''

x=str(5)
y=int(5)
z= float(5)

print(x,y,z)



#GET the TYPE

'''
Puedo obtener el tipo de la varibele con la funcion type()

'''

x=5
y="John"

print(type(x))
print(type(y))


'''
Aclarar que 

x = "John"

es igual 

x= 'John'


'''

# CASE SENSITIVE

'''

En python las variable son case sensitives 
osease que importa si las escribo en mayusculas o en minusculas


'''

a=4
A="Sally"

print(a)
print(A)

#No se sobreescribe el tipo de valor ni el valor son dos variables completament edistititas 


#Nombres de las varibles 

'''

Las variablen en python pueden tener nombres tanto de un solo caracter como de una palabra 

Reglas para nombrar las variables en python:

    Las varibles siempre deben de empezar con una letra o o _ 
    Los nombres de las varibles no deben empezar con un numero 
    Sus nombres solo pueden contener A-z 0-9 y _
    Recordar que son case sensitives age, AGE, y Age son tres varibles distintas 
    el nombre de una variable no debbe estar entre las pythin keywords


'''


#Many values to multiple values 

'''

python permite asignar valores a multiples variables en una linea 


'''

x, y, z = "orange", "banana", 5
print(x)
print(y)
print(z)


#One values to multple varibles 

x=y=z = "orange"

print(x)
print(y)
print(z)

#Unpack a Collection

'''

Si tienes una coleccion de valores en una list, tuple, etc 
Pyhton te permite desempacar los valores a una variable 

'''

print("\n Espaciaol")
fruits =["apple", "banana", " caca"]
x, y, z = fruits


print(x)
print(y)
print(z)


#Se le pueden asignar el mismo valor a multiples varibales 

x = y = z = "Orange"
print("\n"+x)
print(y)
print(z)

#Podemos guardar cadenas de caracteres '
x = "\nPython is awesome"
print(x)

x ="Python"
y="is"
z="awesome"
print(x,y,z)

# o

print(x+y+z)



#Variables Globales

x = "awesome :) "

def myfunc():
    print("Python is " + x)
    
myfunc()


#Variables locales 

x = "awesome :( "

def myfunc2():
    x="fantastico"
    print("Python is " + x)
    
myfunc2()

print("Piton es "+ x)   




#Para que las variables creadas dentro de funciones se lean 
#De de forma global se debe usar    global


def myfunc3():
    global x
    x="xd"
    
myfunc3()
print("\nPython es "+x)