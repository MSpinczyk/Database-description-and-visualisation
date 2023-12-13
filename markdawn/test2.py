import subprocess

'''GETTING SQL SYNTAX FROM DATABase'''

# Command to run
command = 'pg_dump --dbname=postgresql://postgres:jmrozek@127.0.0.1:5432/Project1 -s > dump.txt'

try:
    result = subprocess.run(command, shell=True)

except subprocess.CalledProcessError as e:
    # Handle any errors that occurred during the command execution
    print("Error:", e)
