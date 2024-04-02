

import collections
import random



class NamedQueue:
    def __init__(self, name:str):
        self.name = name
        self.q = collections.deque()


class ProcessingNode:
    def __init__(self, name:str, period: int, source: NamedQueue, destination: NamedQueue, amount=1, sigma=0.1):

        self.name = name
        self.period = period
        self.sigma = period * sigma

        self.source = source
        self.destination = destination

        self.remaining_time = 0
        self.amount = int(amount)

        self.period = period

    def perform(self):
        if len(self.source.q) > 0:
            for _ in range(self.amount):
                if len(self.source.q) > 0:
                    item = self.source.q.popleft()

                    self.destination.q.append(item)

class Observer:
    def __init__(self, list_to_observe):
        self.list_to_observe = list_to_observe
        self.history = collections.defaultdict(lambda: list())

    def take_snapshot(self):
        state_strings = []
        for named_queue in self.list_to_observe:
            state_strings.append(f"{named_queue.name}({len(named_queue.q)})")

        return "->".join(state_strings)
        

def next_ocur_in(mu, s):
    return int(random.gauss(mu, s))


def main():
    pass
            
    people_number = 1000
    people_in_the_city = collections.deque([i for i in range(people_number)])

    # vytvoříme "frontu" která bude reprezentovat lidi chodící po městě
    street_q = NamedQueue(f"in_the_streets")
    street_q.q = people_in_the_city

    # vytvoříme fronty pro jednotlivé obslužné prvky v obchodě
    gate_keeper_q = NamedQueue(f"shop_gate")
    vege_q = NamedQueue(f"vege_queue")
    cr_q = NamedQueue(f"final_cr")

    # frontu lidí, co už z obchodu odešli 
    done_q = NamedQueue(f"done")

    FINAL_M = 2 * 60  # střední hodnota doby obsluhy na pokladně
    VEGE_M = 10 # střední hodnota doby obsluhy na váze se zeleninou

    usual_day = ProcessingNode("usual_day_generator", (1 * 60) * 1 , street_q, gate_keeper_q, 1)
    gate_keeper_node = ProcessingNode(f"gate_keeper", 0, gate_keeper_q, vege_q, 1)
    vege_cr = ProcessingNode(f"vege_1", VEGE_M, vege_q, cr_q, 1)
    crs = ProcessingNode(f"final_crs_1", FINAL_M, cr_q, done_q, 1)
        
    to_tick = [crs, vege_cr, gate_keeper_node, usual_day]

    observer = Observer([street_q,gate_keeper_q,vege_q,cr_q,done_q])
    for time in range(2 * 60 * 60):
        for te in to_tick:
            if te.remaining_time is None:
                te.remaining_time = next_ocur_in(te.period, te.sigma)
                continue
            te.remaining_time -= 1

            if te.remaining_time <= 0: 
                te.remaining_time = next_ocur_in(te.period, te.sigma)
                te.perform()
        
        if time % (10)== 0:
            snpsht = observer.take_snapshot()
            h = time // (60*60)
            m = (time % (60*60)) // 60
            s = time % 60
            print(f"{h:02d}:{m:02d}:{s:02d}\t{snpsht}")
    
            

if __name__ == '__main__':
    main()

