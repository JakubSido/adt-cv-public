# Experimenty s kolekcemi v pythonu: Měření času

V předchozích dvou cvičení jsme si mohli vyzkoušet základní práci s daty. Pracovali jsme s celkem velkou datovou sadou a mohli jsme narážet na limity rychlosti při výkonu některých operací.

V dnešním cvičení si vyzkoušíme změřit a porovnat některé klíčové operace se základními kolekcemi.

# 1. Experimenty s list,set
Implementujte experiment demonstrující rychlost operace nad datovými strukturami.
Změřte průběh rychlosti operace IN pro list,set,dict



1. Ve funkci `experiment_with_operations()` vytvořme list, který obsahuje výčet čísel z intervalu _0, COLLECTION_SIZE_

2. Implementujme funkci, která přijme seznam nebo množinu a ověří přítomnost náhodného čísla v rozsahu. Použijme operátor pythonu `in`, který je implementovaný pro všechny základní kolekce. Pro ověření, můžeme přidat ladící výpis. Můžeme otestovat správnost implementace. 

```python
def test_operation_in(collection: list|set)
```

3. Připravme funkci, která přijme kolekci k otestování a spustí nad ní několik testů funkce, která je také předána jako parametr. Použijme balík timeit, který za nás řeší spoustu problémů, které se pojí s měřením času běhu funkce nebo kusu programu. 

```python
def test_collection(our_collection: list|set, test_function: Callable) -> float
```

4. Vše spojíme dohromady a otestujeme rychlost operace `in` nad naším listem. 

5. Přidáme smyčku, která postupně vyrobí listy rostoucí velikosti a změříme časy pro rozdílné velikosti abychom zachytili trend. 

6. Použijme knihovnu plotly.express pro vizualizaci našich zjištění.  

7. Přidejme měření stejné operace pro množinu (set) a přidejme do obrázku

### Diskutujme
Jak by to dopadlo, pokud bychom nehledali náhodný prvek, ale ten, který je:
 - první ,
 - poslední,
 - prostřední. 


# 2. Experimenty s přepravkou
8. Implementujme přepravku pro reprezentaci obdélníku (a, b).
```python 
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
```
9. Vytvořte funkci `experiment_eq_and_hash()` která bude  implementovat následující experiment:
10. Vytvořme seznam obdélníků. 
11. Vytvořme další obdélník X se stejnými atributy. 
12. Vyzkoušejme obdélník X najít pomocí operace `in`

### Diskutujme
Co bychom museli udělat, abychom mohli použivat všech výhod pro vlastní implementaci přepravky?



12. Implementujme do třídy Rectangle metodu `__eq__`. Jak kritická je efektivita kódu v této metodě? 

13. Vyzkoušejme zaměnit incializaci seznamu původně čísel, za seznam instancí třídy Rectangle
14. Implementujme třídě Rectangle metodu `__hash__`


# Diskuze 

1. Co ovlivní, jak moc je vyhledávání v množině závislé na *n*? 

# Další Experimenty 
- Vyzkoušejte změrit i rychlost a závislost jiných operací nad stukturou list a set. Např:
    - odstranit náhodný prvek (i ve variantě, že je v listu na pozici 0)
    - Ověřte složitost přidání dalšího prvku do kolekce. 

- Pro list porovnejte přidání na konec vs. přidání na začátek

# K zamyšlení
Proč hledání v listu je dle dokumentace O(n)? neumíme to rychleji? 

