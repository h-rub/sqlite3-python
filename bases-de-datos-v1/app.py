import sqlite3

DB_NAME = "/Users/hever/Desktop/bases-de-datos-py/gkshop.db"
conn = sqlite3.connect(DB_NAME)

c = conn.cursor()

def crear_tabla():
    c.execute(""" CREATE TABLE empleados (
                            nombre TEXT,
                            apellido TEXT,
                            salario REAL)
    """)

#c.execute("INSERT INTO empleados VALUES ('Kate', 'Winslet', 12000)")

c.execute("SELECT * from empleados")

resultados_query = c.fetchall()

for i in resultados_query:
    print(i)

conn.commit()

conn.close()