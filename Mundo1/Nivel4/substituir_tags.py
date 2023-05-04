def substituirTag(texto, numero, frase):
    cfrase = frase
    resultado = ''
    tag = ''
    iniTag = frase.find('<')
    fimTag = frase.find('>')
    count = 0
    if iniTag == -1:
        resultado = frase
    while True:
        if iniTag < fimTag:
            resultado = resultado + cfrase[:iniTag]
            tag = cfrase[iniTag:fimTag+1]
            if texto.casefold() in tag.casefold():
                ctag = tag
                t = texto.casefold()
                count = ctag.casefold().count(t)
                for i in range(count):
                    itag = ctag.casefold().find(t)
                    aux = ctag[:itag] + numero
                    ctag = aux + ctag[itag+len(t):]
                resultado = resultado + ctag
                cfrase = cfrase[fimTag+1:]
                iniTag = cfrase.find('<')
                fimTag = cfrase.find('>')
                if iniTag == fimTag:
                    resultado = resultado + cfrase
            else:
                resultado = resultado + tag
                cfrase = cfrase[fimTag+1:]
                iniTag = cfrase.find('<')
                fimTag = cfrase.find('>')
        else:
            break
        count += 1
    return resultado

if __name__ == '__main__':
    listaFinal = []

    while True:
        texto = input()
        if texto == '':
            break
        numero = input()
        frase = input()
        resultado = substituirTag(texto, numero, frase)
        listaFinal.append(resultado)

for linha in listaFinal:
    print(linha)