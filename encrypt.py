#el siguiente algoritmo de encriptacion, por cada caracter elige un numero al azar
#y multiplica su codigo ascii por este, guardando en una estructura dicho resultado y el
#numero usado para calcular el producto. Luego, para decodificarlo, habra que tomar
#el resultado de la multiplicacion y dividirlo, para despues codificar el ascii obtenido.

import random
import csv
import sys

def search(nick):
    ruta = "C:\\Users\\maxip\\Desktop\\Informatica\\SEM-Python\\trabajo_integrador\\file_users.csv"
    file = open(ruta,'r')

    csvreader = csv.reader(file)

    decoded_pass = []
    for user in csvreader:
        if user[0] == nick:
            decoded_pass = user[1]
            break
    file.close()

    return decoded_pass

def decoded(cifrado):
    
    clave = ''
    for elemento in cifrado:
        cant = int(elemento[0])
        res = int(elemento[1:cant+1])
        div = int(elemento[cant+1:])
        clave += chr(int(res/div))

    return clave


def cifrar(caracter):
    num = random.randint(1,25)
    token = str(ord(caracter)*num)
    cifrado = str(len(token)) + token + str(num)
    
    return cifrado


def encrypting(password):
    lista_cifrada = list(map(cifrar, password))

    return lista_cifrada


if __name__ == '__main__':
    password = input('Ingrese su contraseña: ')

    lista_cifrada = encrypting(password)
    print(f"La contraseña cifrada es: {lista_cifrada}")
    print(f"El peso de esta variable es {sys.getsizeof(lista_cifrada)}")

    print('-'*60)
    clave = decoded(lista_cifrada)
    print(f"La contraseña es: {clave}")