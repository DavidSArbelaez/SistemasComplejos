from data_loader import load_data
from graph_builder import build_graph
from penguin_search import penguin_search_optimization
from map_plotter import plot_map_with_best_path
import os

def main():
    """
    Carga los datos de viajes y zonas, construye un grafo de las zonas, 
    ejecuta el algoritmo de optimización de búsqueda PeSOA, 
    y guarda el mapa con la mejor ruta encontrada.
    """
    trip_data_path = 'data/2023_For_Hire_Vehicles_Trip_Data_20241021 (1).csv'
    zone_data_path = 'data/codes.xlsx'

    trips, zones = load_data(trip_data_path, zone_data_path)

    graph = build_graph(zones)

    start_location = 203
    end_location = 105

    best_path, best_distance = penguin_search_optimization(graph, start_location, end_location)

    m = plot_map_with_best_path(graph, best_path, zones)
    output_dir = 'Results'
    output_path = os.path.join(output_dir, 'best_route_map.html')
    m.save(output_path)
    print(f"Mejor ruta: {best_path}")
    print(f"Distancia total: {best_distance} km")

if __name__ == "__main__":
    main()
