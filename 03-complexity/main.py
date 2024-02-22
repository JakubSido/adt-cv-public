from dataclasses import dataclass
import random
import timeit
from typing import Callable
import plotly.express as px

COLLECTION_SIZE = 100000
N_TESTS = 100  # Number of test runs


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
def test_operation_in(collection: list|set):
    rand = random.randint(0,len(collection))
    # TODO doplňte testování, zda je náhodně vybraný prvek v kolekci

def test_collection(our_collection: list|set ,test_function: Callable):
    elapsed_in = 0.0
    # TODO dopolňte měření času pro testovací funkci pomocí timeit

    return elapsed_in


def experiment_eq_and_hash():
    rectangles = list()
    # TODO naplňte list několika obdélníky. Následně vytvořte nový obdélník, který má stejné parametry jako některý z obdélníků v listu a zjistěte, zda je v listu pomocí operátori in

def experiment_with_operations():
    # pro vizualizaci výsledků
    structure_sizes = list()
    times = list()
    structure_types = list()

    # TODO doplňte měření času pro list a set pro různé velikosti kolekcí (krok po 10 % velikosti COLLECTION_SIZE), uložte si výsledky a poté je vizualizujte

    # vizualizace výsledků
    plot_data = {
                'Structure size': structure_sizes, # osa x - velikost kolekce
                 'Time': times,                   # osa y - časy
                 'Data Structure':  structure_types     # typ kolekce (list/set) pro barevné rozlišení
                }

    fig = px.line(plot_data, x='Structure size', y='Time', color='Data Structure',
                 title='Time Comparison of List vs Set Operations')
    fig.show()
    


if __name__ == "__main__":
    experiment_with_operations()
    # experiment_eq_and_hash()
