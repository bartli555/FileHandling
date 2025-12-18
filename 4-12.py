import csv

GENRE_TO_FILENAME = {
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt'
}

def copy_books_by_genre(input_file):

    try:
        with open(input_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            stats = {genre: 0 for genre in GENRE_TO_FILENAME}

            for row in reader:
                genre = row['Genre']

                if genre in GENRE_TO_FILENAME:
                    target_file = GENRE_TO_FILENAME[genre]

                    book_info = f"{row['Title']},{row['Author']},{row['Year']}\n"

                    with open(target_file, 'a', encoding='utf-8') as file:
                        file.write(book_info)
                        
                    stats[genre] += 1

        print("\nStatystyki:")
        for genre, count in stats.items():
            print(f"- {genre}: zapisano {count} książek do '{GENRE_TO_FILENAME[genre]}'")            

    except FileNotFoundError:
        print(f"Błąd. Nie znaleziono pliku '{input_file}'.")
    except KeyError:
        print("Błąd. Plik CSV ma nieprawidłowe nagłówki")     

if __name__ == "__main__":
    for filename in GENRE_TO_FILENAME.values():
        with open(filename, 'w', encoding='utf-8') as f:
            pass

    copy_books_by_genre('books.csv')               