import pandas as pd
import heapq


class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_arista(self, ciudad1, ciudad2, distancia, tiempo):
        if ciudad1 not in self.vertices:
            self.vertices[ciudad1] = []
        if ciudad2 not in self.vertices:
            self.vertices[ciudad2] = []

        self.vertices[ciudad1].append((ciudad2, distancia, tiempo))
        self.vertices[ciudad2].append((ciudad1, distancia, tiempo))

    def dijkstra(self, inicio, fin, parametro):
        heap = [(0, inicio, [])]
        visitados = set()

        while heap:
            (costo, actual, camino) = heapq.heappop(heap)

            if actual not in visitados:
                visitados.add(actual)
                camino = camino + [actual]

                if actual == fin:
                    return (costo, camino)

                for vecino, distancia, tiempo in self.vertices[actual]:
                    if parametro == "distancia":
                        heapq.heappush(heap, (costo + distancia, vecino, camino))
                    elif parametro == "tiempo":
                        heapq.heappush(heap, (costo + tiempo, vecino, camino))

        return (float("inf"), [])


# Funcion para cargar desde excel
def cargar_datos(archivo):
    grafo = Grafo()

    # Lee el archivo Excel y crea un DataFrame
    df = pd.read_excel(archivo)
    print("Columnas disponibles en el DataFrame:")
    print(df.columns)

    # Itera sobre las filas del DataFrame y agrega las aristas al grafo
    for index, row in df.iterrows():
        grafo.agregar_arista(
            row["Nombre Ciudad A"],
            row["Nombre Ciudad B"],
            row["Distancia (km)"],
            row["Tiempo (min)"],
        )

    return grafo


# Programa principal
archivo_excel = "ViasCol.xlsx"
grafo = cargar_datos(archivo_excel)
# Ejemplo de uso
ciudad_a = input("Ingrese el nombre de la Ciudad A: ")
ciudad_b = input("Ingrese el nombre de la Ciudad B: ")

# Determinar si las ciudades están conectadas por una única carretera
if (ciudad_a in grafo.vertices) and (ciudad_b in grafo.vertices):
    conectadas = any(
        ciudad_b == vecino for vecino, _, _ in grafo.vertices[ciudad_a]
    )  # el primer _ representa la distancia y el segundo _ representa el tiempo
    if conectadas:
        print(
            f"Las ciudades {ciudad_a} y {ciudad_b} están conectadas por una carretera."
        )
    else:
        print(f"No hay conexión directa entre {ciudad_a} y {ciudad_b}.")

# Determinar el camino más corto en términos de distancia
distancia, camino_distancia = grafo.dijkstra(ciudad_a, ciudad_b, "distancia")
print(
    f"Camino más corto en distancia: {camino_distancia}, Distancia total: {distancia} km"
)

# Determinar el camino más corto en términos de tiempo
tiempo, camino_tiempo = grafo.dijkstra(ciudad_a, ciudad_b, "tiempo")
print(f"Camino más corto en tiempo: {camino_tiempo}, Tiempo total: {tiempo} minutos")
