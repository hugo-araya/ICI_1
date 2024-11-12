

def inicializa():
    return [1,2,3,4,5,6,7,8,9]

def calcula_pivote(ini, fin):
    piv = (fin + ini)//2
    return piv

def busqueda(lista, elemento):
    ini = 0
    fin = len(lista)-1
    ok = False
    while ini <= fin and ok == False:
        piv = calcula_pivote(ini, fin)
        if lista[piv] == elemento or lista[ini] == elemento:
            ok = True
        else:
            if elemento < lista[piv]:
                fin = piv - 1
            else:
                ini = piv + 1
    return ok

if __name__ == '__main__':
    lista = inicializa()
    elemento = 5
    ok = busqueda(lista, elemento)
    if ok == True:
        print('Encontrado')
    else:
        print('No existe')


