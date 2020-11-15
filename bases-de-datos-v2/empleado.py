class Empleado:
    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
    
    def crear_email(self):
        return '{}_{}@mail.com'.format(self.nombre, self.apellido)
    
    def crear_nombre_completo(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def __repr__(self):
        return "Empleado('{}', '{}', {})".format(self.nombre, self.apellido, self.salario)

