# Rozpis cvičení

| no | obsah    | tema        |
|-------|--------------------------------------------------------|--------------------|
| cv 01 | REPL, Jednoduchá aplikace pro analýzu databáze osob    | csv; soubor        |
| cv 02 | Aplikace pro analýzu dat z prodejen obchodního řetězce | dist; set          |
| cv 03 | Experimenty s datovými strukturami a jejich rychlostmi | úpravy předchozích |
| cv 04 | __ZÁPOČET 1__                                          |                    |
| cv 05 | Framework pro simulaci systému hromadné obsluhy        | SHO                |
| cv 06 | Sudoku                                                 | Backtracking       |
| cv 07 | Playlist na párty                                      | Knapsack           |
| cv 08 | __ZÁPOČET 2__                                          |                    |
| cv 09 | Nejkratší cesta                                        | Dijkstra           |
| cv 10 | Kostra grafu                                           | Prim-Jarník        |
| cv 11 | Město Plzeň, české železnice                           |                    |
| cv 12 | __ZÁPOČET 3__                                          |                    |
| cv 13 | Ukázka distribuce funkčního SW, REZERVA                |                    |

https://github.com/JakubSido/example_package


# Podpůrné materiály: 
- na konci každého cvičení doporučujeme, jak lze práci rozšiřovat (dobrá příprava na zápočet)
## Obecně python
- https://www.w3schools.com/python

## Jak psát čitelný a dobře udržitelný kód? 
Pyhton dává programátorovi velkou volnost. S velkou sílou přichází však i velká zodpovědnost. Pokud vám záleží na tom, aby po vás byl kód čitelný, pro ostatní přehledný a dobře udržitelný, doporučujeme pročíst si [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)


# Chybovník
## Chyby neslučitelné se získáním zápočtu
1. Plagiátorství
2. Porušení pravidel nastavených pro vypracování úloh. 

## Velmi závažné chyby: jsou důvodem k dalšímu nehodnocení práce
1. Nevalidní kód
    - Odevzdané zdrojové kódy nejsou validním kódem v jazyce Python - znemožňují spuštění programu.   

2. Program nelze spustit dle specifikace z jiného důvodu. Například: 
    - chybí importy, 
    - program nepracuje s argumenty předanými z příkazové řádky.

3. Program havaruje 
    - Program havaruje na neošetřené výjimce (např. dělení nulou, index out of range, ...)

4. Program nedoběhne během vyhrazeného času. 
    - Program obsahuje nekonečnou smyčku, nebo je řádově pomalejší než by měl být například v důsledku neefektivního algoritmu. 


## Závažné chyby: mohou být důvodem ke znemožnění hodnocení nebo snížení bodového ohodnocení části vaší práce.

1. Data jsou načtena pouze částečně nebo ve formátu, který neodpovídá zadání.
2. Program řeší zadanou úlohu nekompletně, nebo řešení neodpovídá očekávanému výstupu. 
3. Špatná dekompozice řešení.     
4. Neošetřený vstup programu (např. chybějící kontrola parametrů předaných z příkazové řádky).
5. Málo obecný algoritmus. 
    - program funguje pouze na konkrétních vstupech a není dobře přenositelný. 
6. Špatná práce s cestami k souborům nebo složkám, která vede na nemožnost spuštění programu na jiném počítači, s jinými daty nebo v jiném adresáři.
7. Program pracuje špatně při volání funkcí.  
    - například nepoužívá návratové hodnoty
    - namísto předaných parametrů používá globální proměnné