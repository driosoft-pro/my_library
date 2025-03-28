from datetime import date, timedelta  # Importa las clases date y timedelta para manejar fechas.

class Prestamo:
    def __init__(self, usuario, libro, dias_prestamo):
        """
        Constructor de la clase Prestamo.
        Inicializa un préstamo con el usuario, el libro, la fecha de préstamo y la duración del préstamo.
        """
        self.usuario = usuario  # Usuario que realiza el préstamo.
        self.libro = libro  # Libro que se presta.
        self.fecha_prestamo = date.today()  # Fecha en la que se realiza el préstamo (fecha actual).
        self.dias_prestamo = dias_prestamo  # Número de días que dura el préstamo.
        self.fecha_devolucion = self.calcular_fecha_devolucion()  # Calcula la fecha de devolución.

    def calcular_fecha_devolucion(self):
        """
        Calcula la fecha de devolución sumando los días del préstamo a la fecha de préstamo.
        Retorna la fecha de devolución.
        """
        return self.fecha_prestamo + timedelta(days=self.dias_prestamo)  # Suma los días del préstamo a la fecha actual.

    def __str__(self):
        """
        Retorna una representación en cadena del préstamo.
        Muestra el nombre del usuario, el título del libro y la fecha de devolución.
        """
        return f"{self.usuario.nombre} prestó {self.libro.titulo} hasta {self.fecha_devolucion}"