import random

class Penguin:
    """
    Representa un pingüino en el algoritmo de optimización de búsqueda de rutas. 
    Cada pingüino sigue una ruta en el grafo hasta alcanzar el destino y evalúa su distancia total.

    Atributos:
    graph (Graph): Grafo que representa las zonas y las conexiones entre ellas.
    start (int): Nodo de inicio en el grafo.
    end (int): Nodo de destino en el grafo.
    path (list): Lista de nodos que representan el camino recorrido por el pingüino.
    total_distance (float): Distancia total recorrida por el pingüino.
    """

    def __init__(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.path = [start]
        self.total_distance = 0
        
    def move(self):
        """
        Mueve el pingüino a un nodo vecino aleatorio y actualiza la distancia total.

        Si no hay vecinos disponibles, el movimiento se detiene.
        """
        current_node = self.path[-1]
        neighbors = list(self.graph.neighbors(current_node))
        
        if not neighbors:
            return
        
        next_node = random.choice(neighbors)
        distance = self.graph[current_node][next_node]['weight']
        self.path.append(next_node)
        self.total_distance += distance

    def evaluate(self):
        """
        Evalúa la distancia total recorrida por el pingüino.

        Retorna:
        float: La distancia total recorrida por el pingüino.
        """
        return self.total_distance
    
    def reset(self):
        """
        Reinicia el pingüino a su estado inicial, listo para una nueva búsqueda.
        """
        self.path = [self.start]
        self.total_distance = 0

def penguin_search_optimization(graph, start, end, num_penguins=100, max_iterations=1000):
    """
    Optimización de búsqueda de rutas utilizando el algoritmo de búsqueda de pingüinos.

    Parámetros:
    graph (Graph): Grafo que representa las zonas y las conexiones entre ellas.
    start (int): Nodo de inicio en el grafo.
    end (int): Nodo de destino en el grafo.
    num_penguins (int): Número de pingüinos en la población de búsqueda. Valor predeterminado es 30.
    max_iterations (int): Número máximo de iteraciones de búsqueda. Valor predeterminado es 100.

    Retorna:
    tuple: Una tupla con dos elementos:
        - best_path (list): El mejor camino encontrado.
        - best_distance (float): La distancia total del mejor camino.
    """
    best_path = None
    best_distance = float('inf')

    penguins = [Penguin(graph, start, end) for _ in range(num_penguins)]

    for iteration in range(max_iterations):
        for penguin in penguins:
            penguin.reset()

            while penguin.path[-1] != end:
                penguin.move()

            distance = penguin.evaluate()

            if distance < best_distance:
                best_distance = distance
                best_path = penguin.path

    return best_path, best_distance
