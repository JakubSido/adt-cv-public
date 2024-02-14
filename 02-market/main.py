from collections import defaultdict
import os
import sys

class Record():
    def __init__(self,time:int ,id_cost: int,ckpt:str) -> None:
        self.time = time
        self.id_cost = id_cost
        self.ckpt = ckpt
    


def load_data(datapath:str ,city:str ,shop:str) -> dict[str, list[Record]]:
    #doporučujeme jako klíč použít název checkpointu 

    city_data = defaultdict(lambda: list())
    print("loading", city)

    return city_data 


def get_passed_set(data : dict[str, list[Record]],key_words:list[str]) -> set[int]:
    costumers = set()
    return costumers
            

def filter_data_time(data :dict[str, list[Record]], cond_time:int) -> dict[str, list[Record]]:
    ret = defaultdict(lambda: list())
    return ret
         
def get_q_size(data :dict[str, list[Record]], seconds:int) -> int:   
    queue = set()   
    return len(queue)
    

def histogram(data :dict[str, list[Record]]):
    pass

def main(datadir):
    
    data = None

if __name__ == "__main__":
    datadir = ""
    main(datadir)
