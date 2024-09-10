# SistemasComplejos

\documentclass{article}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{geometry}
\usepackage{booktabs}

\geometry{margin=1in}

\title{Algoritmo de Optimización de Búsqueda del Pingüino Aplicado a Vehículos de Alquiler en Nueva York}
\author{Lex Luthor}
\date{Septiembre 2024}

\begin{document}

\maketitle

\section{Introducción}

El \textit{Algoritmo de Optimización de Búsqueda del Pingüino} (PeSOA, por sus siglas en inglés) es un algoritmo bio-inspirado basado en el comportamiento de búsqueda de alimento de los pingüinos en su entorno natural. Este algoritmo puede aplicarse para resolver problemas de optimización en entornos complejos, como la planificación de rutas y la asignación de recursos. En este trabajo, aplicamos el PeSOA para optimizar la asignación de rutas en el contexto del transporte urbano, utilizando datos del mundo real de Vehículos de Alquiler (FHV) en la ciudad de Nueva York. El objetivo es optimizar las rutas para minimizar el tiempo total de viaje y maximizar la eficiencia en la asignación de conductores a pasajeros.

\section{¿Por qué este problema?}

El transporte urbano es uno de los principales retos en las grandes ciudades debido al creciente aumento de la demanda de servicios de movilidad y la necesidad de optimización para mejorar la eficiencia. La ciudad de Nueva York es un excelente caso de estudio debido a su tráfico denso y al gran número de pasajeros que utilizan los servicios de vehículos de alquiler. Optimizar las rutas de estos vehículos puede impactar directamente en los tiempos de espera de los pasajeros, los costos operativos y la congestión del tráfico. Los datos de los Vehículos de Alquiler de Nueva York ofrecen una fuente rica y real para evaluar el rendimiento del algoritmo en un escenario del mundo real.

\section{Conjunto de Datos Utilizado}

El conjunto de datos utilizado para este proyecto es el \textbf{Conjunto de Datos de Viajes de Vehículos de Alquiler de 2023}. Estos registros son generados a partir de los envíos de registros de viajes de Vehículos de Alquiler, que incluyen categorías como vehículos de lujo, servicios tradicionales de transporte y autos de lujo. Los registros de los viajes capturan los siguientes campos:

\begin{itemize}
    \item Número de licencia de la base de despacho
    \item Fecha y hora de recogida
    \item Identificación de la ubicación de recogida, basada en el \textit{Conjunto de Datos Abierto de Zonas de Taxis de Nueva York}
\end{itemize}

Cada fila de este conjunto de datos representa un viaje individual realizado por un FHV en la ciudad de Nueva York.

\textbf{Acceso a los Datos:} Este conjunto de datos es de acceso público y está disponible en \href{https://data.cityofnewyork.us/Transportation/2023-For-Hire-Vehicles-Trip-Data/ywip-y6qr/about_data}{Conjunto de Datos de Viajes de Vehículos de Alquiler de 2023}.

\section{Herramientas Utilizadas}

Para implementar PeSOA y resolver el problema de optimización de rutas, utilizaremos las siguientes herramientas:

\begin{itemize}
    \item \textbf{Python}: Lenguaje de programación para implementar el algoritmo.
    \item \textbf{Bibliotecas}:
    \begin{itemize}
        \item \textbf{Numpy}: Para operaciones numéricas eficientes.
        \item \textbf{Pandas}: Para la manipulación y análisis de datos del \textit{Conjunto de Datos de Viajes de Vehículos de Alquiler de 2023}.
        \item \textbf{Matplotlib} y \textbf{Seaborn}: Para la visualización de datos y rutas.
        \item \textbf{Geopy}: Para calcular distancias geográficas entre los puntos de recogida y entrega.
        \item \textbf{SciPy}: Para funciones de optimización que apoyarán el proceso de búsqueda de soluciones.
        \item \textbf{PuLP}: Para resolver problemas de optimización lineal y combinatoria como referencia.
    \end{itemize}
    \item \textbf{Entorno de Desarrollo}: Jupyter Notebook para la implementación interactiva y visualización de resultados.
\end{itemize}

\section{Modelos Matemáticos}

El \textit{Algoritmo de Optimización de Búsqueda del Pingüino} (PeSOA) se utilizará para optimizar rutas y asignaciones de conductores a pasajeros. Los componentes matemáticos clave incluyen:

\subsection{Función de Aptitud}

El objetivo principal es minimizar el tiempo total de viaje para todos los pasajeros y la distancia total recorrida. La función de aptitud puede expresarse como:

\[
\text{Tiempo Total de Viaje} = \sum_{i=1}^{N} t_{i}
\]

Donde \( t_{i} \) es el tiempo de viaje para el pasajero \( i \), y \( N \) es el número total de pasajeros.

\subsection{Restricciones}

\begin{itemize}
    \item \textbf{Capacidad del Vehículo}: Los vehículos tienen capacidad limitada, por lo que no pueden tomar más pasajeros de los que pueden acomodar.
    \item \textbf{Asignación de Tiempo}: Los pasajeros deben ser recogidos y entregados dentro de una ventana de tiempo razonable.
    \item \textbf{Optimización de Rutas}: Cada vehículo debe seguir una ruta eficiente para recoger y entregar a los pasajeros, evitando recorridos innecesariamente largos.
\end{itemize}

\subsection{Estrategia de Exploración y Explotación}

Los "pingüinos" en PeSOA representan diferentes combinaciones de rutas de vehículos y asignaciones de pasajeros. La exploración implica probar nuevas combinaciones de rutas, mientras que la explotación mejora las soluciones prometedoras ya encontradas.

\subsection{Enfriamiento}

Al igual que los pingüinos ajustan su búsqueda de alimentos en ambientes difíciles, el algoritmo utiliza un mecanismo de enfriamiento para optimizar la solución con mayor precisión a medida que avanza.

\section{Soluciones Propuestas}

Las soluciones propuestas utilizando PeSOA son las siguientes:

\begin{enumerate}
    \item \textbf{Optimización de Rutas de Vehículos}: Usando los datos de recogida y entrega, PeSOA generará rutas que minimicen los tiempos de viaje de los pasajeros.
    \item \textbf{Minimización de Tiempos de Espera y Costos}: Probaremos diferentes configuraciones de PeSOA para reducir tanto los tiempos de espera de los pasajeros como los costos operativos.
    \item \textbf{Validación y Comparación}: Las soluciones obtenidas se compararán con otros algoritmos de optimización, como \textit{Algoritmos Genéticos} (GA) y \textit{Recocido Simulado} (SA).
    \item \textbf{Visualización de Rutas y Patrones de Demanda}: Finalmente, visualizaremos las rutas generadas y analizaremos los patrones de demanda en diferentes momentos del día, evaluando cómo PeSOA mejora la distribución de los viajes.
\end{enumerate}


\begin{thebibliography}{9}

\bibitem{pesoa}
S. K. Ghosh, M. Roy, and P. Roy, ``Penguin Search Optimization Algorithm: A new metaheuristic for optimization problems,'' \textit{Journal of Computational Science}, vol. 22, pp. 234-250, 2020.

\bibitem{nyc_tlc}
City of New York, ``2023 For-Hire Vehicles Trip Data,'' \textit{NYC Taxi & Limousine Commission}, [Online]. Available: \url{https://data.cityofnewyork.us/Transportation/2023-For-Hire-Vehicles-Trip-Data/ywip-y6qr/about_data}. [Accessed: 09-Sep-2024].



\end{thebibliography}

\end{document}
