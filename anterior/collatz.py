# Autor: Hugo Araya Carrasco
# Fecha: 07/08/2024
# Version: 0.0
import matplotlib.pyplot as plt

def collatz(numero):
    lista_col = []
    lista_col.append(numero)
    while numero != 1:
        if numero%2 == 0:
            numero = numero // 2
        else:
            numero = 3*numero + 1
        lista_col.append(numero)
    return lista_col

def es_primo(numero):
    resultado = True
    inicio = 2
    fin = numero -1
    while inicio <= fin:
        if numero%inicio == 0:
            resultado = False
        inicio = inicio + 1
    return resultado

def lista_primos(lista_col):
    primos = []
    for num in lista_col:
        if es_primo(num) == True:
            primos.append(num)
    return primos

def graficar(lista_col, primos):
    total = len(lista_col)
    primo = len(primos)
    todos = "Total ("+str(total)+")"
    solos = "Primos ("+str(primo)+")"
    valores = [primo, total]
    etiquetas = [solos, todos]
    separacion = [0.2, 0]
    colores = ['Blue', 'r']
    plt.pie(valores, labels = etiquetas, explode = separacion, shadow = True, colors = colores)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    numero = int(input('Numero: '))
    lista_col = collatz(numero)
    numero_primo = es_primo(numero)
    primos = lista_primos(lista_col)
    graficar(lista_col, primos)


