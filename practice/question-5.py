#https://www.youtube.com/watch?v=qz9tKlF431k
from queue import Queue

# M elements
airports = [
    "BGI", "CDG", "DEL", "DOH", "DSM", "EWR", "EYW", "HND", "ICN",
    "JFK", "LGA", "LHR", "ORD", "SAN", "SFO", "SIN", "TLV", "BUD"
]

# N elements
routes = [
    ["DSM", "ORD"],
    ["ORD", "BGI"],
    ["BGI", "LGA"],
    ["SIN", "CDG"],
    ["CDG", "SIN"],
    ["CDG", "BUD"],
    ["DEL", "DOH"],
    ["DEL", "CDG"],
    ["TLV", "DEL"],
    ["EWR", "HND"],
    ["HND", "ICN"],
    ["HND", "JFK"],
    ["ICN", "JFK"],
    ["JFK", "LGA"],
    ["EYW", "LHR"],
    ["LHR", "SFO"],
    ["SFO", "SAN"],
    ["SFO", "DSM"],
    ["SAN", "EYW"]
]

startingAirport = "LGA"

class Solution:
    def __init__(self, airport_list, flights, startingAirport) -> None:
        self.airports = airport_list
        self.flights = flights
        self.startingAirport = startingAirport
        self.graph = self.generate_graph()
        self.island = self.find_island()
    
    def find_island(self):
        visited = []
        count = 0
        for airport in self.graph.keys():
            if self.explore(airport, visited):
                count += 1
        return count
    
    def explore(self, node, visited):
        if node in visited:
            return False
        visited.append(node)
        for n in  self.graph[node]:
            self.explore(n, visited)
        return True

    def generate_graph(self):                           # O(M+N)
        graph = {}
        for airport in airports:                        # O(M)
            if airport not in graph.keys():
                graph[airport] = []
        
        for flight in self.flights:                     # O(N)
            src = flight[0]
            des = flight[1]
            if src in graph.keys():
                graph[src].append(des)
        
        return graph

s = Solution(airports, routes, startingAirport)
pass