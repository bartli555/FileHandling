import re

files_list_name = 'files.txt'

try:
    with open(files_list_name, 'r', encoding='utf-8') as file:
        for line in file:
            filename = line.strip()

            pattern = r'\.\w{4}$'

            if re.search(pattern, filename):
                print(filename)

except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku '{files_list_name}'.")                