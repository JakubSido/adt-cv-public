# Framework pro simulaci systému hromadné obsluhy & Objektové programování

# Úvodem
Systém hromadné obsluhy(SHO) umožňuje modelovat opakující se sekvenci operací.
Výskyt událostí je náhodný.
Cílem modelování takových systémů je lepší porozumění a zlepšení činnosti systému. Simulace
umožňuje nastavovat parametry a sledovat dopad na systém jako celek.
Jednoduché simulátory SHO lze realizovat pomocí front a aktivních prvků obsluhující požadavky
ve frontách.



1. Pro reprezentaci prvku v SHO použijte celé číslo – identifikátor.
2. Implementujte třídu class NamedQueue, která bude představovat frontu v systému hromadné obsluhy. Pro samotnou realizaci fronty použijte collections.deque, navíc umožněte každou frontu pojmenovat.
NamedQueue obsahuje collection.queue jako nedílnou součást. Navíc má jméno.

```python
class NamedQueue:
    def __init__(self, name:str):
```


3. Implementujte třídu class ProcessingNode, která bude představovat aktivní prvek v systému hromadné obsluhy. 

Konstruktor bude přijímat 
- zdroj (odkud bere) 
- destinaci (kam dává),
- množství (kolik jednotek zpracuje najednou).
- Čas doby obsluhy odpovídá normálnímu rozdělení se střední hodnotou μ a směrodatnou odchylkou σ

```python
class ProcessingNode:
    def __init__(self, name:str, period: int, source: NamedQueue, destination: NamedQueue, amount=1, sigma=0.1):
```
4. Implementujte metodu 
```python
def perform() -> None 
```
která provede přeřazení _n_ prvků ze zdroje do destinace.

5. Imlementujte metodu 
```python
def schedule_next_occurr() -> None
```
která provede nastavení instanční proměnné remaining_time (počet tiků do dalšího výskytu události). Pro generování použijte funkci random.gaus(mu,sigma)

6. Implementujte metodu 
```python
def tick() -> None
```
která sníží čítač zbývajícího času. Pokud čas vyprší provede obsluhu a naplánuje další výskyt obsluhy.

7. Ve funkci main implementujte jednoduchou smyčku, která bude iterovat vteřinami ve dni. S každou
iterací na všech instancích třídy class ProcessingNode zavolá metodu `tick()`




8. Vytvořme jednoduchý simulátor prodejny obchodního řetězce. Simulace bude tvořit podobná data, se kterými jsme pracovali na dřívějším cvičení.
Tentokrát nad systémem však získáme plnou kontrolu, budeme moci upravovat a přidávat události, které chceme simulovat. 
- pro jednoduchost začneme pouze s modelem kde: 
    - člověk přijde do prodejny, 
    - zváží si zeleninu - vždy :-) , 
    - zaplatí u finální pokladny a odejde. 

9. Implementujte třídu Observer, který ve svém konstruktoru přijme seznam front, které má sledovat.
```python
class Observer:
    def __init__(self, list_to_observe):
```

10. Implementujte metodu do třídy Observer, která vypíše stav všech sledovaných front do terminálu například v tomto formátu:
```
in_the_streets(943)->shop_gate(0)->vege_queue(0)->final_cr(2)->done(55)
in_the_streets(942)->shop_gate(0)->vege_queue(0)->final_cr(2)->done(56)
in_the_streets(941)->shop_gate(0)->vege_queue(0)->final_cr(2)->done(57)
```

```python
def take_snapshot(self):
```

11. Zařiďte, aby se metoda _take_snapshot()_ zavolala každou minutu simulovaného času.


# Závěrem
Obdobným způsobem je možné modelovat chování celé řady systémů:
- Doprava ve městech, kdy obslužné prvky jsou křižovatky a prvky putující systémem jsou dopravní prostředky přepravující lidi.
- Cestování a směrování packetů v počítačových sítích.



# Další cvičení
1. Upravte implementaci třídy ProcessingNode tak, aby umožnila místo jedné destinace přidat celý list destinací. V případe, kdy aktivní prvek zpracuje požadavek, umístí jej náhodně do jedné z cílových destinací.
```python
class ProcessingNode:
    def __init__(self, name:str, period: int, source: NamedQueue, destinations: list[NamedQueue], amount=1, sigma=0.1):
```

2. Upravte implementaci tak, aby kromě seznamu možných destinací vstupoval nepovinný parametr který bude ošetřídit distribuci zpracovávaných požadavků do jednotlivých destinací. Pro jednoduchost můžeme uvažovat, že seznam všech možných destinací a distribuce je vždy stejně dlouhý. Parametr dist_ratio bude tedy seznam celých čísel, které budou vyjadřovat poměr, ve kterém se budou prvky rozdělovat do příslušných front. Pokud bude bude hodnota dist_ratio=None, bude distribuce rovnoměrná.
```python
class ProcessingNode:
    def __init__(self, name:str, period: int, source: NamedQueue, destinations: list[NamedQueue], amount=1, sigma=0.1, dist_ratio:None|list[int] = None):
```

3. Přidejte implementaci, která umožní zpětně pro každý prvek, který prošel systémem hromadné obsluhy získat záznam jeho putování. pozn. Připravte třídu pro prvek, který bude obsahovat seznam, ve kterém bude vždy (čas, obslužný_bod). 
```python
class Item:
    def __init__(self, id):
        self.id = id
        self.history = []
```
4. Upravte realizaci prodejny tak, aby modelovala prodejnu, která se chová obdobným způsobem jako jsme zjistili v analýze dat na dřívejším cvičení. 
    - Přidejte pult s masem a váhu na ovoce
    - Zákazník po příchodu do obchodu jde s pravděpodobností 40% nakupovat zeleninu
    - Přidejte větší počet cílových pokladen. 
    - Modelujte chování v odpolední špičce, kdy v 15:00 větší množství lidí odchází z práce a jde nakupovat. 
    - Z předchozího cvičení víte, jak vykreslit data do grafu, jste tedy schopní přímo vykreslit stav fronty v kterýkoli čas simulace.


