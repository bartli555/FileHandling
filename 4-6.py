filename = input("Podaj nazwę pliku tekstowego: ").strip()

try:
    with open(filename, 'r', encoding='UTF-8') as file:

        content = file.read()

        num_chars = len(content)

        words = content.split()
        num_words = len(words)

        lines = content.splitlines()
        num_lines = len(lines)

        print(f"\n Plik: {filename}")
        print(f"Liczba wierszy: {num_lines}")
        print(f"Liczba znaków:  {num_chars}")
        print(f"Liczba słów:    {num_words}")

except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku '{filename}'.")
except Exception as e:
    print(f"Wystąpił nieoczekiwany błąd: {e}")        
