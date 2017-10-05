#!/usr/bin/env python3

import random

def alto():
    print('El numero introducido es mayor que el numero buscado')#too high)
    
def bajo():
    print('El numero introducido es menor que el numero buscado')#too low
    
def repetición():
    jugar = input("Te gustaría jugar de nuevo? Y/n\n> ")
    if jugar.lower() == 'y':
        jugar()
    print('Adios')    

def jugar():
    print("Bienvenido, vamos a jugar")    
    x = random.randint(1, 100)
    cont = 0
    numero = None
    
    while cont < 10 and numero != x:    
        while True:
            try:
                numero = int(input("Introduzca un numero: ")) 
                break
            
            except ValueError:
                print("Debe introducir un número entero")
                pass
        
        if numero > x:
            alto()
            cont += 1
            
        elif numero < x:
            bajo()
            cont += 1
    
    if cont >= 10:
        print("Has tardado mucho, el numero era: ", x)
        repetición()                
    else:
        print("Enhorabuena, encontraste el numero")
        repetición()
        
if __name__ == '__main__':
    jugar()
