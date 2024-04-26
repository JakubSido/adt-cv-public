# pipem nainstalovat
# https://github.com/JakubSido/adthelpers

# pip install git+https://github.com/JakubSido/adthelpers
# nebo stáhnout zip a instalovat jako pip install <cesta_k_rozbalenému_zipu>

import json
import adthelpers

from queue import PriorityQueue

class Node:
    def __init__(self, id) -> None:
        self.id: int = id  # identifikátor uzlu
        self.neighbors: list[tuple[float, Node]] = list()  # (váha hrany, (kam_se_dostanu))


class Graph:
    def __init__(self) -> None:
        self.nodes: dict[int, Node] = dict()
        self.edges: set = set()
        
    def __add_node(self, node: Node):
        self.nodes[node.id] = node          

    def __add_edge(self, src: Node, dst: Node, weight: float = 0):
        src.neighbors.append((weight, dst))
        dst.neighbors.append((weight, src))
        self.edges.add((weight, src, dst))
        
    def create_edge(self, src_id: int, dst_id: int, weight: float = 0):
        if src_id not in self.nodes:
            src_node = Node(src_id)
            self.__add_node(src_node)
        if dst_id not in self.nodes:
            dst_node = Node(dst_id)
            self.__add_node(dst_node)

        self.__add_edge(self.nodes[src_id], self.nodes[dst_id], weight)
        

def load_graph(filepath: str) -> Graph:
    graph = Graph()
    with open(filepath, "r", encoding="utf8") as fd:
        file_string = fd.read()
        js = json.loads(file_string)
        
        for e in js["links"]:
            graph.create_edge(e["source"], e["target"], e["weight"])
    return graph
    

def find_spanning_tree(graph: Graph) -> set[tuple[int, int]]:
    q: PriorityQueue = PriorityQueue()

    # TODO Implementujte Prim-Jarníkův algoritmus pro nalezení minimální kostry
    spanning_tree: set[tuple[int, int]] = set()
    closed: set[int] = set()
    
    # pro ucely vizualizace
    painter = adthelpers.painter.Painter(
        graph,
        visible=q,
        closed=closed,
        color_edges=spanning_tree,
    )

    next_item = (0.0, (-1, 0))  # (váha hrany, (odkud_id, kam_id))
    q.put(next_item)

    actual_node = None
    while q.qsize() > 0:  ## pokud sem umístíme breakpoint, můžeme sledovat jak se algoritmus vyvíjí
        
        # vyberu hranu s nejmenším ohodnocením, o to se stará prioritní fronta. Ohodnocení samotné (první část) 
        # už nepotřebujeme používá se pro účely prioritní fronty (řazení). Dále pracujeme jen s hranou (druhá část)
        # Tato hrana je dobrý kandidát na přidání do kostry.
        _, edge = q.get()  
        from_id, actual_id = edge
        actual_node = graph.nodes[actual_id]

        # Pokud je uzel na konci uvažované hrany už zpracovaný - objevený odjinud dříve (přístupný z kostry),
        # zahazuji ji a beru si další. V opačném případě bych vytvořil cyklus v grafu a kostru si poničil. 
        if actual_id in closed:
            continue
        
        # Hranu přidám do kostry
        spanning_tree.add(edge)

        # přidám všechny nově objevené hrany do fronty
        for weight, to_id in actual_node.neighbors:
            next_item = (weight, (actual_node.id, to_id.id))
            q.put(next_item)
            
        painter.draw_graph(actual_node)  # vizualizace, pro krokování algoritmu je vhodné mít breakpoint zde

        closed.add(actual_id)  # uzel je zpracovaný

    return spanning_tree
    

def main():
    graph = load_graph("data/graph_grid_s3_3.json")
    painter = adthelpers.painter.Painter(graph)
    painter.draw_graph()
    input("Graph loaded. Press Enter to find spanning tree...")

    find_spanning_tree(graph)
    input("Press enter to exit program...")


if __name__ == "__main__":
    main()