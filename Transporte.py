def verifyIntInput(str):
    while True:
        try:
            n = int(input(f'{str}'))
            return n
        except:
            print("Escribir un numero")

def getValores(origenes, destinos):
    valores = [[0 for x in range(origenes)] for y in range(destinos)]
    for x in range(origenes):
        for y in range(destinos):
            valores[x][y] = verifyIntInput(f'Introducir el costo del origen {x} con el destino {y}: ')
    return valores

def getOferta(num):
    oferta = []
    for x in range(num):
        aux = verifyIntInput(f'Introducir la cantidad de drones disponibles en el origen {x}:')
        oferta.append(aux)
    return oferta

def getDemandas(num):
    demanda = []
    for x in range(num):
        aux = verifyIntInput(f'Introducir la cantidad de drones necesitados del destino {x}:')
        demanda.append(aux)
    return demanda


def getDestinos():
    while True:
        aux = verifyIntInput("Introducir el numero de destinos del dron: ")
        if (aux > 1):
            break
        print('escribir un numero igual o mayor a dos')
    return aux


def getOrigenes():
    while True:
        aux = verifyIntInput("Introducir el numero de origenes del dron: ")
        if (aux > 1):
            break
        print('escribir un numero igual o mayor a dos')
    return aux


def imprimirValores(origenes, destinos, valores, oferta, demanda):
    for x in range(destinos + 2):
        for y in range(origenes + 2):
            #   Primer renglon, imprime origenes
            if(x == 0):
                #   primera columna, imprime el espacio vacio
                if(y == 0):
                    print('', end="\t")
                #   ultima columna, imprime la cantidad
                elif (y == origenes + 1):
                    print('  Oferta')
                #   cualquier columna menos la ultima, imprime el valor
                else:
                    print(f'  Destino {y}', end="\t")
            #   Ultimo renglon, imprime demanda
            elif(x == (origenes + 1)):
                if(y == 0):
                    print('Demanda  ', end=" ")
                elif(y == origenes + 1):
                    print('\n')
                else:
                    print(f'  {demanda[y-1]}\t', end="\t")
            #   Renglones de valores
            else:
                if(y == 0):
                    print(f'Origen {x}', end=" ")
                elif(y == destinos + 1):
                    print(f'  {oferta[x-1]}', end="\n")
                else:
                    print(f'  {valores[x-1][y-1]}\t', end="\t")


def esquinaNoroeste(origenes, destinos, valores, oferta, demanda):
    res = []
    val = []
    x = 0
    y = 0
    while (x < origenes and y < destinos):
        nor = valores[x][y]
        if(oferta[x] > demanda[y]):
            #La oferta es mayor que la demanda en este caso
            oferta[x] = oferta[x] - demanda[y]
            res.append(valores[x][y])
            val.append(demanda[y])
            #Se sigue a la siguiente columna
            y += 1
            
        elif(oferta[x] < demanda[y]):
            #La demanda es mayor que la oferta en este caso
            demanda[y] = demanda[y] - oferta[x]
            res.append(valores[x][y])
            val.append(oferta[x])
            #Se sigue a la siguiente columna
            x += 1


        elif(oferta[x] == demanda[y]):
            #La demanda y la oferta son iguales
            res.append(valores[x][y]) #Se guarda el valor de esta esquina
            val.append(oferta[x])#Se guarda el valor de oferta demanda usado
            #Se sigue con la siguiente columna e hilera
            x += 1
            y += 1

    res.extend(val)
    return res

def imprimirResultados(res):
    y = int(len(res)/2)
    mitad = y
    n = 0
    print(f'El resultado es:\n')
    for x in range(y):
        if(x == 0):
            print(f'z = ({res[x]} * {res[y]}) ', end="")
            n += res[x] * res[y]
        elif(x == mitad - 1):
            y += 1
            n += res[x] * res[y]
            print(f'+ ({res[x]} * {res[y]}) = {n}', end='\n')
        else:
            y += 1
            print(f'+ ({res[x]} * {res[y]}) ', end='')
            n += res[x] * res[y]

def main():
    print('============================================================')
    print('                 ORIGENES Y DESTINOS\n')
    origenes = getOrigenes()
    destinos = getDestinos()
    print('============================================================')
    print('             COSTOS TOTALES DEL TRANSPORTE\n')
    valores = getValores(origenes, destinos)
    print('============================================================')
    print('             NUMERO DE DRONES DISPONIBLES\n')
    oferta = getOferta(origenes)
    print('============================================================')
    print('             NUMERO DE ENTREGAS POR HACER\n')
    demanda = getDemandas(destinos)
    print('============================================================')
    print('                  TABLA ORGANIZADA\n')
    imprimirValores(origenes, destinos, valores, oferta, demanda)
    print('============================================================')
    res = esquinaNoroeste(origenes, destinos, valores, oferta, demanda)
    print('                   RESULTADO\n')
    imprimirResultados(res)
    print('============================================================')

if __name__ == "__main__":
    main()
