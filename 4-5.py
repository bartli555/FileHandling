import emails

email_file = 'email.txt'

try:
    with open(email_file, 'r', encoding='utf-8') as file:
        content = file.read()

    sender = emails.nadawca_emaila(content)
    recipient = emails.odbiorca_emaila(content)
    subject = emails.email_subject(content)
    body = emails.email_body(content)

    print(f"Nadawca:  {sender}")
    print(f"Odbiorca: {recipient}")
    print(f"Temat:    {subject}")
    
    print("\nTreść Wiadomości: ")
    if body:
        print(body)
    else:
        print("(Brak treści lub nieprawidłowy format)")

except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku '{email_file}'.")        