# Public-Transport-Route-Optimizer

Aquí puedes ver cómo funciona el optimizador de rutas de transporte para Metro para encontrar la ruta más corta entre estaciones tanto considerando las distancias entre ellas en metros como sin tenerlas en cuenta.

## Introducción

El algoritmo de Dijkstra es una técnica eficiente para encontrar las rutas más cortas desde un nodo origen a todos los demás nodos en un grafo con pesos no negativos.

## Cómo ejecutar la aplicación
Para ejecutar la aplicación sigue los siguientes pasos:

	1.	Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.
	2.	Clona este repositorio o descarga los archivos fuente en tu máquina local.
	3.	Abre una terminal y navega hasta el directorio donde has descargado los archivos.
	4.	Ejecuta el siguiente comando:
```console
python public_transport_route_optimizer.py
```

## Cómo ejecutar los tests
Para ejecutar los tests de la aplicación sigue los siguientes pasos:

	1.	Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.
	2.	Clona este repositorio o descarga los archivos fuente en tu máquina local.
	3.	Abre una terminal y navega hasta el directorio donde has descargado los archivos.
	4.	Ejecuta el siguiente comando:
```console
python -m unittest
```

## Implementación del algoritmo con distancias

### Descripción

En esta variante, se considera la distancia en metros entre estaciones como el peso de las aristas en el grafo. El objetivo es encontrar la ruta que minimiza la distancia total.

### Pasos del Algoritmo

1. Inicializar la distancia al nodo origen como 0 y a todos los demás nodos como infinito.
2. Establecer todos los nodos como no visitados. Crear un conjunto de nodos no visitados.
3. Para el nodo actual, considerar todos sus vecinos no visitados y calcular sus distancias. Comparar la nueva distancia calculada con la distancia actual asignada y asignar el menor.
4. Una vez considerado todos los vecinos del nodo actual, marcarlo como visitado. Un nodo visitado no será revisado nuevamente.
5. Si el nodo destino ha sido marcado como visitado o si la menor distancia entre los nodos no visitados es infinito, el algoritmo ha terminado.
6. Seleccionar el nodo no visitado con la menor distancia y establecerlo como el nuevo nodo actual, luego volver al paso 3.

## Implementación del algoritmo sin distancias

### Descripción

En esta variante, se ignoran las distancias entre las estaciones

### Pasos del Algoritmo

1. Utilizar el mismo algoritmo, pero en lugar de considerar la distancia física entre estaciones, asignar un peso de 1 a cada arista.
2. Los demás pasos son idénticos a la implementación con distancias.