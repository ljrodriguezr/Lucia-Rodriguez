
matriz = [
    [10, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
]

no_fila =0
busqueda = int(input("ingrese el valor de busqueda"))

for fila in matriz:
    no_columna = 0
    for columna in fila:
        if (columna == busqueda):
            print(f" No. {busqueda} , posision es: [{no_fila}][{no_columna}]")
no_columna += 1
no_fila += 1

