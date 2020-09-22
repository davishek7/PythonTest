import psycopg2
conn = psycopg2.connect(database="PythonTest", 
user="postgres", 
password="1234", 
host="localhost", 
port="5432")
print("Database Connected....")