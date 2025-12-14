###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    numerowanie = 1
    for line in file:
        print(numerowanie, line, end="")
        numerowanie += 1