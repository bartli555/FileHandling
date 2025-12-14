seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

file_name = 'seven_wonders.txt'

seven_wonders.sort()

try:
    with open(file_name, 'w') as file:
        for item in seven_wonders:
            file.write(f"{item}\n")

    print(f"Pomyślnie zapisano dane do pliku '{file_name}'.")           

    with open(file_name, 'r',) as file:
        content = file.read()
        print(content)

except IOError:
    print("Błąd: Nie udało się zapisać lub odczytać pliku.")