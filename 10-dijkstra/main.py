import numpy as np
import geopy.distance
from tqdm import tqdm

import plotly.express as px  ##COMMENT##

from spanning import Graph

# https://www.linode.com/docs/guides/python-priority-queue/
from queue import PriorityQueue

# https://github.com/JakubSido/adthelpers
# pip install git+https://github.com/JakubSido/adthelpers
from adthelpers.painter import Painter


# id,WKT
def load_nodes(filename: str) -> dict[int, tuple[float, float]]:
    """Načte informaci o uzlech z csv souboru a vrátí slovník id uzlu a jeho gps souřadnic
    Args:
        filename str: _description_

    Returns:
        Dict[int, tuple[float,float]]: _description_
    """
    node_map: dict[int, tuple[float, float]] = dict()
    return node_map


def load_edges(filename, load_first=0) -> Graph:
    graph: Graph = Graph()
    return graph


def calculate_distance(list_of_coordinates: list[tuple[float, float]]) -> float:
    """Vypočítá délku cesty mezi body v listu souřadnic

    Args:
        list_of_coordinates (list[tuple[float, float]]): seznam souřadnic (lat, long)

    Returns:
        float: vzdálenost v metrech mezi body
    """
    return 0


def show_path(
    predecessors: dict[int, int], start_id: int, end_id: int, nodes: dict[int, tuple[float, float]] | None = None
):
    """Funkce pro zobrazení nalezené cesty. V případě jednoduchého grafu lze použít pouze textový výstup (např. 0 -> 1 -> 4 -> 5) .
     V případě GPS dat je možné zobrazit trasu na mapě pomocí plotly express (viz readme).

    Args:
        predecessors (dict[int, int]): zpětné ukazatele pro rekonstrukci cesty
        start_id (int): startovní uzel
        end_id (int): cílový uzel
        nodes (dict[int, tuple[float, float]] | None, optional): metadata uzlů. Výsledek funkce load_nodes.
    """


def find_path_dijkstra(graph: Graph, start_id: int, end_id: int, paint=False, verbose=1):
    priority_queue = PriorityQueue()

    closed: set[int] = set()  # starší verze adthelpers painter počítá s Node -- novější umí vizualizovat i int
    distances: dict[int, float] = dict()
    predecessors: dict[int, int] = dict()

    painter = None
    if paint:
        painter = Painter(graph, priority_queue, closed, None, distances=distances)

    return predecessors, distances


def main():
    import spanning

    # umělý graf
    graph = spanning.load_graph("graph_grid_s3_3.json")
    painter = Painter(graph)
    painter.draw_graph()

    start = 0
    end = 5
    paint = True
    predecessors, distances = find_path_dijkstra(graph, start, end, paint=paint)
    show_path(predecessors, start, end)

    input("Press Enter to continue...")
    # graf města Plzně

    # LOBZY # 372,"POINT(13.4079837944859 49.7353302487858)"
    # SADY 4729,"POINT(13.3745807748411 49.7495249505102)"
    # ZBUCH 4569,"POINT(13.2272145436097 49.6782129992438)"
    # HRADEK 4651,"POINT(13.4449402230356 49.7548605123502)"
    # start = "4651"

    graph = load_edges(r"plzen/pilsen_edges.csv")
    nodes = load_nodes(r"plzen/pilsen_nodes.csv")
    start = 4651
    end = 4569
    paint = False
    predecessors, distances = find_path_dijkstra(graph, start, end, paint=paint, verbose=0)
    show_path(predecessors, start, end, nodes=nodes)


if __name__ == "__main__":
    main()