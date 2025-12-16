###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Wprowadź nazwę użytkownika: ')
password = input('Wprowadź hasło: ')

# pattern (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^\w{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print('Poprawne dane, utworzono konto.')
else:
   print('Błąd danych')
   if not username_match:
        print('Nazwa użytkownika musi mieć min. 6 znaków i zawierać TYLKO małe litery.')
   if not password_match:
        print('Hasło musi mieć min. 8 znaków i zawierać tylko litery, cyfry lub "_".')   