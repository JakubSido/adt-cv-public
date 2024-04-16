# pipem nainstalovat
# https://github.com/JakubSido/adthelpers
# pip install git+https://github.com/JakubSido/adthelpers
import json
import adthelpers

from queue import PriorityQueue


class Node:
    def __init__(self, id) -> None:
        # TODO 1
        pass
        self.id: int = id  # identifikátor uzlu
        self.neighbors: list[tuple[float, Node]] = list()  # (váha hrany, (kam_se_dostanu))


class Graph:
    def __init__(self) -> None:
        # TODO 2
        pass

    def add_node(self, node: Node):
        # TODO 3
        pass

    def add_edge(self, src: Node, dst: Node, weight=0):
        # TODO 4
        pass


def load_graph(filepath: str) -> Graph:
    # TODO 5
    return None


def main():

    graph = load_graph("data/graph_grid_s3_3.json")
    painter = adthelpers.painter.Painter(graph)
    painter.draw_graph()
    input("Press Enter to continue...")



if __name__ == "__main__":
    main()
    input("Press Enter to continue...") 


