numTestes = eval(input())
listaFinal = []
for rep in range(numTestes):
    numLista = eval(input())
    lista = list(input().split(' '))
    intLista = sorted(list(map(lambda n: int(n), lista[:numLista])))
    um = False
    for num in intLista:
        if num == 1:
            um = True
    if not um:
        listaFinal.append(1)
    else:
        minimo = 1
        for num in intLista:
            if num > minimo:
                break
            minimo += num
        listaFinal.append(minimo)

for numero in listaFinal:
    print(numero)
