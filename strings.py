#Strings 

#string normal
x= "hola mi bro"


#String multilinea

a="""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(a)

#Los trings son arreglo de caracteres unicodigo 
#Python no usa char o strings especificos de tamano 1 

a="Hello World"

print(a[0])
print(a[1])
print(a[6])


#Recorriendo un string 

for x in "banana":
    print(x)


#Largo de un string 

print(len(a))


#Con 

"""
    CHECK IN

"""

#Podemos verificar que algo este en un string 

txt = "The best things in life are free!"
print("free"in txt)
if "free" in txt:
  print("Yes, 'free' is present.")

print  

txt = "The best things in life are free!"
print("expensive" not in txt)
if("expensive"not in txt):
    print("nop esta")
    
    
    
#Se pueden recortar los strings usando 

    """
    Slicing 
    """
    
print("\n")
b="Hellouda world"
print(b[2:6])

#Podemos cortar desde el principio

print(b[:8])


#Podemos cortar desde el final


print(b[5:])



#Indices negativos 

#se peude usar los indices negativos para manipular el string 

print(b[-5:-2])






"""Modificar Strings """
#Se pueden modificar los strings de distitas formas 

#MAYUSCULAS

print(a)
print(a.upper())


#minusculas

print(a)
print(a.lower())



#Remover los espacios en blanco 
a = "     Hello world amigos mios       "

print(a)
print(a.strip())


#Remplazar caracteres del strings por otro en el string 

a = "Hello, World!"
print(a.replace("H", "J"))

#podemos semarar el string en partes para ser convertidos en 
#una lista de substring 0

a="Hello, worlds"
print(a.split(","))

#Podemos concatenar strings para juntarlos 

a = "Hola"
b = "amiko"
c= a+"  " +b

print(c)

#en stri g no se pueden conbinar con otros tipos de datos 
"""
age = 63
txt = " hola yo tengo : " +age
print(txt)

"""

#Esto da error 





#Para combinar ocupamos los:
    
"""

    Fstring 
    
    usamos los place holders {}
    
"""


age = 63
txt = f" hola yo tengo : {age}" 
print(txt)


