# Primer Parcial Practico
# Iram Abbud 33150

# ----- FUNCION QUICKSORT -----
# Funcion para Quick Sort
def QuickSort(lista,l,r):
    
    # Si la lista tiene solo 1 elemento, la regresa sin hacer calculos
    if len(lista) == 1:
        return lista
    
    # Si el valor del indice es igual o mayor al numero maximo de elementos en la lista, la funcion acaba
    if l >= r:
        return
    
    # Se crean las particiones de la lista
    m = Partition(lista,l,r)
    
    # Se vuelve a utilizar la funcion de Quick Sort, con las particiones respectivas
    QuickSort(lista,l,m)
    QuickSort(lista,m+1,r)
# Funcion para el orden de las particiones
def Partition(lista,l,r):
    
    # valor del pivote
    pivote = lista[l]
    
    # indice que indica que valor se utiliza para cambiar
    j = l
    
    for i in range(l+1, r):
        
        if lista[i] <= pivote:
            
            # incrementar el indice
            j = j + 1
            lista[j], lista[i] = lista[i], lista[j]
    
    lista[l], lista[j] = lista[j], lista[l]

    return j

# ----- FUNCION DE BINARY SEARCH -----
# Funcion para Binary Search
def BinarySearch(arr, target):
    # Variables para poder buscar el numero pedido que determinar los límites de arreglo a buscar
    min = 0
    max = len(arr) - 1

    # Funcion while para buscar el numero utilizando min y max
    # Se realiza un ciclo sin parada hasta que los min>=max, por lo tanto no se encontro o se llega al número buscado
    while True:

        # Creamos una variable con la posicion media del arreglo que es nuestro intento actual
        guess = (min + max) // 2

        # Si esta posicion resulta tener el numero buscado termina el programa
        if arr[guess] == target:
            break
        # Si el numero en la posicion de nuestro intento es menor que el numero
        # buscado se suma 1 al rango minimo y se intenta otra vez
        elif arr[guess] < target:
            min = guess + 1
        # Si el numero de nuestro intento es mayor, se resta 1 al rango
        # maximo y se intenta otra vez
        else:
            max = guess - 1
        # Si el numero no se encuentra y se regresa un "No"
        # como respuesta a la funcion
        if min > max:
            return "No"
    return guess

# ----- FUNCIONES DE DATOS DE LISTA
# Funcion que checa si cualquier numero de una lista es mayor a 10^5
def ResInNumMAX(x):
    for i in x:
        if i > 10**5:
            return False
            break
    return True
# Funcion que checa si cualquier numero de una lista es menor a 1
def ResInNumMIN(x):
    for i in x:
        if i < 1:
            return False
            break
    return True

# ----- CODIGO PREGUNTAR LA LISTA -----
# Funcion while que le pide al usuario el # de elementos y los elementos en el arreglo
# y checa que no rompa las restricciones impuestas del ejercicio
while True:
    n,*datos=map(int,input('Porfavor escriba el # de elementos en su arreglo, seguido por los elementos, todo separado por 1 espacio: ').split())
    # Correr funciones para restricciones de datos individuales en la lista y guardarlos en su variable
    MAX1 = ResInNumMAX(datos)
    MIN1 = ResInNumMIN(datos)
    # Imprimimos un error con su mensaje especifico, dependiendo de la regla que no se siguio
    if len(datos) != n:
        print(f'# de elementos pedidos: {n}, # de elementos ingresados: {len(datos)}')
        print('Cantidad de datos ingresados diferente a # de datos especificados, intente otra vez!')
    elif not 1<=n<=3*10**4:
        print(f'# de elementos segun el ususario: {n}')
        print('La cantidad de datos no esta dentro de los limites (1 - 30 mil), intente otra vez!')
    elif MAX1 == False:
        print(datos)
        print('Uno de los datos de la lista excede el limite de 100 mil, intente otra vez!')
    elif MIN1 == False:
        print(datos)
        print('Uno de los datos de la lista es menor a 1, intente otra vez!')
    # Si todas las reglas fueron cumplidas, seguimos con el codigo
    else:
        break

# Se ordena la lista por quicksort
QuickSort(datos, 0, n)

# ----- CODIGO PARA PEDIR LA BUSQUEDA -----
# Funcion while para realizar el Binary Search
while True:
    # Pedimos el numero que se quiere buscar
    j,*lista2=map(int,input('Porfavor escriba el # de elementos que desea buscar, seguido por los elementos, todo separado por 1 espacio: ').split())
    # Correr funciones para restricciones de datos individuales en la lista y guardarlos en su variable
    MAX2 = ResInNumMAX(lista2)
    MIN2 = ResInNumMIN(lista2)
    # Imprimimos un error con su mensaje especifico, dependiendo de la regla que no se siguio
    if len(lista2) != j:
        print(f'# de elementos: {j}, # de elementos ingresados {len(lista2)}')
        print('Cantidad de datos ingresados diferente a # de datos especificados, intente otra vez!')
    elif MAX2 == False:
        print(lista2)
        print('Uno de los datos que busca excede el limite de 100 mil, intente otra vez!')
    elif MIN2 == False:
        print(lista2)
        print('Uno de los datos que busca es menor a 1, intente otra vez!')
    # Si todas las reglas son cumplidas el programa procede
    else:
        # Se crea una lista para imprimir los resultados de Binary Search
        ListaFinal = []
        # Se implementa Binary Search con un for para poder buscar todos los numeros deseados
        for i in lista2:
            # Convertimos en una variable el lugar de la lista a buscar para poder utilizarla con la funcion BinarySearch
            BuscaBusca = lista2[i-1]        # AQUI ESTA DANDO EL ERROR INDEX OUT OF RANGE PERO NO ENTIENDO POR QUE SI i-1 DEBERIA FUNCIONAR
                                            # SOLO FUNCIONA CUANDO HAY 1 NUMERO EN LA LISTA ORIGINAL
            
            # Guardamos el resultado de la busqueda en una variable para utilizar en la siguiente parte del codigo
            buscar = BinarySearch(datos, BuscaBusca)

            # Si BinarySearch no encuentra el numero agrega un -1 a una lista
            if buscar == "No":
                ListaFinal.append(-1)

            # Si encuentra el numero agrega el valor del indice del numero a una lsita
            else:
                ListaFinal.append(i-1)
        break

# Se imprimen las 2 lineas finales 
print(datos)
print(ListaFinal)
