import heapq
from typing import Dict, Hashable, List, Tuple, Optional


class Graph:
    def __init__(self):
        self._adj: Dict[Hashable, List[Tuple[Hashable, float]]] = {}

    def add_edge(self, u, v, w: float, undirected: bool = False):
        self._adj.setdefault(u, []).append((v, w))
        if undirected:
            self._adj.setdefault(v, []).append((u, w))

    def dijkstra(self, start) -> Tuple[Dict[Hashable, float], Dict[Hashable, Optional[Hashable]]]:
        dist: Dict[Hashable, float] = {node: float("inf") for node in self._adj}
        prev: Dict[Hashable, Optional[Hashable]] = {node: None for node in self._adj}

        dist[start] = 0.0
        heap: List[Tuple[float, Hashable]] = [(0.0, start)]
        visited = set()

        while heap:
            current_dist, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)

            for v, weight in self._adj.get(u, []):
                new_dist = current_dist + weight
                if new_dist < dist.get(v, float("inf")):
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(heap, (new_dist, v))

        return dist, prev

    def shortest_path(self, start, target):
        dist, prev = self.dijkstra(start)
        if dist.get(target, float("inf")) == float("inf"):
            return None

        path = []
        current = target
        while current is not None:
            path.append(current)
            current = prev[current]
        path.reverse()
        return path, dist[target]


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B", 1, undirected=True)
    graph.add_edge("B", "C", 2, undirected=True)
    graph.add_edge("A", "C", 5, undirected=True)
    graph.add_edge("C", "D", 1, undirected=True)
    graph.add_edge("B", "D", 4, undirected=True)

    path, distance = graph.shortest_path("A", "D")
    print("Найкоротший шлях A → D:", path)
    print("Довжина шляху:", distance)