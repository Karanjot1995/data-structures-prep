# Approach: Use BFS, keeping a track of predecessor paths. Maintain visited nodes to avoid cycle.

'''
== Instructions ==
1) Run this code in the REPL to observe its behaviour. The execution entry point is main()
2) Consider adding some additional tests in doTestsPass().
3) Implement def shortestPath(self, fromStationName, toStationName) method to find shortest path between 2 stations
4) If time permits, some possible follow-ups

Visual representation of the Train map used

    King's Cross St Pancras ---------- Angel ----------- Old Street
    |                  \                                    |
    |                   \                                    |
    |                    \                                    |
    |                   Farringdon ------ Barbican ----- Moorgate
    |                                                         |
    Russell Square                                            /
    |                                                        /
    |                                                       /
    |                                                      /
    |                                                     /
    Holborn ------ Chancery Lane ----- St Paul's ----- Bank
'''

'''
/**
* class Station
*
* Respresents Station in the rail network. Each station is identified by unique name. Station is connected with other stations - this information is 
* stored in the neighbours field. Two station objects with the same name are equal therefore they are considered to be same station.
* 
*/
'''

from functools import reduce
from collections import deque, defaultdict

class Station:
    def __init__(self, name):
        self._name = name
        self._neighbours = []
    
    def getName(self):
        return self._name

    def addNeighbour(self, station):
        self._neighbours.append(station)
    
    def getNeighbours(self):
        return self._neighbours
    
    def __eq__(self, other):
        return isinstance(other, Station) and self._name == other.getName()

    def __hash__(self):
        return hash((self._name))

'''
/**
* class TrainMap
*
* Respresents whole rail network - consists of number of the Station objects.
* Stations in the map are bi-directionally connected. Distance between any 2 stations is of same constant distance unit. This implies that shortest
* distance between any 2 stations depends only on number of stations in between
* 
*/
'''

class TrainMap:
    def __init__(self):
        self._stations = {}
    
    def addStation (self, stationName):
        self._stations[stationName] = Station(stationName)
        return self

    def getStation(self, name):
        return self._stations[name]

    def connectStations(self, fromStation, toStation):
        fromStation.addNeighbour(toStation)
        toStation.addNeighbour(fromStation)
        return self
    
    def convertPathToString(self, path):
        if len(path) == 0: return ""
        
        return reduce(lambda s1, s2: s1 + "->" + s2, map(lambda station: station.getName(), path))
    
    def shortestPath(self, fromStationName, toStationName):
        from_station, to_station = self.getStation(fromStationName), self.getStation(toStationName)
        visited = set()
        q = deque([from_station])
        visited.add(from_station)
        parent_map = defaultdict(None)
        
        while q:
            node = q.popleft()
            
            if node == to_station:
                break
            
            for nbr in node.getNeighbours():
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
                    parent_map[nbr] = node
                    # if nei not in parent_map:
                    #     parent_map[nei] = node
        
        # cur = parent_map[to_station]
        # path = [to_station, cur]
        cur = to_station
        path = []
        # print(cur.getName())
        while cur != from_station:
            path.append(cur)
            # print(cur.getName())
            cur = parent_map[cur]
        
        path.append(from_station)
        path.reverse()
        # print(path)

        return path

trainMap = TrainMap()
trainMap.addStation("Kings").addStation("Angel").addStation("Old Street").addStation("Moorgate").addStation("Farringdon").addStation("Barbican").addStation("Russel").addStation("Holborn").addStation("Chancery Lane").addStation("St Paul's").addStation("Bank")

trainMap.connectStations(trainMap.getStation("Kings"), trainMap.getStation("Angel"))
trainMap.connectStations(trainMap.getStation("Kings"), trainMap.getStation("Farringdon"))
trainMap.connectStations(trainMap.getStation("Kings"), trainMap.getStation("Russel"))
trainMap.connectStations(trainMap.getStation("Russel"), trainMap.getStation("Holborn"))
trainMap.connectStations(trainMap.getStation("Holborn"), trainMap.getStation("Chancery Lane"))
trainMap.connectStations(trainMap.getStation("Chancery Lane"), trainMap.getStation("St Paul's"))
trainMap.connectStations(trainMap.getStation("St Paul's"), trainMap.getStation("Bank"))
trainMap.connectStations(trainMap.getStation("Angel"), trainMap.getStation("Old Street"))
trainMap.connectStations(trainMap.getStation("Old Street"), trainMap.getStation("Moorgate"))
trainMap.connectStations(trainMap.getStation("Moorgate"), trainMap.getStation("Bank"))
trainMap.connectStations(trainMap.getStation("Farringdon"), trainMap.getStation("Barbican"))
trainMap.connectStations(trainMap.getStation("Barbican"), trainMap.getStation("Moorgate"))

print(trainMap.convertPathToString(trainMap.shortestPath("Kings", "St Paul's"))) # Kings -> Russel -> Holborn -> Chancery -> St Pauls