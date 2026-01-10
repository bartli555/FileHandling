file_name = 'it_company.csv'

try:
    with open(file_name, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        total_lines = len(lines)

        current_line = 0

        while current_line < total_lines:
            end_line = min(current_line +5, total_lines)

            for i in range(current_line, end_line):
                print(lines[i].strip())

            current_line = end_line

            if current_line < total_lines:
                input('Naciśnij Enter')
                print()

except FileNotFoundError:
    print('Nie znaleziono pliku')                    

