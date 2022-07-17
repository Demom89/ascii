#!/bin/python3


data = str(input("Que voy a convertir: ")) 

string = "".join([chr(int(item, 16)) for item in data.split()])

print('\nTu salida es:' + string)
