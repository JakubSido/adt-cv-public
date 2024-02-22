
import os
import sys

class Person:
    def __init__(self, first:str, last:str, salary:float):
        self.first: str = first
        self.last: str = last
        self.salary: float = salary

    def __str__(self):
        return f"{self.first} {self.last} {self.salary}"


def load_data_file(filepath: str, wanted_year: int):
    people : list[Person] = list()
     
    with open(filepath, "r", encoding="utf8") as fd:

        for line in fd:
            line = line.replace("\n", "")
            fields = line.split(";")

            if len(fields) != 15:
                print(f"V řádku je nevalidní záznam -- špatný počet polí\n{line}\n", len(fields), file=sys.stderr)
                continue
            
            first_s = fields[2]
            last_s = fields[3]
            year_s = fields[12]
            sallary_s = fields[14]
            
            if not year_s.isnumeric():
                print(f"V řádku je nevalidní záznam -- Očekávám číselnou hodnotu\n{line}\n{year_s}", file=sys.stderr)
                continue

            year = int(year_s)
            sallary = float(sallary_s)
            if year == wanted_year:
                s = Person(first_s, last_s, sallary)
                people.append(s)

                if len(people) % 10000 == 0:
                    print(f"loaded {len(people)}")
    
    return people


def count_average_salary(data: list[Person]):
                                
    sum = 0.0
    for d in data:
        sum += d.salary
    return sum / len(data)
                                

                                
def sallary_from_person(p: Person):
    return p.salary
                                

def count_median_salary(data: list[Person]):
    
    # sorted_data = sorted(data, key=lambda x: x.salary)
    sorted_data = sorted(data, key=sallary_from_person)
    # sorted_data = sorted(data, key=attrgetter('sallary'))
    if len(sorted_data) % 2 == 1:
        return sorted_data[len(data) // 2].salary
    else:
        return (sorted_data[len(data) // 2 - 1].salary + sorted_data[(len(data) // 2)].salary) / 2
    


def main(input_path: str):

    
    avg14 = count_average_salary(load_data_file(input_path, 2014))
    avg15 = count_average_salary(load_data_file(input_path, 2015))
    
    print(f"Prumerna mzda se pro rok 2014 a 2015 změnila z {avg14} na {avg15} to je o {avg15-avg14} Kč" )
    

    while True:
        year_s = input("Zdejte rok (year):")
        if not year_s.isnumeric():
            print("Zadejte numerickou hodnotu")
            continue

        year = int(year_s)
        data = load_data_file(input_path, year)
        if len(data) == 0:
            print("Filtrem na rok neprošly žádné osoby")
            continue
        print(f"Načteno datovych vzorků: {len(data)}\n")
        break
    
    avg = count_average_salary(data)
    print(f"Průměrný plat v roce {year}  je  {avg}")

    median = count_median_salary(data)
    print(f"Medián v roce {year}  je  {median}")


if __name__ == '__main__':
    data_path = None
    
    print("Program počítá průměrný příjem a medián.")

    arguments = sys.argv
    print(f"nacteno parametrů: {len(arguments)} -- {arguments}")

    if len(arguments) != 2:
        print("Program nebyl spuštěn správně. Očekávám jméno souboru\n ")
        exit(1)

    data_path = arguments[1]
    if not os.path.exists(data_path):
        print(f"Soubor {data_path} neexistuje")
        exit(2)  
    
    main(data_path)

