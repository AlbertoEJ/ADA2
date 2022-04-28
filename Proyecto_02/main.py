from grafo2dot import guardar_grafo
from grafo import Grafo



# Generamos grafo de mallas con 30 nodos
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(5, 6) 
guardar_grafo(grafo_malla_30, "grafo_malla_30_nodos") #Grafo de 5*6 nodos
guardar_grafo(grafo_malla_30.bfs("1"),"grafo_malla_30_bfs")
guardar_grafo(grafo_malla_30.dfs_i("1"),"grafo_malla_30_dfs_i")
guardar_grafo(grafo_malla_30.dfs_r("1"),"grafo_malla_30_dfs_r")
# Generamos grafo de mallas con 100 nodos
grafo_malla_100 = Grafo(dirigido=False)
grafo_malla_100.grafo_malla(10, 10)
guardar_grafo(grafo_malla_100, "grafo_malla_100_nodos") #Grafo de 10*10 nodos
guardar_grafo(grafo_malla_100.bfs("1"),"grafo_malla_100_bfs")
guardar_grafo(grafo_malla_100.dfs_i("1"),"grafo_malla_100_dfs_i")
guardar_grafo(grafo_malla_100.dfs_r("1"),"grafo_malla_100_dfs_r")
# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos") #Grafo de 50*10 nodos
guardar_grafo(grafo_malla_500.bfs("1"), "grafo_malla_500_nodos_bfs")
guardar_grafo(grafo_malla_500.dfs_i("1"), "grafo_malla_500_nodos_dfs_i")
guardar_grafo(grafo_malla_500.dfs_r("1"), "grafo_malla_500_nodos_dfs_r")
# Generamos grafo Erdös y Rényi con 30 nodos y 400 aristas
grafo_erdos_30_200 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(30 , 400) 
guardar_grafo(grafo_erdos_30_200, "grafo_erdos_30_400") #Grafo de 30 nodos con 400 aristas
guardar_grafo(grafo_erdos_30_200.bfs("1"), "grafo_erdos_30_400_bfs")
guardar_grafo(grafo_erdos_30_200.dfs_i("1"), "grafo_erdos_30_400_dfs_i")
guardar_grafo(grafo_erdos_30_200.dfs_r("1"), "grafo_erdos_30_400_dfs_r")
# Generamos grafo Erdös y Rényi con 100 nodos y 400 aristas
grafo_erdos_100_400 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(100, 1500)
guardar_grafo(grafo_erdos_30_200, "grafo_erdos_100_1500")  #Grafo de 100 nodos con 1500 aristas
guardar_grafo(grafo_erdos_30_200.bfs("1"),"grafo_erdos_100_1500_bfs")
guardar_grafo(grafo_erdos_30_200.dfs_i("1"), "grafo_erdos_100_1500_dfs_i")
guardar_grafo(grafo_erdos_30_200.dfs_r("1"),"grafo_erdos_100_1500_dfs_r")
# Generamos grafo Erdös y Rényi con 500 nodos y 4000 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 4000) 
guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_4000") #Grafo de 500 nodos con 4000 aristas
guardar_grafo(grafo_erdos_500_2500.bfs("1"),"grafo_erdos_500_4000_bfs")
guardar_grafo(grafo_erdos_500_2500.dfs_i("1"),"grafo_erdos_500_4000_dfs_i")
guardar_grafo(grafo_erdos_500_2500.dfs_r("1"),"grafo_erdos_500_4000_dfs_r")
# generamos grafo con modelo de Gilbert 30 nodos y probabilidad 0.7
grafo_gilbert_30_05 = Grafo(dirigido=False)
grafo_gilbert_30_05.grafo_gilbert(30, 0.7) 
guardar_grafo(grafo_gilbert_30_05, "grafo_gilbert_30_07") #Grafo de 30 nodos con probabilidad 0.7
guardar_grafo(grafo_gilbert_30_05.bfs("1"),"grafo_gilbert_30_07_bfs")
guardar_grafo(grafo_gilbert_30_05.dfs_i("1"),"grafo_gilbert_30_07_dfs_i")
guardar_grafo(grafo_gilbert_30_05.dfs_r("1"),"grafo_gilbert_30_07_dfs_r")
# generamos grafo con modelo de Gilbert 100 nodos y probabilidad 0.6
grafo_gilbert_100_03 = Grafo(dirigido=False)
grafo_gilbert_100_03.grafo_gilbert(100, 0.6)
guardar_grafo(grafo_gilbert_100_03, "grafo_gilbert_100_03") #Grafo de 30 nodos con probabilidad 0.6
guardar_grafo(grafo_gilbert_100_03.bfs("1"),"grafo_gilbert_100_03_bfs")
guardar_grafo(grafo_gilbert_100_03.dfs_i("1"),"grafo_gilbert_100_03_dfs_i")
guardar_grafo(grafo_gilbert_100_03.dfs_r("1"),"grafo_gilbert_100_03_dfs_r")
# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.04
grafo_gilbert_500_002 = Grafo(dirigido=False)
grafo_gilbert_500_002.grafo_gilbert(500, 0.04)
guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_004")  #Grafo de 500 nodos con probabilidad 0.04
guardar_grafo(grafo_gilbert_500_002.bfs("1"),"grafo_gilbert_500_002_bfs")
guardar_grafo(grafo_gilbert_500_002.dfs_i("1"),"grafo_gilbert_500_002_dfs_i")
guardar_grafo(grafo_gilbert_500_002.dfs_r("1"),"grafo_gilbert_500_002_dfs_r")
# generamos grafo con modelo geográfico simple con 30 nodos y r=0.4
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(30, 0.4)
guardar_grafo(grafo_geografico_30_05, "grafo_geografico_30_04") #30 nodos r=0.4
guardar_grafo(grafo_geografico_30_05.bfs("1"), "grafo_geografico_30_04_bfs")
guardar_grafo(grafo_geografico_30_05.dfs_i("1"), "grafo_geografico_30_04_dfs_i")
guardar_grafo(grafo_geografico_30_05.dfs_r("1"), "grafo_geografico_30_04_dfs_r")
# generamos grafo con modelo geográfico simple con 100 nodos y r=0.3
grafo_geografico_100_03 = Grafo(dirigido=False)
grafo_geografico_100_03.grafo_geografico(100, 0.3)
guardar_grafo(grafo_geografico_100_03, "grafo_geografico_100_03") #100 nodos, r=0.3
guardar_grafo(grafo_geografico_100_03.bfs("1"), "grafo_geografico_100_03_bfs")
guardar_grafo(grafo_geografico_100_03.dfs_i("1"), "grafo_geografico_100_03_dfs_i")
guardar_grafo(grafo_geografico_100_03.dfs_r("1"), "grafo_geografico_100_03_dfs_r")

# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.1)
guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01") #500 nodos, r=0.1
guardar_grafo(grafo_geografico_500_01.bfs("1"), "grafo_geografico_500_01_bfs")
guardar_grafo(grafo_geografico_500_01.dfs_i("1"), "grafo_geografico_500_01_dfs_i")
guardar_grafo(grafo_geografico_500_01.dfs_r("1"), "grafo_geografico_500_01_dfs_r")

# generamos grafo con modelo Barabási-Albert con 30 nodos y grado 05
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(30, 5, False, False)
guardar_grafo(grafo_babarasi_30_10, "grafo_babarasi_30_05") #30 nodos grado 05
guardar_grafo(grafo_babarasi_30_10.bfs("1"), "grafo_babarasi_30_05_bfs")
guardar_grafo(grafo_babarasi_30_10.dfs_i("1"), "grafo_babarasi_30_05_dfs_i")
guardar_grafo(grafo_babarasi_30_10.dfs_r("1"), "grafo_babarasi_30_05_dfs_r")
# generamos grafo con modelo Barabási-Albert con 100 nodos y grado 09
grafo_babarasi_100_07 = Grafo(dirigido=False)
grafo_babarasi_100_07.grafo_barabasi_albert(100, 9) 
guardar_grafo(grafo_babarasi_100_07, "grafo_babarasi_100_09") #100 nodos grado 9
guardar_grafo(grafo_babarasi_100_07.bfs("1"), "grafo_babarasi_100_09_bfs")
guardar_grafo(grafo_babarasi_100_07.dfs_i("1"), "grafo_babarasi_100_09_dfs_i")
guardar_grafo(grafo_babarasi_100_07.dfs_r("1"), "grafo_babarasi_100_09_dfs_r")
# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 20
grafo_babarasi_500_12 = Grafo(dirigido=False)
grafo_babarasi_500_12.grafo_barabasi_albert(500, 20)
guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_20") #500 nodos grado 20
guardar_grafo(grafo_babarasi_500_12.bfs("1"), "grafo_babarasi_500_20_bfs")
guardar_grafo(grafo_babarasi_500_12.dfs_i("1"), "grafo_babarasi_500_20_dfs_i")
guardar_grafo(grafo_babarasi_500_12.dfs_r("1"), "grafo_babarasi_500_20_dfs_r")
# generamos grafo con modelo Dorogovtsev-Mendes con 30 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30)
guardar_grafo(grafo_dorogovtsev_mendes_30, "grafo_dorogovtsev_mendes_30")
guardar_grafo(grafo_dorogovtsev_mendes_30.bfs("1"), "grafo_dorogovtsev_mendes_30_bfs")
guardar_grafo(grafo_dorogovtsev_mendes_30.dfs_i("1"), "grafo_dorogovtsev_mendes_30_dfs_i")
guardar_grafo(grafo_dorogovtsev_mendes_30.dfs_r("1"), "grafo_dorogovtsev_mendes_30_dfs_r")
# generamos grafo con modelo Dorogovtsev-Mendes con 100 nodos
grafo_dorogovtsev_mendes_100 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_100.dorogovtsev_mendes(100)
guardar_grafo(grafo_dorogovtsev_mendes_100, "grafo_dorogovtsev_mendes_100")
guardar_grafo(grafo_dorogovtsev_mendes_100.bfs("1"), "grafo_dorogovtsev_mendes_100_bfs")
guardar_grafo(grafo_dorogovtsev_mendes_100.dfs_i("1"), "grafo_dorogovtsev_mendes_100_dfs_i")
guardar_grafo(grafo_dorogovtsev_mendes_100.dfs_r("1"), "grafo_dorogovtsev_mendes_100dfs_r")
# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
guardar_grafo(grafo_dorogovtsev_mendes_500.bfs("1"), "grafo_dorogovtsev_mendes_500_bfs")
guardar_grafo(grafo_dorogovtsev_mendes_500.dfs_i("1"), "grafo_dorogovtsev_mendes_500_dfs_i")
guardar_grafo(grafo_dorogovtsev_mendes_500.dfs_r("1"), "grafo_dorogovtsev_mendes_500_dfs_r")
