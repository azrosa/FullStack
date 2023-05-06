import re

def padraoTag(tag):
    padrao = r"^(<[a-zA-Z0-9=\/ ]{0,50}>)$"
    return bool(re.match(padrao, tag))
def substituirTag(tag):
    global texto
    global numero
    # ctag = tag[1:len(tag)-1]
    ctag = tag
    if texto.casefold() in tag.casefold():
        t = texto.casefold()
        # ctag.replace(t,numero)
        count = ctag.casefold().count(t)
        for i in range(count):
            itag = ctag.casefold().find(t)
            aux = ctag[:itag] + numero
            ctag = aux + ctag[itag+len(t):]
    # ctag =f'<{ctag}>'
    return ctag

def substituirTexto():
    global texto
    global numero
    global frase
    cfrase = frase
    resultado = ''
    tag = ''
    iniTag = frase.find('<')
    fimTag = frase.find('>')
    count = 0
    if iniTag == -1:
        resultado = frase
    count = 0
    while True:
        if iniTag < fimTag:
            resultado = resultado + cfrase[:iniTag]
            tag = cfrase[iniTag:fimTag+1]
            if padraoTag(tag):
                ctag = substituirTag(tag)
                resultado = resultado + ctag
                cfrase = cfrase[fimTag+1:]
                iniTag = cfrase.find('<')
                fimTag = cfrase.find('>')
                if iniTag == fimTag == -1:
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
    texto = input()
    numero = input()
    frase = input()
    resultado = substituirTexto()
    print(resultado)