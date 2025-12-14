print("--- Zawartość pliku pets.txt ---")
try:
   
    with open('pets.txt', 'r', encoding='utf-8') as file:
        
        total_words = 0
        
        
        for line in file:
        
            print(line, end='')
            
            words = line.split()
            
            line_word_count = len(words)
            
            total_words += line_word_count

    print("\n\n--- Wynik ---")
    print(f"Liczba słów w tekście: {total_words}")

except FileNotFoundError:
    print("Błąd: Nie znaleziono pliku 'pets.txt'. Upewnij się, że plik istnieje.")