#Data  types

"""En pyhton existen varios tipos de datos 

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType


"""


#Para imprimir el tipo de datos de una varibale solo
#tenemos que escrbir type

x=5
print(type(x))

#Si queremos especificar el tipo solo tenmeos que castearlos 

x = range(6)		
x = dict(name="John", age=36)



#Numeros en pyhton 

"""
    Existen tres tipos de numeros 
    
    int 
    float 
    complex
    
"""

#Las variables se crean con el dato que le asignamos 
x=1     #int
y=2.5   #float
z=1j    #complex

print(type(x))
print(type(y))
print(type(z))


#Como dato existen -+ de ambos y del float podemos usar e
#Para describir a la x10

x=35e3
y=12e24
z=-87.5e100


print(type(x))
print(type(y))
print(type(z))



#Complex

#estos muy importante son
"""
    
    NUMEROS Imaginarios
    
    """
#se utiliza una j para detonar la i de imaginario

x= 3+5j
y=5j
z=+5j

print(type(x))
print(type(y))
print(type(z))



print("\n")

#Podemos convertir el tipo de nuestros numeros 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)



#Random 

#se puede usar el random en pyhton 


import random

print(random.randrange(1,10))



#Casteos ejm:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2