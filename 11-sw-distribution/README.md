# Ukázka distribuce Software v pythonu

Jedním z nejrozumnějších způsobů, jak někomu předat výsledek naší programátorské práce je vytvořit balíček.
Tento balíček se dá snadno nainstalovat na jiném zařízení, obsahuje závislosti, příklady užití, návody, testy....
Také má jasně definované vstupní body a rozhraní pro jeho uživatele.

Není ale vůbec od věci vlastní projekty, které chceme uchovat pro vlastní pozdější použití, archivovat stejným způsobem. Vyhneme se tak nepříjemným vstupním investicím po tom, co zapomeneme jak to vlastně všechno fungovalo.

Pro účely ADT a vaše další působení jsme připravili minimalistický example package, který můžete použít ve svých semestrálních pracích nebo jako výchozí bod k jakémukoli kusu software, který budete v budoucnu připravovat v pythonu.

Sami jej aktivně používáme. To má několik důsledků:
    + budete vždy pracovat s nejnovějším doporučeným postupem pro přípravu balíčků
    - může se stát, že se objeví nějaká novinka, které nebudete rozumět. Pokusíme se této variantě co nejvíce vyhýbat. V případě, že taková věc nastane, ji řádně popíšeme v README.

Dopad této šablony sahá i za hranice předmětu ADT, tedy se zde objevují věci jako jsou například testy, které jsou nedílnou součástí každého rozumného kusu SW.


Vzorové repo
[https://github.com/JakubSido/example_package](https://github.com/JakubSido/example_package)



# Cvičení s balíčkem

1. Seznamte se se strukturou balíčku
    - složka src/example_package
        - `internal_counts.py` 
        - `counts.py`
        - `cli.py` (Command line interface)
        - `__init__.py`
    
    - README.md + /img
    - `pyproject.toml`
    - `tests`
    
2. Seznamte se s obsahem README
    - Jak se takový balíček instaluje
        - pipem přímo z gitu
        - pipem z lokální složky 
        - diskutujte variantu, `git clone` + `pip install -e <lokální cesta>`
        
3. Vyzkoušejte v nově vytvořeném souboru kdekoli jinde na lokálním stroji použít nově nainstalovnanou knihovnu (viz examples)

4. vyzkoušejte použít command line interface nainstalovaného balíčku z CMD
    - Všimněte si, že argparser automaticky generuje help_prompt. Zkuste do CMD napsat jen `expac`
5. Zkuste spustit testy podle návodu v README


# Další cvičení
Vytvořte / Upravte balíček:
1. Integrujte funkcionalitu z prvního cvičení (výpočet průměrného platu) 
2. Připravte CLI, které vypočte meziroční změnu průměrného platu. Příkaz `salstat`

    `salstat --file <cesta_k_souboru> --year <rok>` 

# K zamyšlení
- proč jsou argumenty parsované z příkazové řádky drženy v dataclass? 
