def imprimir(imprimir):
    if imprimir:
        for frases in imprimir[2:-1].split('\\r\\n'):
            print(frases)
    else:
        print("Comando retornou vazio !!!")

def entrada():
    return input("Escreva <<< ")