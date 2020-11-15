import sqlite3 

from empleado import Empleado

DB_NAME_PATH = "/Users/hever/Desktop/bases-de-datos-py/bases-de-datos-v2/gkshopv2.db"

conn = sqlite3.connect(DB_NAME_PATH)

c = conn.cursor()

def insertar_empleado(emp):
    with conn:
        c.execute("INSERT INTO empleados VALUES (:nombre_empleado, :apellido_empleado, :salario_empleado)",
        {"nombre_empleado":emp.nombre,"apellido_empleado":emp.apellido, "salario_empleado":emp.salario}
        )

def ver_empleados():
    c.execute("SELECT * FROM empleados")
    return c.fetchall()

def obtener_empleado_por_apellido(apellido_empleado):
    c.execute("SELECT * FROM empleados WHERE apellido=:apellido",{'apellido':apellido_empleado})
    return c.fetchall()


def actualizar_pago(emp,salario_empleado):
    with conn:
        query = """UPDATE empleados SET salario = ? WHERE nombre = ? AND apellido = ?"""
        parameters = (salario_empleado,emp.nombre,emp.apellido)
        c.execute(query,parameters)

def eliminar_empleado(emp):
    with conn:
        query = """DELETE FROM empleados WHERE nombre = ? AND apellido = ?"""
        parameters = (emp.nombre, emp.apellido)
        c.execute(query,parameters)


if __name__ == "__main__":
    #crear_tabla()
    # Insertar
    empleado_uno = Empleado("Jhon","Doe", 5000)

    #insertar_empleado(empleado_uno)

    #empleado_dos = Empleado("Bob","Winslet", 8000)

    #insertar_empleado(empleado_dos)

    # Actualizar

    #actualizar_pago(empleado_dos,6000)

    #busqueda = obtener_empleado_por_apellido('Winslet')
    
    #print(busqueda)

    eliminar_empleado(empleado_uno)

    todos_los_datos = ver_empleados()

    print(todos_los_datos)

    conn.commit()

    conn.close()