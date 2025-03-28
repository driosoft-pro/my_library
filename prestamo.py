from datetime import date, timedelta

class Prestamo:
    def __init__(self, usuario, libro, dias_prestamo):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.dias_prestamo = dias_prestamo
        self.fecha_devolucion = self.calcular_fecha_devolucion()

    def calcular_fecha_devolucion(self):
        return self.fecha_prestamo + timedelta(days=self.dias_prestamo)

    def __str__(self):
        return f"{self.usuario.nombre} prestó {self.libro.titulo} hasta {self.fecha_devolucion}"