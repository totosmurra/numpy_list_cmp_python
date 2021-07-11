# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Empecemos a jugar con las listas y su métodos, el objetivo
es realizar el código lo más simple, ordenado y limpio posible,
no utilizar bucles donde no haga falta, no "re inventar" una función
que ya dispongamos de Python. El objetivo es:

1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
    que estén comprendidos entre 1 y 10 inclusive
    (NOTA: utilizar comprension de listas tal como se hizo en clase)
2) Luego de generar la lista sumar los números y ver si el resultado
    de la suma es menor o igual a 21
    a) Si el número es menor o igual a 21 se imprime en pantalla
        la suma y los números recoletados
    b) Si el número es mayor a 21 se debe informar al usuario que perdio
'''
import random as rd
if __name__ == '__main__':
    print('Comenzamos a divertirnos!')
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    nums_aleatorios = [rd.randrange(1,11) for i in range(0,3)]
    
    if sum(nums_aleatorios) <= 21:
        print("Ganaste, tus numeros son",nums_aleatorios)
    else:
        print("Perdiste")

    print("terminamos")