
#Importamos pandas para hacer uso de la hoja csv
import pandas as pd 
#Libreria para usar colas de prioridad más facilmente
import heapq 

#Leemos la hoja de datos del metro y guardamos sus datos en BaseDatos
BaseDatos = pd.read_csv('C:\\Users\\Belen\\Desktop\\proyecto metro\\Metro.csv')

#En la hoja tenemos columnas llamadas Nodo1 y Nodo2 que son practicamente las estaciones y tambien tenemos las 
#distancias entre ellas todo lo guardamos como si fuera un grafo aunque tecnicamente solo son arreglos 
Nodo1 = BaseDatos["Nodo1"]
Nodo2 = BaseDatos["Nodo2"]
aristas = BaseDatos["Longitud"]

#Creamos una varible que guardara todos estos datos como arreglos de arreglos la creamos desde ya para poder usar
#el metodo append(); tambien agregamos un contador para llevar un orden al meter los datos en el arreglo
nodoNodoArista = []
contador = 0

#Ciclo for para introducir los datos en el arreglo
for estacion in Nodo1:
    #Cada estacion en el arreglo se ordena como vienen en el archivo csv es decir así: (Pantitlán,Zaragoza,1320)
    #ademas se transforma la distancia a un entero por si acaso
    nodoNodoArista.append((Nodo1[contador], Nodo2[contador], int(aristas[contador])))
    #El contador recorre cada elemento del nodo1
    contador += 1

#Pedimos las estaciones inicial y final
estacionInicial = input("Desde que estacion salimos?")
estacionFinal = input("Que estacion es nuestro destino?")

    
#Construimos el grafo que representara al metro entero, este se compondra de un diccionario tipo así: 
#{Lindavista: {Instituto del Petroleo: 1258, Deportivo 18 de Marzo: 1075}}
metro = {}

#Este for se encargara de recorrer todos los elementos(estaciones) que conformaran el grafo (metro), sus conexiones y sus distancias
for estacion1, estacion2, distancia in nodoNodoArista:

    #Se revisa si las estaciones no se encuentran ya en el metro en caso de que no esten en el metro, entonces se agregan al 
    #grafo, como claves de diccionario que a su vez guardan otro diccionario dentro de ellas en el que iran las estaciones
    #vecinas y sus distancias, se toman en cuenta ambas estaciones para agregar porque el metro es bidireccional
    if estacion1 not in metro:
        metro[estacion1] = {}
    if estacion2 not in metro:
        metro[estacion2] = {}

    #Despues de crear las estaciones o que ya esten creadas, se procede a llenar el diccionario de segundo nivel con la estacion2
    #y su distancia de la estacion1, se hace a la inversa tambien porque el metro es bidireccional
    metro[estacion1][estacion2] = distancia
    metro[estacion2][estacion1] = distancia

#Se crea un diccionario que mantendra las distancias que existan desde el nodo de inicio a los nodos del camino
#se llena con cada estacion del metro estableciendo la distancia hacia ellas en infinito para que no haya errores
#al engañar al algoritmo con ceros
distancias = {estacion: float('inf') for estacion in metro}

#La distancia al nodo de inicio dentro del diccionario se establece como cero pues ahí es donde comenzamos
distancias[estacionInicial] = 0

#Este diccionario se encargara de guarda el camino, o mejor dicho las estaciones anteriores a otras, como si fuera una lista enlazada
#donde cada estacion(clave o nodo) hace referencia a su estacion anterior
estacionAnterior = {}

#Declaramos un conjunto de datos que contendra a las estaciones que ya hayamos visitado, el conjunto es mejor que un arreglo
visitados = set()

#Declaramos el arreglo que tendra a nuestros nodos ordenados por distancia al nodo de inicio, como primer par en aparecer 
#estan la estacion de inicio con su distancia a la estacion de inicio así recoremos ordenadamente los caminos dependiendo
#de su distancia al nodo inicial
colaDePrioridad = [(0, estacionInicial)]

#Este while se encargara de recorrer la cola de prioridad, la cola de prioridad trabaja como una lista de los nodos y sus 
#distancias al nodo de inicio, al iterar sobre ella nos aseguramos de repasar todos los nodos del grafo
while colaDePrioridad:

    #Asignamos a las variables de distanciaActual y estacionActual el primer elemento de la cola de prioridad, es decir, 
    #el nodo con la distancia minima al nodo de inicio
    distanciaActual, estacionActual = heapq.heappop(colaDePrioridad)

    #Revisamos que la estacion no este en visitados, si ya fue visitado el nodo entonces nos saltamos al siguiente elemento
    #de la cola de prioridad, es decir, omitimos el codigo que sigue dentro del while en esta iteracion
    if estacionActual in visitados:
        continue

    #La estacion se agrega a las estaciones visitadas
    visitados.add(estacionActual)

    #Este for se encargara de recorrer todas las estaciones vecinas de la estacion actual dentro del grafo (metro)
    for estacionVecina, distanciaVecina in metro[estacionActual].items():

        #Calculamos la distancia a la estacion vecina más la distancia que teniamos a la estacion actual
        distanciaNueva = distanciaActual + distanciaVecina

        #Comprobamos si la distancia calculada al nodo vecino es más corta
        if distanciaNueva < distancias[estacionVecina]:

            #Si la distancia es más corta actualizamos la distancia en el arreglo
            distancias[estacionVecina] = distanciaNueva
            
            #Asignmos a la clave de la estacion vecina la estacion actual
            estacionAnterior[estacionVecina] = estacionActual

            #Se introduce a la cola de prioridad la distancia nueva junto con la estacion vecina nueva
            heapq.heappush(colaDePrioridad, (distanciaNueva, estacionVecina))

            #Hay que tomar en cuenta que esta parte de codigo solo se hace si la distancia es menor, 
            #ignoramos todas aquellas situaciones en las que la distancia resultante es mayor

# Reconstruir el camino más corto entre el nodo de inicio y final, se agrega al arreglo el nodo final
camino = [estacionFinal]

#Este while se encarga de agregar las estaciones anteriores al camino a partir de la estacion final hasta que alcance
#la estacion inicial
while camino[-1] != estacionInicial:
    
    #Se agrega al camino la estacion anterior que guardamos en nuestro diccionario de estaciones anteriores y así se continua
    #hasta que se ha agregado la estacion inicial
    camino.append(estacionAnterior[camino[-1]])

#La funcion reversa invierte el arreglo para no confundirnos
camino.reverse()

#Imprimimos los reultados
print("Distancia mínima:", distancias[estacionFinal])
print("Camino mínimo:", camino)
