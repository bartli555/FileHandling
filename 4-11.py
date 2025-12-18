output_file = 'potęgi.txt'

try:
    with open(output_file, 'w', encoding='utf-8') as file:
        for i in range(1, 101):
            square = i ** 2
            cube = i ** 3

            line = f"{i},{square},{cube}"

            print(line)
            
            
            file.write(line + "\n")

            print("\nZakończono! Dane zostały zapisane.")

except IOError as e:
    print(f"Błąd zapisu do pliku: {e}")            