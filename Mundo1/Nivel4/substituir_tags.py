# CASOS DE TESTE

# texto = 'body'
# numero = '10'
# frase = '<><BODY garbage>body</BODY>'

# texto = 'aBc'
# numero = '923'
# frase = '<dont replacethis>abcabc<abcabcde>'

# texto = 'table'
# numero = '1'
# frase = '<ta>bLe<TaBlewidth=100></table></ta>'

# texto = 'replace'
# numero = '323'
# frase = 'nothing inside'

# texto = 'HI'
# numero = '667'
# frase = '92<HI=/><z==//HIb><cHIhi>'

# texto = 'a'
# numero = '23'
# frase = '<a B c a>'

# texto = 'b'
# numero = '2'
# frase = '<b b abc ab c> Mangojata'


# PROGRAMA

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
    texto = input()
    numero = input()
    frase = input()
    resultado = substituirTag(texto, numero, frase)

    print(resultado)