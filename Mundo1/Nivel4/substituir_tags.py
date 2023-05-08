import re

def padraoTag(tag):
    padrao = r"^(<[a-zA-Z0-9=\/ ]{0,50}>)$"
    return bool(re.match(padrao, tag))

def substituirTag(texto, numero, tag):
    # ctag = tag[1:len(tag)-1]
    ctag = tag
    if texto.casefold() in tag.casefold():
        t = texto.casefold()
        count = ctag.casefold().count(t)
        for i in range(count):
            itag = ctag.casefold().find(t)
            aux = ctag[:itag] + numero
            ctag = aux + ctag[itag+len(t):]
    # ctag =f'<{ctag}>'
    return ctag

def substituirTexto(texto, numero, frase):
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
                ctag = substituirTag(texto, numero, tag)
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

def main():
    while True:
        try:
            texto = input()
            numero = input()
            frase = input()

            resultado = substituirTexto(texto, numero, frase)
            print(resultado)

        except EOFError:
            break

if __name__ == '__main__':
    main()