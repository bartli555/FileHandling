###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as file_in:
   with open(position_file, 'w') as file_out:
      licznik = 0
      for line in file_in:
         if job_title in line:
            file_out.write(line)
            licznik += 1
print(f"Zapisano {licznik} pracowników do pliku '{position_file}'.")            