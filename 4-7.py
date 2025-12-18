import re

text = input("Wprowadź tekst: ")

pattern = r"[aeiouyAEIOUY]"

vowels = re.findall(pattern, text)

count = len(vowels)

print(f"\nTekst: '{text}'")
print(f"Liczba samogłosek: {count}")