#--------------------------------------
#name: Dijkstra Algorithm in Python
#version: v1.0
#--------------------------------------

import numpy as np
import sys

class Dijkstra:
    #Initialization
    def __init__(self, graph: dict, start):
        self.graph = graph
        self.startNode = start
        self.distances = np.full(len(graph), sys.maxsize)
        self.predecessor = np.full(len(graph), None)
        self.queue = [start]
        self.distances[self.getIndexOfNode(self.graph.items(), self.startNode)] = 0
        print("")
        print("__________________________________________________________")
        print("Erstes Ergebnis:")
        print("   Entfernung: " + str(self.distances))
        print("    Vorgänger: " + str(self.predecessor))
        print("Warteschlange: " + str(self.queue))
        print("__________________________________________________________")
        print("")
    #Main Programm
    def run(self):
        #So lange die Queue nicht leer ist
        while len(self.queue) > 0:
            #Knoten in Queue mit kleinsten Wert in self.distances
            shortestDistance = sys.maxsize
            shortestIndex = -1
            shortestNode = ""
            for i in range(len(self.queue)):
                indexNode = int(self.queue[i]) - 1
                if(self.distances[indexNode] < shortestDistance):
                    shortestDistance = self.distances[indexNode]
                    shortestIndex = i
                    shortestNode = self.queue[i]

            #entferne Knoten mit kleinstem abstand in self.distances aus queue
            del self.queue[shortestIndex]
            self.distanzUpdate(shortestNode)
            #Zwischenergebnisse
            print("")
            print("__________________________________________________________")
            print("Zwischenergebnisse:")
            print("   Entfernung: " + str(self.distances))
            print("    Vorgänger: " + str(self.predecessor))
            print("Warteschlange: " + str(self.queue))
            print("__________________________________________________________")
            print("")
        #Ergebnisausgabe
        else:
            print("")
            print("__________________________________________________________")
            print("Ergebnis:")
            print("   Entfernung: " + str(self.distances))
            print("    Vorgänger: " + str(self.predecessor))
            print("Warteschlange: " + str(self.queue))
            print("__________________________________________________________")
            print("")

    #Berechnet den Index eines Knoten im graph, da der Knoten als String gespeichert wird
    def getIndexOfNode(self, area, pSearchedNode):
        zaehler = 0
        for key, distance in area:
            if key == pSearchedNode:
                return zaehler
            zaehler = zaehler + 1

        print("Startknoten konnte nicht gefunden werden")

    #Distanzupdate
    def distanzUpdate(self, pShortestNode):
        indexShortestNode = self.getIndexOfNode(self.graph.items(),pShortestNode)
        for node, distance in self.graph[pShortestNode].items():
            indexNeighbourNode = self.getIndexOfNode(self.graph.items(), node)
            alternatively = self.distances[indexShortestNode] + self.graph[pShortestNode][node]
            if alternatively < self.distances[indexNeighbourNode]:
                self.distances[indexNeighbourNode] = alternatively
                self.predecessor[indexNeighbourNode] = pShortestNode
                self.queue += node


#Main Methode
if __name__ == '__main__':
    graph = {
        "1": {"2": 7, "4": 5},
        "2": {"3": 9, "4": 4, "5": 10},
        "3": {"4": 7},
        "4": {"6": 11},
        "5": {"6": 11},
        "6": {"3": 11},
    }
    startknoten = "1"
    d = Dijkstra(graph, startknoten)
    d.run()
