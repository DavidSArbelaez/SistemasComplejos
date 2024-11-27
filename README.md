# Penguin Search Optimization for Optimal Route Prediction

This project implements the Penguin Search Optimization Algorithm (PeSOA) to find the optimal route between two locations in a ride-hailing network. The project uses real-world trip and zone data to build a graph of locations and predicts the best route using a bio-inspired optimization technique. The results are visualized on a map with the predicted route.

## Project Structure

project/ │ ├── data_loader.py # Loads and preprocesses the trip and zone data ├── graph_builder.py # Builds the graph of zones and distances ├── penguin_search.py # Implements the Penguin Search Optimization Algorithm (PeSOA) ├── map_plotter.py # Visualizes the best path on a map ├── main.py # Main script to execute the complete workflow └── requirements.txt # List of dependencies


## Prerequisites

Before running the project, make sure you have the following:

- Python 3.x
- Dependencies listed in `requirements.txt`

You can install all the necessary libraries by running:


pip install -r requirements.txt


### Required Libraries

- `pandas`: For handling and processing the trip and zone data.
- `numpy`: For numerical operations.
- `folium`: For map visualization.
- `geopy`: For calculating geographical distances between locations.
- `networkx`: For building and managing the graph of locations.

## How to Use

### Step 1: Prepare Your Data

- **Trip Data**: You will need a CSV file containing trip data, including pickup and drop-off locations, and timestamps. The file should have columns like `PUlocationID`, `DOlocationID`, and `pickup_datetime`, `dropOff_datetime`.
  
- **Zone Data**: You also need an Excel file containing zone data. It should include information like location IDs, boroughs, zones, and latitude/longitude coordinates.

Update the paths in the `main.py` file to point to your specific data files:

```python
trip_data_path = 'data/2023_For_Hire_Vehicles_Trip_Data_20241021 (1).csv' 
zone_data_path = 'data\codes.xlsx'
```
Step 2: Run the Optimization
To run the project and find the optimal route:

Start the main script by running:

python main.py


The algorithm will use the Penguin Search Optimization (PeSOA) to find the best route from the starting location to the destination.

The best route will be visualized on a map, and the map will be saved as best_route_map.html.

The best path and total distance will also be printed in the console.

Example Output
```
Best path: [1, 3, 7, 10]
Total distance: 15.5 km
```
The generated map will be saved as best_route_map.html. You can open this file in a web browser to view the map with the optimal route highlighted.

Code Explanation
data_loader.py: This script loads the trip and zone data, processes it to calculate trip duration and distance, and merges the data into a single DataFrame.
graph_builder.py: Builds a graph where nodes represent locations and edges represent distances between them.
penguin_search.py: Implements the Penguin Search Optimization Algorithm (PeSOA) to find the optimal path from a start location to an end location in the graph.
map_plotter.py: Visualizes the best path found by PeSOA on a map using the folium library.
main.py: The main driver script that brings everything together. It loads the data, builds the graph, runs the optimization algorithm, and generates the map visualization.

Acknowledgements
The Penguin Search Optimization Algorithm (PeSOA) is a bio-inspired algorithm used for optimization tasks.

Folium and Geopy are used for mapping and calculating geographical distances.

NetworkX is used for graph management and traversal.


### How to Use the `README.md`

1. **Installation**: Provides instructions on how to install dependencies using the `requirements.txt`.
2. **Data Preparation**: Describes how to prepare your input data files (trip and zone data).
3. **Execution**: Explains how to run the project by executing the `main.py` file and how to view the results.
4. **Explanation of Code**: Briefly explains what each file does within the project.
5. **License**: Mentions that the project is open-source under the MIT license.
6. **Acknowledgments**: Credits external libraries and tools used in the project.


