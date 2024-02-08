



def load_data_file(filepath: str, wanted_year: int):
    students = []
    return students


def count_average_salary(data: list[Person]):
    return 0


def count_median_salary(data: list[Person]):
    return 0
    


def main(input_path: str):
    # data14 = count_average_salary(load_data_file(input_path, 2014))
    # data15 = count_average_salary(load_data_file(input_path, 2015))
    # print(data14, data15)

    
    year = None
    data = None
    avg = count_average_salary(data)
    print(f"Průměrný plat v roce {year}  je  {avg}")

    median = count_median_salary(data)
    print(f"Medián v roce {year}  je  {median}")


if __name__ == '__main__':
    data_path = None
    main(data_path)

