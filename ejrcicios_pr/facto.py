import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":

    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1100)
    numero = int(input("Numero: "))
    numero_f = factorial(numero)
    print (numero_f)
    print(sys.getrecursionlimit())
