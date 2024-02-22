# Opakování PPA, načítání dat ze souboru a jejich analýza


# 1. REPL: Read-eval-print-loop

Spusťte REPL Pythonu v terminálu operačního systému. Spočtěte délku přepony pravoúhlého trojuhelníku:

1. Připravte proměnné pro délky odvěsen a = 3; b = 4
2. Vypočtěte délku přepony pravoúhlého trojúhelníku a uložte do proměnné c
   (použijte sqrt z modulu math)
3. Vypište hodnotu c



# 2. CMD, Visual Studio Code

Vytvořte skript (textový soubor) se sekvencí příkazů, které vedou ke stejnému výsledku jako v předešlém cvičení s REPL.

## Zásady pro vypracování

1. Proměnné staticky vytvořte v kódu.
2. Importy soustřeďte na začátku textového souboru
3. Diskutujte příponu souboru (.txt .py) Fungují stejně? Proč?
    1. Program spusťte z terminálu operačního systému
    2. Program spusťte v prostředí VSC




# 3. Jednoduchá aplikace pro analýzu databáze osob



Vstupující datový soubor[^1] [[liks]](https://liks.fav.zcu.cz/adt/exam/service/download-data?filename=data-salaries-years-11M.csv) obsahuje 11M datových vzorků s informacemi o osobách a jejich příjmech v letech 2010-2020 (
11 let). Úkolem je vytvořit program, který načte záznamy a vypočte průměrný příjem osob splňující zadanou podmínku, s
jeho pomocí bude snadné odpovídat na otázky jako:
_Jak se změnila průměrná mzda mezi lety 2014 a 2015?_

[^1]: Data jsou synteticky vyrobená -- generovaná ze statistických ukazatelů. Výsledky analýzy tedy mohou být zkreslené

1. Načtete cestu k souboru -- argument spouštěného programu.
   
   Ověřte, že:
    1. Programu je předán očekávaný počet argumentů.
    2. Předaný argument je cesta k existujícímu souboru.
    3. Ověřte, že pracujeme se souborem ve správném kódování znaků
    
2. Připravte třídu pro reprezentaci Záznamu -- řádek v souboru s daty.
3. Vytvořte funkci _load\_data\_file_, která načtete do paměti všechny osoby z datového souboru. Cestu k souboru
      přijme jako svůj parametr. Seznam instancí osob vrátí jako svou návratovou hodnotu.

   
4. Ošetříme hlavičku souboru
      1. Všechny řádky obsahují očekávaný počet hodnot.
      2. Rok a příjem jsou číselné hodnoty.
      3. Řádek, který neobsahuje validní záznam přeskočte, informujte o tom ale uživatele.
5. Vytvořte funkci _count\_average\_sallary_, která jako vstupní parametr přijme seznam osob a vrátí průměrný
   příjem.
6. Ve funkci main zavolejte funkci pro načtení dat. Pohledem ověřte, že je seznam osob načtený správně.
7. Navrácený seznam osob předejte do funkce pro výpočet průměrného příjmu.
8. Hodnotu průměrného příjjmu vytiskněte na standardní výstup programu.
9. Upravte funkci _load\_data\_file_ tak, aby přijimala navíc jeden parametr $year$. Funkce vrátí záznamy
   pouze z daného roku.
10. Připravte funkci pro výpočet mediánu příjmu.

11. Jak se změnil průměrný příjem a medián mezi roky 2014 a 2015?



# K zamyšlení

1. Je nutné v našem případě načítat všechny informace o osobách do přepravek? 
2. Je možné úkol splnit jedním průchodem bez nutnosti načítat celá data do paměti?
3. Jsou problémy které streamově nevyřešíme? 
4. Jaká jsou pro a proti? 
5. Když pracujeme jen s podskupinou, má smysl načíst jen podskupinu?
6. Co je návratová hodnota programu? Jak ji nastavit? K čemu je to dobré?
7. Přidat transformaci dat na každý prvek v poli
8. ukažme co se stane když bude náš vstup špatný například: jako rok zadáme 2000, který v datech není.



# Tipy

1. VSC umožní při použití ctrl+click prokliknout chybu v konzoli do kódu.
2. Všimněme si podobnosti argumentů python main.py python main.py datat.csv main.py je vstup pro python data.csv je
   vstup pro main.py
3. Očekávání vstupu od uživatele intput() je stejné jako prompt REPLu


# Domácí cvičení Odpovězte na otázku:

V roce 2013 byl nendostatek krve 0+. Kolik litrů krve mohlo transfúzní oddělení v obci Kamenice v tomto roce odebrat od
lidí?
1. Darovat krev může každý muž či žena ve věku 18-65 let.
2. Tělesná hmotnost dárce krve by měla být minimálně 50 kg.
3. Muži mohou darovat 4x ročně ale ženy pouze 3x.
4. Při jednom odběru získáme 450 ml krve 

