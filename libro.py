class Libro:
    """
    Clase que representa un libro en el sistema de biblioteca.
    
    Atributos:
        titulo (str): Título del libro.
        autor (str): Autor del libro.
        anio_publicacion (int): Año de publicación del libro.
        area (str): Área temática del libro (ej. programación, física, etc.).
        codigo (str): Código único identificador del libro.
        unidades (int): Cantidad total de copias del libro.
        disponibles (int): Cantidad de copias disponibles para préstamo.
    """
    
    def __init__(self, titulo, autor, anio_publicacion, area, codigo, unidades):
        """
        Inicializa un nuevo libro con los datos proporcionados.
        
        Args:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            anio_publicacion (int): Año de publicación.
            area (str): Área temática.
            codigo (str): Código único.
            unidades (int): Cantidad total de copias.
        """
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.area = area
        self.codigo = codigo
        self.unidades = unidades
        self.disponibles = unidades
        
    def __str__(self):
        """Representación en string del libro."""
        return (f"Libro: {self.titulo} - {self.autor} ({self.anio_publicacion})\n"
                f"Área: {self.area}, Código: {self.codigo}\n"
                f"Disponibles: {self.disponibles}/{self.unidades}")
    
    def prestar(self):
        """Método para registrar el préstamo de una unidad del libro."""
        if self.disponibles > 0:
            self.disponibles -= 1
            return True
        return False
    
    def devolver(self):
        """Método para registrar la devolución de una unidad del libro."""
        if self.disponibles < self.unidades:
            self.disponibles += 1
            return True
        return False
    
    def esta_disponible(self):
        """Verifica si hay unidades disponibles del libro."""
        return self.disponibles > 0

    def obtener_info_prestamo(self):
        """Devuelve información relevante para préstamos"""
        return {
            'codigo': self.codigo,
            'titulo': self.titulo,
            'disponibles': self.disponibles,
            'unidades': self.unidades,
            'esta_disponible': self.esta_disponible()
        }