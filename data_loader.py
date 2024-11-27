import pandas as pd
import numpy as np
from geopy.distance import geodesic

def load_data(trip_data_path, zone_data_path):
    """
    Carga los datos de viajes y zonas desde archivos CSV y Excel, respectivamente. 
    Procesa las fechas de los viajes, calcula la duración de los viajes y 
    agrega información geográfica y de zona a los datos de viajes.

    Parámetros:
    trip_data_path (str): Ruta al archivo CSV con los datos de los viajes.
    zone_data_path (str): Ruta al archivo Excel con la información de las zonas.

    Retorna:
    tuple: Una tupla que contiene dos elementos:
        - trips (DataFrame): DataFrame con los datos de los viajes procesados.
        - zones (DataFrame): DataFrame con la información de las zonas.
    """
    try:
        trips = pd.read_csv(trip_data_path)
        zones = pd.read_excel(zone_data_path).set_index('LocationID')
    except Exception as e:
        raise FileNotFoundError(f"Error al cargar los datos: {e}")

    for col in ['pickup_datetime', 'dropOff_datetime']:
        trips[col] = pd.to_datetime(
            trips[col], format='%m/%d/%Y %I:%M:%S %p', errors='coerce'
        )

    trips['trip_duration'] = (
        trips['dropOff_datetime'] - trips['pickup_datetime']
    ).dt.total_seconds()

    trips = trips.dropna(subset=['PUlocationID', 'DOlocationID', 'trip_duration'])
    trips = trips.reset_index(drop=True)

    trips = trips.merge(
        zones.rename(columns={
            'Borough': 'PU_Borough',
            'Zone': 'PU_Zone',
            'Latitude': 'PU_Latitude',
            'Longitude': 'PU_Longitude'
        }),
        how='left',
        left_on='PUlocationID',
        right_index=True
    )

    trips = trips.merge(
        zones.rename(columns={
            'Borough': 'DO_Borough',
            'Zone': 'DO_Zone',
            'Latitude': 'DO_Latitude',
            'Longitude': 'DO_Longitude'
        }),
        how='left',
        left_on='DOlocationID',
        right_index=True
    )

    trips = trips.dropna(subset=['PU_Borough', 'DO_Borough']).reset_index(drop=True)
    trips = trips.drop(columns=["dispatching_base_num", "pickup_datetime", "dropOff_datetime", "SR_Flag", "Affiliated_base_number"])
    trips["distances"] = np.sqrt(
        (trips["PU_Latitude"] - trips["DO_Latitude"])**2 + (trips["PU_Longitude"] - trips["DO_Longitude"])**2
    )

    return trips, zones
