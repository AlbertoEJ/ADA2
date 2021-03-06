# Proyecto 2
Alumno: Alberto Espinosa Juárez

Programa Académico: Maestría en Ciencias de la Computación

## ¿Qué contiene el proyecto 2?
El proyecto 2 consiste en utilizar la biblioteca creada en "Proyecto_01" para implementar los algoritmos de BFS y DFS.

La instrucción es: Utilizando la biblioteca de grafos desarrollada en el proyecto 1, implementar los algoritmos BFS y DFS (recursivo e iterativo) de tal forma que dado un nodo fuente (s), calculen el árbol inducido por los algoritmos mencionados; es decir, desarrollar los métodos en la clase Grafo:

- def BFS(self, s):
- def DFS_R(self, s):
- def DFS_I(self, s):

Los archivos que contiene la carpeta "Proyecto_02" son: 
+ nodo.py Archivo que contiene la clase que define a un nodo y sus métodos
+ arista.py Archivo que contiene la clase que define a una arista y sus métodos
+ grafo.py Archivo que contiene la clase que define a un grafo y sus métodos, además, contiene los algortimos descritos para el proyecto 1 y contiene los algoritmos DFS (recursivo e iterativo) y BFS, correspondientes al proyecto 02
+ grafo2dot.py Archivo que hace la conversión o traducción a lenguaje DOT para hacerlo compatible con GraphViz y posteriormente abrirlo con el software de visualización de grafos Gephi
+ main.py Archivo que contiene la generación y guardado de cada uno de los grafos, tanto los generados como los calculados.
+ Carpeta archivos_gv_e_imagenes que contiene por subcarpetas los algortimos con sus correspondientes archivos .gv e imágenes
+ ADA_Proyecto2.ipynb este archivo es un notebook en caso de quererlo replicar en Notebook

## Ejecución en local y en nube (Colab)
Para este proyecto realicé dos versiones
1. Ejecución en nube utilizando Google Colab. Para ejecutar el código se debe ir a la siguiente liga https://colab.research.google.com/drive/1R0Cp43TN28XxTia7SNTnHfX8F-tjL6ga?usp=sharing y ejecutar todas las celdas (iniciando de arriba para abajo). No debería existir problema alguno. Los grafos generados se guardan en la sección de "files" dentro de Google Colab (icono de folder en el menú izquierdo).
2. Ejecución en local. Si se clona el repositorio se puede ejecutar en local. Solo se pide leer antes el archivo grafo2dot pues es importante (solo en local).

## ¿Cómo veo la documentación?
Para revisar la documentación es necesario hacer uso del método *help(método)* que nos brindará información sobre cómo y qué hace un método.

**Ejemplo**

help(guardar_grafo)

**Desplegará información sobre el método guardar_grafo así como también de los parámetros que recibe**

## Resúmen del proyecto 2

### Modelo de malla de 30 nodos
#### Generado
![Grafo en malla de 30 nodos (5x6)][malla1]
#### Calculado con BFS
![Grafo en malla calculado con BFS][malla2]
#### Calculado con DFS Iterativo
![Grafo en malla calculado con DFS iterativo][malla3]
#### Calculado con DFS Recursivo
![Grafo en malla calculado con DFS recursivo][malla4]

[malla1]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/30%20nodos/grafo_malla_30_nodos.png?raw=true
[malla2]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/30%20nodos/grafo_malla_30_bfs.png 
[malla3]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/30%20nodos/grafo_malla_30_dfs_i.png 
[malla4]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/30%20nodos/grafo_malla_30_dfs_r.png

### Modelo de malla de 100 nodos
#### Generado
![Grafo en malla de 100 nodos (10x10)][malla100]
#### Calculado con BFS
![Grafo en malla calculado con BFS][malla1002]
#### Calculado con DFS Iterativo
![Grafo en malla calculado con DFS iterativo][malla1003]
#### Calculado con DFS Recursivo
![Grafo en malla calculado con DFS recursivo][malla1004]

