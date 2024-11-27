import networkx as nx
from geopy.distance import geodesic

def build_graph(zones):
    """
    Construye un grafo a partir de las zonas proporcionadas, donde cada nodo representa una 
    zona y las aristas representan conexiones entre zonas que están a una distancia menor a un umbral especificado.

    Parámetros:
    zones (DataFrame): DataFrame que contiene la información de las zonas, incluyendo las coordenadas geográficas (latitud y longitud).

    Retorna:
    G (Graph): Grafo con nodos representando las zonas y aristas con pesos  basados en las distancias geográficas entre ellas.
    """
    G = nx.Graph()

    for idx, row in zones.iterrows():
        G.add_node(idx, pos=(row['Longitude'], row['Latitude']), zone=row['Zone'])

    threshold_distance = 6.5

    for i, loc1 in zones.iterrows():
        for j, loc2 in zones.iterrows():
            if i != j:
                loc1_coords = (loc1['Latitude'], loc1['Longitude'])
                loc2_coords = (loc2['Latitude'], loc2['Longitude'])
                distance = geodesic(loc1_coords, loc2_coords).kilometers
                if distance < threshold_distance:
                    G.add_edge(i, j, weight=distance)

    return G
