from collections import defaultdict
import os
import sys



class Record():
    def __init__(self,time:int ,id_cost: int,ckpt:str) -> None:
        self.time = time
        self.id_cost = id_cost
        self.ckpt = ckpt
    
    
    def __repr__(self) -> str:
        return f"id:{self.id_cost} time:{self.time}"
    


def load_data(datapath:str ,city:str ,shop:str, day="1-Mon") -> dict[str, list[Record]]|None:

    city_data = defaultdict(lambda: list())
    print("loading", city)

    
    shop_path = os.path.join(datapath, city, day, f"{shop}.txt")
    if not os.path.exists(shop_path):
        print("soubor neexistuje", shop_path)
        return None
    
    with open(shop_path, 'r', encoding="utf8") as fd:
        fd.readline()

        lines = fd.readlines()
        for line in lines:
            line = line.replace("\n", "")
            
            spl = line.split(";")
            try:
                r = Record(int(spl[0]),int(spl[2]),spl[1])
                key = f"{r.ckpt}"
                city_data[key].append(r)
            except ValueError as e:
                print("chyba v souboru ValueError neocekavana hodnota",shop_path,"\n",line)
                continue
            except IndexError as e:
                print("chyba v souboru IndexError neocekavany pocet hodnot",shop_path,"\n",line)
                continue
    
    return city_data 


def get_passed_set(data : dict[str, list[Record]],key_words:list[str]) -> set[int]:
    costumers = set()
    
    for k,d in data.items():
        d_ckpt_gen = k.split("_")[0] 
        if d_ckpt_gen in key_words:
            for r in d:
                costumers.add(r.id_cost) 
    
    return costumers
            

def filter_data_time(data :dict[str, list[Record]], cond_time:int) -> dict[str, list[Record]]:
    ret = defaultdict(lambda: list())
    
    for k,v in data.items():
        for r in v:
            if int(r.time) > cond_time:
                break 
            ret[k].append(r)
    
    return ret
         
def get_q_size(data :dict[str, list[Record]], seconds:int) -> int:   
    queue = set()   
    
    filtered_data = filter_data_time(data,seconds)
        
    key_words = ["vege","frui","meat"]
    first = get_passed_set(filtered_data,key_words)
    
    key_words = ["final-crs"]
    second = get_passed_set(filtered_data,key_words)

    queue = first.difference(second)
    
    return len(queue)
    

def histogram(data :dict[str, list[Record]]):
    pass
    
    
    for m in range(0,24*60,10):
        seconds = m*60

        q_size = get_q_size(data,seconds)

        h = m // 60
        mi = m % 60
        print(f"{h}:{mi} -- {q_size}  ")
    

def main(datadir):
    
    data = None
    
    while True:
        city = input("Zadejte město (např Plzeň): ")
        shop = input("Zadejte obchod: (např shop_a): ")
        data = load_data(datadir, city,shop)
        if data is None:
            print("zadna data nebyla nactena")
            continue
        histogram(data)
    

if __name__ == "__main__":
    datadir = ""
    
    argv = sys.argv
    if len(argv) < 2:
        print("Usage: python main.py <data_dir>")
        exit(1)   
    
    datadir = argv[1]

    if not os.path.exists(datadir):
        print("složka z daty neexistuje")
    
    
    main(datadir)
