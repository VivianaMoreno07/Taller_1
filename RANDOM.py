
#Programa para generar un numero aleatorio en python
import random


a=input('limite inferior:')
b=input('limite superior:')

a=int(a)
b=int(b)
respuesta=random.randint(a,b)
print(respuesta)