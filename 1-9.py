###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

with open('it_company.csv', 'r') as file:
   numerowanie = 1
   for line in file:
      if job_title in line:
         print (f'{numerowanie}. Pracownik na stanowisko Inżynier oporgramowania: {line}')
         numerowanie += 1