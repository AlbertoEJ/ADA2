"""
definición de la clase grafo, posee un diccionario para almacenar objetos de tipo nodo
las aristas se guardan en una estructura tipo set

"""
from arista import Arista
from nodo import Nodo
import random
import itertools
import math
from collections import deque
import random
import itertools
import math

from collections import deque
"""
Autor: Alberto Espinosa Juárez
Escuela: CIC IPN
Materia: Analisis y Diseño de Algoritmos
Ruta: D:\Escuela\CIC\Segundo\ADA\Proyecto_1
"""

class Grafo:
    """
    Creacion de la clase grafo, aqui se almacenaran todos los algoritmos y se crearan los grafos, para ello, 
    es necesario en primera instancia que las clases Nodo Y Arista se encuentren importadas correctamente
    """
    def __init__(self, dirigido=False):

        """
        Constructor de la clase
        """
        self.nodos = {}  # diccionario para almacenar los nodos con su etiqueta como llave
        self.__aristas = set()  # mantiene las aristas guardadas en un conjunto
        self.__dirigido = dirigido  # parametro para saber si el grafo es dirigido

    def __str__(self):  # sobreescritura del metodo string
        imp_cadena = ""
        nodos_copy=self.nodos
        for llave in nodos_copy.copy():
            if str(nodos_copy[llave])=="":
               # nodos_copy.pop(llave)
                pass
            else:
                new_string = str(nodos_copy[llave]).replace(llave, "")
                if  not new_string.startswith(llave):
                    if new_string.startswith(" --"):
                        imp_cadena += llave + new_string + '\n'
                    else:
                        if new_string.endswith("-- "):
                            t = new_string.rsplit('--', 1)
                            u = ''.join(t)
                        else:
                            t = new_string.rsplit('--',1)
                            u = ''.join(t)
                        if u=='':
                            u=''
                        imp_cadena += "{0} -- ".format(llave) + u + '\n'



        return imp_cadena

    def add_nodo(self, etiqueta): 
        """
        Metodo que nos permite crear un nodo
        Parametro: 
        Etiqueta
        Retorna
        Nodo con la etiqueta colocada
        """
        if etiqueta not in self.nodos:
            self.nodos[etiqueta] = Nodo(etiqueta, self.__dirigido)

    def add_arista(self, etiqueta_inicio, etiqueta_final):  

        """
        Metodo para la creacion de una arista. Regresara un mensaje si no se encuentra el nodo inicial o final
        Parametros:
        Nodo_inicio
        Nodo_final
        Retorna
        Arista que conecta nodo A--B 
        """
        nodo_fuente = self.get_nodo(etiqueta_inicio)
        nodo_final = self.get_nodo(etiqueta_final)
        mirror_edge = None
        if (nodo_fuente or nodo_final) is None:  # si no existe el nodo fuente o el nodo destino salta el error
            print(nodo_fuente,nodo_final)
            raise ValueError("El nodo inicio o final no existe, debes crearlo primero")
        if self.__dirigido:  # Si el grafo es dirigido se agrega la arista tal cual
            arista = Arista(nodo_fuente, nodo_final, self.__dirigido)
        else:
            for aristaen in self.get_aristas():
                nodo_fuente_arista = aristaen.get_nodo_fuente()
                nodo_destino_arista = aristaen.get_nodo_destino()
                if (nodo_destino_arista == nodo_fuente) and (nodo_fuente_arista == nodo_final):
                    mirror_edge = True
            if not mirror_edge:
                arista = Arista(nodo_fuente, nodo_final, self.__dirigido)
            else:
                arista = Arista(nodo_final, nodo_fuente, self.__dirigido)
        nodo_fuente.add_arista(arista)
        if nodo_fuente != nodo_final:
            nodo_final.add_arista(arista)

        self.__aristas.add(arista)

    def remove_arista(self, etiqueta_inicio, etiqueta_final):  
        """
        Metodo para eliminar una arista
        Parametros:
        Nodo_inciial
        Nodo_final
        Retorna:
        La eliminacion de la arista
        """
        nodo_fuente = self.get_nodo(etiqueta_inicio)
        nodo_destino = self.get_nodo(etiqueta_final)

        if (nodo_fuente or nodo_destino) is None:
            raise ValueError("No se encontro el nodo fuente o el nodo destino en el grafo")

        arista = Arista(nodo_fuente, nodo_destino, self.__dirigido)

        if arista not in self.__aristas:
            raise ValueError( "no se encuentra la arista  {0} en el grafo".format(str(Arista)))

        nodo_fuente.remove_arista(arista)
        nodo_destino.remove_arista(arista)
        self.__aristas.remove(arista)

    def remove_nodo(self, etiqueta_nodo): 

        """
        Metodo que permite la eliminacion del nodo en el grafo
        """
        if etiqueta_nodo not in self.nodos:
            raise ValueError("No se encontro el nodo {0} en el grafo".format(etiqueta_nodo))

        nodo = self.nodos[etiqueta_nodo]

        copia_aristas_entrantes = nodo.get_aristas_entrantes().copy()  # Removemos la entrada de las aristas entrantes
        for arista in copia_aristas_entrantes:
            nodo_adyacente = arista.get_nodo_fuente()
            nodo_adyacente.remove_arista(arista)

            if arista in self.__aristas:
                self.__aristas.remove(arista)

        copia_aristas_salientes = nodo.get_aristas_salientes().copy()
        for arista in copia_aristas_salientes:  # Removemos la entrada de las aristas salientes
            adjacent_vertex = arista.get_nodo_destino()
            adjacent_vertex.remove_arista(arista)

            if arista in self.__aristas:
                self.__aristas.remove(arista)

        self.nodos.pop(etiqueta_nodo)

        nodos = self.get_nodos()
        for nodo in nodos:
            aristas = nodos[nodo].get_aristas()
            copia_aristas = aristas.copy()
            for arista in aristas:
                nodo = arista.get_nodo_fuente()
                if nodo.get_etiqueta() == etiqueta_nodo:
                    copia_aristas.remove(arista)
                nodo.set_aristas(copia_aristas)


    def get_nodo(self, etiqueta):
        return self.nodos.get(etiqueta)

    def get_nodos(self):
        return self.nodos

    def get_aristas(self):
        return self.__aristas

    def get_grado(self, etiqueta):
        if self.es_dirigido():
            grado = len(self.get_nodo(etiqueta).get_aristas_entrantes()) + \
                    len(self.get_nodo(etiqueta).get_aristas_salientes())
        else:
            grado = len(self.get_nodo(etiqueta).get_aristas_salientes())
        return grado

    def es_dirigido(self):  # Metodo que regresa si el grafo es dirigido
        return self.__dirigido

    #Grafo Malla
    def grafo_malla(self, m, n):
        """
        Metodo que permite la creacion de un grafo en malla
        Parametros
        m
        n
        Devuelve
        Grafo en malla de m*n
        """
        for i in range(m * n):  # se comienza creando los n nodos
            self.add_nodo(str(i))
        for j in range(m):
            index_horizontal = j * n
            for i in range(index_horizontal, index_horizontal + n):
                if (i != (n - 1) + index_horizontal):
                    self.add_arista(str(i), str(i + 1))
                if j != (m - 1):
                    self.add_arista(str(i), str(i + n))
        return self
    #Grafo Erdos Renyi
    def grafo_erdos_renyi(self, n, m, dirigido=False, auto=False): 
        """
        Metodo que crea un grafo con el algoritmo Erdos Renyi
        Parametros:
        n
        m
        Direccion
        Auto 
        Retorna
        Grafo Erdos Renyi de n*m
        """
        self.__dirigido = dirigido
        for i in range(n):
            self.add_nodo(str(i))
        while len(self.get_aristas()) != m:
            n1 = (random.randrange(n))
            n2 = (random.randrange(n))
            if not auto:
                if n1 != n2:
                    self.add_arista(str(n1), str(n2))
            else:
                self.add_arista(str(n1), str(n2))
        print(len(self.get_aristas()))
        return self
    
    #grafo Gilbert
    def grafo_gilbert(self, n, p, dirigido=False, auto=False):

        """
        Metodo que permite crear un grafo con el algoritmo de Gilbert
        Parametros:
        n
        p
        Direccion
        Auto
        Devuelve:
        Grafo de n nodos con probabilidad p
        """
        self.__dirigido = dirigido
        for i in range(n):
            self.add_nodo(str(i))
        for i in range(n):
            for j in range(n):
                if not auto:
                    if (i != j):
                        if random.random() <= p:
                            self.add_arista(str(i), str(j))
        print(len(self.get_aristas()))
        return self

    def grafo_geografico(self, n, r, dirigido=False, auto=False):  # metodo para generar el modelo geografico

        """
        Metodo que permite la creacion de un grafo geografico
        Parametros:
        n
        r
        direccion
        auto
        Retorna
        Un grafo geografico de n nodos con distancia maxima r(0,1)
        """
        self.__dirigido = dirigido  # parametro dirigido
        for i in range(n):  # se crean n nodos
            self.add_nodo(str(i))
        posicion_nodos = {}  # diccionario para mantener las cordenadas de los nodos
        for nodo in self.get_nodos():  # asignamos cordenadas  a los nodos
            llave = nodo
            posicion_random = (random.random(), random.random())
            posicion_nodos.update({llave: posicion_random})
        combinaciones = itertools.combinations(posicion_nodos, 2)  # todos los posibles pares si el grafo es no dirigido
        permutaciones = itertools.permutations(posicion_nodos, 2)  # todos los posibles pares si el grafi es dirigido
        if not dirigido:  # si el grafo es no dirigido usamos las combinaciones para comparar la distancia de los pares
            for combinacion in combinaciones:
                nodo_fuente = combinacion[0]
                nodo_destino = combinacion[1]
                cordenadas_nodo_fuente = posicion_nodos.get(combinacion[0])
                cordenadas_nodo_destino = posicion_nodos.get(combinacion[1])
                nodo_fuente_x = cordenadas_nodo_fuente[0]
                nodo_fuente_y = cordenadas_nodo_fuente[1]
                nodo_destino_x = cordenadas_nodo_destino[0]
                nodo_destino_y = cordenadas_nodo_destino[1]
                # calculamos la distancia entre pares
                distancia = math.sqrt((nodo_destino_x - nodo_fuente_x) ** 2 + (nodo_destino_y - nodo_fuente_y) ** 2)
                # si la distancia es menor o igual a r se genera la arista ente pares
                if (distancia <= r):
                    self.add_arista(nodo_fuente, nodo_destino)
        else:  # lo mismo pero cuando el grafo es no dirigido usamos permutaciones
            for permutacion in permutaciones:
                nodo_fuente = permutacion[0]
                nodo_destino = permutacion[1]
                cordenadas_nodo_fuente = posicion_nodos.get(permutacion[0])
                cordenadas_nodo_destino = posicion_nodos.get(permutacion[1])
                nodo_fuente_x = cordenadas_nodo_fuente[0]
                nodo_fuente_y = cordenadas_nodo_fuente[1]
                nodo_destino_x = cordenadas_nodo_destino[0]
                nodo_destino_y = cordenadas_nodo_destino[1]
                distancia = math.sqrt((nodo_destino_x - nodo_fuente_x) ** 2 + (nodo_destino_y - nodo_fuente_y) ** 2)
                if (distancia <= r):
                    self.add_arista(nodo_fuente, nodo_destino)
        return self


    #grafo Dorogovtsev-Mendes
    def dorogovtsev_mendes(self, n, dirigido=False):
        """
        Metodo que permite la creacion de un grafo Dorogovtsev-Mendes
        Parametros
        n
        Retorna:
        Grafo de n nodos
        """
        self.__dirigido = dirigido
        for i in range(3):
            self.add_nodo(str(i))
        self.add_arista("0", "1")
        self.add_arista("0", "2")
        self.add_arista("1", "2")
        while len(self.get_nodos()) != n:
            nodo_nuevo = str(len(self.get_nodos()) + 1)
            self.add_nodo(nodo_nuevo)
            arista_random = random.choice(list(self.get_aristas()))
            nodo_fuente = arista_random.get_nodo_fuente()
            etiqueta_nodo_fuente = nodo_fuente.get_etiqueta()
            nodo_destino = arista_random.get_nodo_destino()
            etiqueta_nodo_destino = nodo_destino.get_etiqueta()
            self.add_arista(nodo_nuevo, etiqueta_nodo_fuente)
            self.add_arista(nodo_nuevo, etiqueta_nodo_destino)
        print("numero de nodos: {}".format(len(self.get_nodos())))
        print("numero de aristas: {}".format(len(self.get_aristas())))
        return self

    #Grafo Barabási-Albert
    def grafo_barabasi_albert(self, n, d, dirigido=False, auto=False):

        """
        Metodo que permite crear un grafo Barabási-Albert
        Parametros:
        n
        d
        direccion
        auto
        Retorna:
        Grafo de Barabási-Albert con n nodos y grado maximo d
        """
        self.__dirigido = dirigido
        for i in range(n):  # se generan n nodos
            self.add_nodo(str(i))
        for i in range(n):  # iteramos entre todos los posibles pares
            for j in range(n):
                if not auto:  # si no se permiten autociclos
                    if i != j:
                        if (self.get_grado(str(j)) < d) and (self.get_grado(str(i)) < d):
                            p = 1 - (self.get_grado(str(j)) / d)
                            if random.random() <= p:  # si el numero random es menor o igual a la probailidad se crea
                                self.add_arista(str(i), str(j))
                else:  # lo  mismo pero si se permiten autociclos
                    if (self.get_grado(str(j)) < d) and (self.get_grado(str(i)) < d):
                        p = 1 - (self.get_grado(str(j)) / d)
                        if random.random() <= p:
                            self.add_arista(str(i), str(j))
        print(len(self.get_aristas()))
        return self

    def get_nodos_adyacentes(self,node):

        """
        Método que obtiene los nodos adyacentes
        Parametros:
        nodo a calcular nodos adyacentes
        Retorna:
        Nodos adyacentes a nodo
        """
        nodos_adyacentes=[]
        nodo=self.get_nodo(node)
        for arista in nodo.get_aristas():
            if arista.get_nodo_fuente()!=nodo:
                nodos_adyacentes.append(arista.get_nodo_fuente().get_etiqueta())
            else:
                nodos_adyacentes.append(arista.get_nodo_destino().get_etiqueta())
        return nodos_adyacentes


    def get_hijos(self,node):

        """
        Método que obtiene los hijos de un nodo
        Parametros:
        nodo a calcular hijos
        Retorna:
        Nodos hijos a nodo
        """
        nodos_adyacentes=[]
        nodo=self.get_nodo(node)
        for arista in nodo.get_aristas():
            if arista.get_nodo_fuente()==nodo:
                nodos_adyacentes.append(arista.get_nodo_destino().get_etiqueta())
        return nodos_adyacentes
    def get_padres(self,node): 

        """
        Método que obtiene los ancestros de un nodo
        Parametros:
        nodo
        Retorna:
        Ancestros de noodo
        """
        nodos_adyacentes=[]
        nodo=self.get_nodo(node)
        for arista in nodo.get_aristas():
            if arista.get_nodo_fuente()!=nodo:
                nodos_adyacentes.append(arista.get_nodo_fuente().get_etiqueta())
        return nodos_adyacentes

    def bfs(self, s): # Metodo de algoritmo de busqueda bfs


        """
        Método de algortimo BFS
        Parametro: 
        s : grafo
        Retorna
        Busqueda BFS
        """
        queue = deque([s]) # cola que nos permitira guadar los nodos para ejecutar el algoritmo bfs
        capa = {s: 0} # creamos la capa 0
        ancestro = {s: None} # diccionario que nos permitira guardar los nodos y la relacion con sus hijos
        arbol = Grafo() #creamos un nuevo objeto de tipo grafo para generar el arbol que nos da el algoritmo bfs
        while queue: #mientras haya elementos en la cola
            nodo = queue.popleft() #extraemos el nodo de la cola
            arbol.add_nodo(nodo) #agregamos el nodo al arbol
            for n in self.get_nodos_adyacentes(nodo):#agregamos los nodos adyacentes al nodo a su respectiva capa
                if n not in capa:
                    queue.append(n)
                    capa[n] = capa[nodo] + 1
                    ancestro[n] = nodo

        for key in ancestro: #se agregan todas las aristas al arbol
            if ancestro[key]!=None:
                arbol.add_arista(ancestro[key], key)

        return arbol

    def dfs_i(self, s): #Metodo de algoritmo de busqueda dfs iterativo

        """
        Método de algoritmo DFS iterativo
        Parametro:
        S : grafo
        Retorna
        Busqeuda DFS
        """
        arbol_dfs = Grafo() #creamos un nuevo objeto tipo grafo para almacenar el arbol creado por el algoritmo
        explorados = [s] # agregamos el nodo fuente a la lista de explorados
        #print(explorados)
        arbol_dfs.add_nodo(s)   #agregamos el nodo fuente al arbol
        u = self.get_nodo(s)
        stack = [] #inicializamos el stack
        while len(explorados)<len(self.get_nodos()):
            #print(stack)
            #print(explorados)
            #print("explorando:{}".format(u))
            aristas = u.get_aristas()
            for arista in aristas:   # añadir al stack todos los nodos adyacentes a u
                #print(arista)
                #print("etiqueta de U:{}".format(u.get_etiqueta()))
                #print("Nodo fuente:{}".format(arista.get_nodo_fuente()))
                #print("Nodo destino:{}".format(arista.get_nodo_destino()))
                if str(u.get_etiqueta()) == str(arista.get_nodo_fuente()): #verificamos la direccion de la arista
                    comp=True
                else:
                    comp=False
                v = arista.get_nodo_destino() if comp else arista.get_nodo_fuente()
                #print("u:{} y v:{}".format(u,v))
                if str(v) not in explorados: #se agrega al stack la arista del nodo explorado
                    stack.append((u.get_etiqueta(), v.get_etiqueta()))
            if not stack:
                break
            padre, hijo = stack.pop() # hacemos pop al stack
            if hijo not in explorados:
                arbol_dfs.add_nodo(hijo)
                #print(padre,hijo)
                arbol_dfs.add_arista(padre,hijo) # se agrega la arista nueva al arbol
                explorados.append(hijo) # se agrega el  nodo explorado a la lista de explorados

            u = self.get_nodo(hijo)
            #print("nuevo u:{}".format(u))

        return arbol_dfs



    def dfs_r(self, u): #Metodo de algoritmo de busqueda dfs recursivo

        """
        Método de algoritmo DFS recursivo
        Parametro:
        S : grafo
        Retorna
        Busqueda DFS    
        """

        arbol_dfs = Grafo()
        explorados = set()
        self.recursive_tool(u, arbol_dfs, explorados)

        return arbol_dfs

    def recursive_tool(self, u, arbol_dfs, explorados):

        arbol_dfs.add_nodo(u)
        explorados.add(u)
        u=self.get_nodo(u)
        aristas = u.get_aristas()

        for arista in aristas:
            v = arista.get_nodo_destino().get_etiqueta()
            if str(u.get_etiqueta()) == str(arista.get_nodo_fuente()):  # verificamos la direccion de la arista
                comp = True
            else:
                comp = False
            v = arista.get_nodo_destino().get_etiqueta() if comp else arista.get_nodo_fuente().get_etiqueta()
            if v in explorados:
                continue
            arbol_dfs.add_nodo(arista.get_nodo_fuente().get_etiqueta()) #se agegan los nodos correspondientes a la arista al grafo
            arbol_dfs.add_nodo(arista.get_nodo_destino().get_etiqueta())#se agegan los nodos correspondientes a la arista al grafo
            #print(arista.get_nodo_fuente().get_etiqueta(),arista.get_nodo_destino().get_etiqueta())
            arbol_dfs.add_arista(arista.get_nodo_fuente().get_etiqueta(),arista.get_nodo_destino().get_etiqueta())
            self.recursive_tool(v, arbol_dfs, explorados)