import folium as folium

def plot_map_with_best_path(graph, best_path, zone_data):
    """
    Genera un mapa interactivo utilizando Folium que muestra las zonas y la mejor ruta 
    entre las ubicaciones especificadas en el camino óptimo.

    Parámetros:
    graph (Graph): Grafo con nodos representando zonas y aristas representando distancias entre ellas.
    best_path (list): Lista de índices representando la secuencia óptima de zonas en la ruta.
    zone_data (DataFrame): DataFrame que contiene la información geográfica de las zonas, 
                            incluyendo latitud y longitud.

    Retorna:
    folium.Map: Mapa interactivo con los nodos de las zonas y la mejor ruta trazada entre ellas.
    """
    locations = {idx: (row['Latitude'], row['Longitude']) for idx, row in zone_data.iterrows()}
    
    map_center = [40.7128, -74.0060]
    m = folium.Map(location=map_center, zoom_start=12)

    for idx, (lat, lon) in locations.items():
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.7,
            popup=f'Zona: {idx}'
        ).add_to(m)

    for i in range(len(best_path)-1):
        start_idx = best_path[i]
        end_idx = best_path[i+1]
        
        start_coords = locations[start_idx]
        end_coords = locations[end_idx]
        
        folium.PolyLine(
            locations=[start_coords, end_coords],
            color='red',
            weight=3,
            opacity=1
        ).add_to(m)

    return m
