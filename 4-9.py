import csv

file_name = 'it_company.csv'

job_title = 'Graphic Designer'

print("GRAPHIC DESIGNERS")
print("=================")

try:
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile) #automatyczne mapowanie nagłówka

        for row in reader:
            if row['Job Title'] == job_title:
                first_name = row['First Name']
                last_name = row['Last Name']
                email = row['Email']

                print(f"{first_name} {last_name},{email}")

except FileNotFoundError:
    print(f"Błąd. Nie znaleziono pliku '{file_name}'.")                