import subprocess

'''GETTING SQL SYNTAX FROM DATABase'''

# Command to run
command = 'pg_dump --dbname=postgresql://jmrozek:furm3w3sj5s7@lab.kis.agh.edu.pl:1500/jmrozek -s  > dump.sql'

try:
    result = subprocess.run(command, shell=True)

except subprocess.CalledProcessError as e:
    # Handle any errors that occurred during the command execution
    print("Error:", e)


''' getting dbml model from sql'''

command = 'sql2dbml dump.sql --postgres'

try:
    with open('dump.dbml', 'w') as file:
        result = subprocess.run(command, shell=True, stdout=file)


except subprocess.CalledProcessError as e:
    # Handle any errors that occurred during the command execution
    print("Error:", e)

'''getting image from dbml'''


# Command to run
command = 'python -m dbml2dot -i dump.dbml -o schema.dot --type svg'

try:
    result = subprocess.run(command, shell=True)

except subprocess.CalledProcessError as e:
    # Handle any errors that occurred during the command execution
    print("Error:", e)