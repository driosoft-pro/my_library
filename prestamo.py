from datetime import datetime, timedelta

class Prestamo:
    """
    Clase que representa un préstamo de libro en el sistema.
    
    Atributos:
        usuario (Usuario): Usuario que realiza el préstamo.
        libro (Libro): Libro que se presta.
        fecha_prestamo (datetime): Fecha en que se realiza el préstamo.
        dias_prestamo (int): Días de duración del préstamo.
        fecha_devolucion (datetime): Fecha estimada de devolución.
        devuelto (bool): Indica si el libro ha sido devuelto.
    """
    
    def __init__(self, usuario, libro, dias_prestamo=7):
        """
        Inicializa un nuevo préstamo.
        
        Args:
            usuario (Usuario): Usuario que pide prestado.
            libro (Libro): Libro a prestar.
            dias_prestamo (int): Días del préstamo (default 7).
        """
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.dias_prestamo = dias_prestamo
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=dias_prestamo)
        self.devuelto = False
        
    def __str__(self):
        """Representación en string del préstamo."""
        estado = "Devuelto" if self.devuelto else "Pendiente"
        return (f"Préstamo: {self.libro.titulo} a {self.usuario.nombre}\n"
                f"Fecha préstamo: {self.fecha_prestamo.strftime('%d/%m/%Y')}\n"
                f"Fecha devolución: {self.fecha_devolucion.strftime('%d/%m/%Y')}\n"
                f"Estado: {estado}")
    
    def esta_vencido(self):
        """Verifica si el préstamo está vencido."""
        return datetime.now() > self.fecha_devolucion and not self.devuelto
    
    def devolver(self):
        """Marca el préstamo como devuelto."""
        if not self.devuelto:
            self.devuelto = True
            return True
        return False