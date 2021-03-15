
from __future__ import annotations

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: dict, start: str) -> set[str]:

    explored = {start}
    queue = [start]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.append(w)
    return explored


if __name__ == "__main__":
    print(breadth_first_search(G, "A"))