[malla100]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/100%20nodos/grafo_malla_100_nodos.png
[malla1002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/100%20nodos/grafo_malla_100_bfs.png
[malla1003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/100%20nodos/grafo_malla_100_dfs_i.png 
[malla1004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/100%20nodos/grafo_malla_100_dfs_r.png

### Modelo de malla de 500 nodos
#### Generado
![Grafo en malla de 500 nodos (10x50)][malla500]
#### Calculado con BFS
![Grafo en malla calculado con BFS][malla5002]
#### Calculado con DFS Iterativo
![Grafo en malla calculado con DFS iterativo][malla5003]
#### Calculado con DFS Recursivo
![Grafo en malla calculado con DFS recursivo][malla5004]

[malla500]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/500%20nodos/grafo_malla_500_nodos.png
[malla5002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/500%20nodos/grafo_malla_500_nodos_bfs.png
[malla5003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/500%20nodos/grafo_malla_500_nodos_dfs_i.png
[malla5004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Mallas/500%20nodos/grafo_malla_500_nodos_dfs_r.png

### Modelo Erdos y Renyi de 30 nodos y 400 aristas

#### Generado
![Grafo erdos renyi 30 nodos y 400 aristas][erdos1]
#### Calculado con BFS
![Grafo erdos renyi calculado con BFS][erdos2]
#### Calculado con DFS iterativo
![Grafo erdos renyi calculado con DFS iterativo][erdos3]
#### Calculado con DFS recursivo
![Grafo erdos renyi calculado con DFS recursivo][erdos4]

[erdos1]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/30/grafo_erdos_30_400.png
[erdos2]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/30/grafo_erdos_30_400_bfs.png
[erdos3]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/30/grafo_erdos_30_400_dfs_i.png
[erdos4]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/30/grafo_erdos_30_400_dfs_r.png

### Modelo Erdos y Renyi de 100 nodos y 1500 aristas

#### Generado
![Grafo erdos renyi 100 nodos y 1500 aristas][erdos100]
#### Calculado con BFS
![Grafo erdos renyi calculado con BFS][erdos1002]
#### Calculado con DFS iterativo
![Grafo erdos renyi calculado con DFS iterativo][erdos1003]
#### Calculado con DFS recursivo
![Grafo erdos renyi calculado con DFS recursivo][erdos1004]

[erdos100]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/100/grafo_erdos_100_1500.png
[erdos1002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/100/grafo_erdos_100_1500_bfs.png
[erdos1003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/100/grafo_erdos_100_1500_dfs_i.png
[erdos1004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/100/grafo_erdos_100_1500_dfs_r.png

### Modelo Erdos y Renyi de 500 nodos y 4000 aristas

#### Generado
![Grafo erdos renyi 500 nodos y 4000 aristas][erdos500]
#### Calculado con BFS
![Grafo erdos renyi calculado con BFS][erdos5002]
#### Calculado con DFS iterativo
![Grafo erdos renyi calculado con DFS iterativo][erdos5003]
#### Calculado con DFS recursivo
![Grafo erdos renyi calculado con DFS recursivo][erdos5004]

[erdos500]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/500/grafo_erdos_500_4000.png
[erdos5002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/500/grafo_erdos_500_4000_bfs.png
[erdos5003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/500/grafo_erdos_500_4000_dfs_i.png
[erdos5004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Erdos_Renyi/500/grafo_erdos_500_4000_dfs_r.png

### Modelo Gilbert de 30 nodos y 0.7
#### Generado
![Gilbert 30 nodos][gilbert1]
#### Calculado con BFS
![Gilbert calculado con BFS][gilbert2]
#### Calculado con DFS iterativo
![Gilbert calculado con DFS iterativo][gilbert3]
#### Calculado con DFS recursivo
![Gilbert calculado con DFS recursivo][gilbert4]

[gilbert1]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/30/grafo_gilbert_30_07.png
[gilbert2]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/30/grafo_gilbert_30_07_bfs.png
[gilbert3]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/30/grafo_gilbert_30_07_dfs_i.png
[gilbert4]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/30/grafo_gilbert_30_07_dfs_r.png

### Modelo Gilbert de 100 nodos y 0.3
#### Generado
![Gilbert 100 nodos][gilbert100]
#### Calculado con BFS
![Gilbert calculado con BFS][gilbert1002]
#### Calculado con DFS iterativo
![Gilbert calculado con DFS iterativo][gilbert1003]
#### Calculado con DFS recursivo
![Gilbert calculado con DFS recursivo][gilbert1004]

[gilbert100]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/100/grafo_gilbert_100_03.png
[gilbert1002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/100/grafo_gilbert_100_03_bfs.png
[gilbert1003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/100/grafo_gilbert_100_03_dfs_i.png
[gilbert1004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/100/grafo_gilbert_100_03_dfs_r.png

### Modelo Gilbert de 500 nodos y 0.02
#### Generado
![Gilbert 500 nodos][gilbert500]
#### Calculado con BFS
![Gilbert calculado con BFS][gilbert5002]
#### Calculado con DFS iterativo
![Gilbert calculado con DFS iterativo][gilbert5003]
#### Calculado con DFS recursivo
![Gilbert calculado con DFS recursivo][gilbert5004]

[gilbert500]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/500/grafo_gilbert_500_002.png
[gilbert5002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/500/grafo_gilbert_500_002_bfs.png
[gilbert5003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/500/grafo_gilbert_500_002_dfs_i.png
[gilbert5004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Gilbert/500/grafo_gilbert_500_002_dfs_r.png

### Modelo geográfico de 30 nodos y 04
#### Generado
![geografico 30 nodos][geo1]
#### Calculado con BFS
![geografico calculado con BFS][geo2]
#### Calculado con DFS iterativo
![geografico calculado con DFS iterativo][geo3]
#### Calculado con DFS recursivo
![geografico calculado con DFS recursivo][geo4]

[geo1]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/30/grafo_geografico_30_04.png
[geo2]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/30/grafo_geografico_30_04_bfs.png
[geo3]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/30/grafo_geografico_30_04_dfs_i.png
[geo4]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/30/grafo_geografico_30_04_dfs_r.png

### Modelo geográfico de 100 nodos y 03
#### Generado
![geografico 100 nodos][geo100]
#### Calculado con BFS
![geografico calculado con BFS][geo1002]
#### Calculado con DFS iterativo
![geografico calculado con DFS iterativo][geo1003]
#### Calculado con DFS recursivo
![geografico calculado con DFS recursivo][geo1004]

[geo100]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/100/grafo_geografico_100_03.png
[geo1002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/100/grafo_geografico_100_03_bfs.png
[geo1003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/100/grafo_geografico_100_03_dfs_i.png
[geo1004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/100/grafo_geografico_100_03_dfs_r.png

### Modelo geográfico de 500 nodos y 01
#### Generado
![geografico 500 nodos][geo500]
#### Calculado con BFS
![geografico calculado con BFS][geo5002]
#### Calculado con DFS iterativo
![geografico calculado con DFS iterativo][geo5003]
#### Calculado con DFS recursivo
![geografico calculado con DFS recursivo][geo5004]

[geo500]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/500/grafo_geografico_500_01.png
[geo5002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/500/grafo_geografico_500_01_bfs.png
[geo5003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/500/grafo_geografico_500_01_dfs_i.png
[geo5004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/geografico/500/grafo_geografico_500_01_dfs_r.png

### Modelo Barabási-Albert 30 nodos y grado 5
#### Generado
![albert 30 nodos][albert1]
#### Calculado con BFS
![albert calculado con BFS][albert2]
### Calculado con DFS iterativo
![aberto calculado con DFS iterativo][albert3]
### Calculado con DFS recursivo
![abertocalculado con DFS recursivo][albert4]

[albert1]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/30/grafo_babarasi_30_05.png
[albert2]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/30/grafo_babarasi_30_05_bfs.png
[albert3]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/30/grafo_babarasi_30_05_dfs_i.png
[albert4]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/30/grafo_babarasi_30_05_dfs_r.png

### Modelo Barabási-Albert 100 nodos y grado 9
#### Generado
![albert 100 nodos][albert100]
#### Calculado con BFS
![albert calculado con BFS][albert1002]
### Calculado con DFS iterativo
![aberto calculado con DFS iterativo][albert1003]
### Calculado con DFS recursivo
![abertocalculado con DFS recursivo][albert1004]

[albert100]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/100/grafo_babarasi_100_09.png
[albert1002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/100/grafo_babarasi_100_09_bfs.png
[albert1003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/100/grafo_babarasi_100_09_dfs_i.png
[albert1004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/100/grafo_babarasi_100_09_dfs_r.png

### Modelo Barabási-Albert 500 nodos y grado 20
#### Generado
![albert 500 nodos][albert500]
#### Calculado con BFS
![albert calculado con BFS][albert5002]
### Calculado con DFS iterativo
![aberto calculado con DFS iterativo][albert5003]
### Calculado con DFS recursivo
![abertocalculado con DFS recursivo][albert5004]

[albert500]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/500/grafo_babarasi_500_20.png
[albert5002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/500/grafo_babarasi_500_20_bfs.png
[albert5003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/500/grafo_babarasi_500_20_dfs_i.png
[albert5004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/babarasi/500/grafo_babarasi_500_20_dfs_r.png

### Modelo Dorogovtsev-Mendes de 30 nodos
#### Generado
![Dorogovtsev-Mendes 30 nodos][mendes1]
#### Calculado con BFS
![Dorogovtsev-Mendes calculado con BFS][mendes2]
#### Calculado con DFS iterativo
![Dorogovtsev-Mendes calculado con DFS iterativo][mendes3]
#### Calculado con DFS recursivo
![Dorogovtsev-Mendes calculado con DFS recursivo][mendes4]

[mendes1]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/30/grafo_dorogovtsev_mendes_30.png
[mendes2]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/30/grafo_dorogovtsev_mendes_30_bfs.png
[mendes3]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/30/grafo_dorogovtsev_mendes_30_dfs_i.png
[mendes4]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/30/grafo_dorogovtsev_mendes_30_dfs_r.png

### Modelo Dorogovtsev-Mendes de 100 nodos
#### Generado
![Dorogovtsev-Mendes 100 nodos][mendes100]
#### Calculado con BFS
![Dorogovtsev-Mendes calculado con BFS][mendes1002]
#### Calculado con DFS iterativo
![Dorogovtsev-Mendes calculado con DFS iterativo][mendes1003]
#### Calculado con DFS recursivo
![Dorogovtsev-Mendes calculado con DFS recursivo][mendes1004]

[mendes100]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/100/grafo_dorogovtsev_mendes_100.png
[mendes1002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/100/grafo_dorogovtsev_mendes_100_bfs.png
[mendes1003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/100/grafo_dorogovtsev_mendes_100_dfs_i.png
[mendes1004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/100/grafo_dorogovtsev_mendes_100dfs_r.png

### Modelo Dorogovtsev-Mendes de 500 nodos
#### Generado
![Dorogovtsev-Mendes 500 nodos][mendes500]
#### Calculado con BFS
![Dorogovtsev-Mendes calculado con BFS][mendes5002]
#### Calculado con DFS iterativo
![Dorogovtsev-Mendes calculado con DFS iterativo][mendes5003]
#### Calculado con DFS recursivo
![Dorogovtsev-Mendes calculado con DFS recursivo][mendes5004]

[mendes500]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/500/grafo_dorogovtsev_mendes_500.png
[mendes5002]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/500/grafo_dorogovtsev_mendes_500_bfs.png
[mendes5003]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/500/grafo_dorogovtsev_mendes_500_dfs_i.png
[mendes5004]: https://github.com/AlbertoEJ/ADA2/blob/main/Proyecto_02/archivos_gv_e_imagenes/Dorogovtsev/500/grafo_dorogovtsev_mendes_500_dfs_r.png

