import os
import geopy.distance
from tqdm import tqdm
import plotly.express as px

import spanning as spanning

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
    
    with open(filename, "r", encoding="utf8") as fd:
        for i, line in enumerate(fd):
            if i == 0:
                continue
            line = line.replace("\n", "")
            line = line.split(',"POINT(')
            id = int(line[0])
            lat, long = line[1].replace(')"', "").split(" ")
            node_map[id] = (float(long), float(lat))
    
    return node_map


def load_edges(filename, load_first=0) -> spanning.Graph:
    graph: spanning.Graph = spanning.Graph()
    
    with open(filename, "r", encoding="utf8") as fd:
        for i, line in tqdm(enumerate(fd)):
            if i == 0:
                continue
            if i == load_first:
                break
            line = line.strip()
            if line.startswith("#"):
                continue
            if line == "":
                continue
            fields, path = line.split("LINESTRING(")

            fields = line.split(",")
            s, t = int(fields[1]), int(fields[2])
            path = path.replace('"', "")
            path = path.replace(")", "").split(",")
            path = [p.split(" ") for p in path]
            unpacked = [(float(lat), float(long)) for long, lat in path]
            w = calculate_distance(unpacked)

            graph.add_edge_id(s, t, weight=w)
    
    return graph


def calculate_distance(list_of_coordinates: list[tuple[float, float]]) -> float:
    """Vypočítá délku cesty mezi body v listu souřadnic

    Args:
        list_of_coordinates (list[tuple[float, float]]): seznam souřadnic (lat, long)

    Returns:
        float: vzdálenost v metrech mezi body
    """
    
    last = None
    sum = 0
    for current in list_of_coordinates:
        if last is None:
            last = current
            continue
        dist = geopy.distance.geodesic(last, current)
        sum += dist.m
        last = current

    return sum
    
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
    
    path = []
    current = end_id
    while current != start_id:
        path.append(current)
        current = predecessors[current]
    path.append(start_id)
    path.reverse()
    print(" -> ".join([str(x) for x in path]))

    if nodes:
        lats = [la for la, lo in [nodes[p] for p in path]]
        lons = [lo for la, lo in [nodes[p] for p in path]]

        fig = px.line_mapbox(lat=lats, lon=lons, mapbox_style="open-street-map", zoom=12)
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_center_lat=49.747)
        fig.show()
    


def find_path_dijkstra(graph: spanning.Graph, start_id: int, end_id: int, paint=False, verbose=1):
    priority_queue = PriorityQueue()

    closed: set[int] = set()  # starší verze adthelpers painter počítá s Node -- novější umí vizualizovat i int
    distances: dict[int, float] = dict()
    predecessors: dict[int, int] = dict()

    painter = None
    if paint:
        painter = Painter(graph, priority_queue, closed, None, distances=distances)

    

    # Inicializuji vzdálenosti a zpětné ukazatele
    for n in graph.nodes:
        distances[n] = float("inf")
        predecessors[n] = -1

    # Přidám startovní uzel do fronty, tím nastartujeme algoritmus
    priority_queue.put((0, (-1, start_id)))
    distances[start_id] = 0

    # dokud mám co zpracovávat
    while priority_queue.qsize() > 0:
        if verbose > 0:
            print("q size: ", priority_queue.qsize())
            print("visible: ", priority_queue.queue)
            print("closed : ", closed)

        # vyberu další uzel, ze kterého budu objevovat z prioritní fronty
        distance, edge = priority_queue.get()
        from_id, active_id = edge
        active_node = graph.nodes[active_id]

        # pokud jsem v cílovém uzlu, končím algoritmus, cesta byla nalezena
        if active_node.id == end_id:
            break

        # zavřené uzly sice do fronty nedávám, ale mohou se uzavřít během toho, co čekají ve frontě
        if active_node in closed:
            if verbose > 0:
                print(f"{active_node} už je zavřený")
            continue

        # kam všude vidím z aktivního uzlu?
        for weight, to in active_node.neighbors:
            to_id = to.id

            # už zavřené přeskakuji
            if to_id in closed:
                if verbose > 0:
                    print(f"{to_id} uz je zavrene")
                continue

            # pokud jsem našel zkratku, aktualizuji vzdálenost a zpětný ukazatel
            new_distance = distances[active_node.id] + weight
            if new_distance < distances[to_id]:
                if verbose > 0:
                    print("found shortcut from ", active_node, " to ", to_id, distances[to_id], "->", new_distance)
                distances[to_id] = new_distance
                predecessors[to_id] = active_node.id

                # do fronty přidám možný uzel s potenciální vzdáleností
                # pro vizualizaci je nutné dodržet tuto strukturu  (váha, (odkud_id, kam_id))
                priority_queue.put((distances[active_node.id] + weight, (active_node.id, to_id)))

        # uzavřu aktivní uzel
        closed.add(active_id)

        if painter:
            painter.draw_graph(active_node)
    
    return predecessors, distances


def demo():
    # umělý graf
    graph = spanning.load_graph("graph_grid_s3_3.json")
    painter = Painter(graph)
    painter.draw_graph()

    start = 0
    end = 5
    paint = True
    predecessors, distances = find_path_dijkstra(graph, start, end, paint=paint)
    show_path(predecessors, start, end)


def city_map(datadir):
    # graf města Plzně
    # LOBZY # 372,"POINT(13.4079837944859 49.7353302487858)"
    # SADY 4729,"POINT(13.3745807748411 49.7495249505102)"
    # ZBUCH 4569,"POINT(13.2272145436097 49.6782129992438)"
    # HRADEK 4651,"POINT(13.4449402230356 49.7548605123502)"
    # start = "4651"

    graph = load_edges(os.path.join(datadir, "pilsen_edges.csv"))
    nodes = load_nodes(os.path.join(datadir, "pilsen_nodes.csv"))
    start = 4651
    end = 4569
    paint = False
    predecessors, distances = find_path_dijkstra(graph, start, end, paint=paint, verbose=0)
    show_path(predecessors, start, end, nodes=nodes)


def main():

    demo()
    input("Press Enter to continue...")

    city_map("plzen")
    input("Press Enter to continue...")


if __name__ == "__main__":
    main()

