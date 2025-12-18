import csv

file_name = 'clothing.csv'

try:
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            price = float(row['Price'])
            stock = int(row['Stock_Quantity'])

            if price < 60 and stock < 40:
                print(f"Produkt: {row['Product_Name']} | Cena: {price} | Ilość: {stock}")

except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku '{file_name}'.")
except ValueError:
    print("Błąd: Dane w pliku CSV nie są poprawnymi liczbami.")                