from libro import Libro
from usuario import Usuario
import unicodedata

class BD:
    """
    Clase que simula una base de datos para el sistema de biblioteca.
    
    Atributos:
        libros (dict): Diccionario de libros (clave: código).
        usuarios (dict): Diccionario de usuarios (clave: identificador).
        prestamos (list): Lista de préstamos activos.
    """
    
    def __init__(self):
        """Inicializa la BD con datos de ejemplo."""
        self.libros = {}
        self.usuarios = {}
        self.prestamos = []
        
        # Inicializar con datos de ejemplo
        self._inicializar_datos()
    
    def _inicializar_datos(self):
        """Método privado para cargar datos iniciales."""
        # Crear libros de ejemplo
        libros_ejemplo = [
            Libro("Python Crash Course", "Eric Matthes", 2019, "programación", "PYT001", 3),
            Libro("Clean Code", "Robert C. Martin", 2008, "programación", "PYT002", 2),
            Libro("The Pragmatic Programmer", "Andrew Hunt", 1999, "programación", "PYT003", 1),
            Libro("Introduction to Algorithms", "Thomas H. Cormen", 2009, "programación", "PYT004", 4),
            Libro("Design Patterns", "Erich Gamma", 1994, "programación", "PYT005", 2),
            Libro("A Brief History of Time", "Stephen Hawking", 1988, "física", "FIS001", 3),
            Libro("The Feynman Lectures on Physics", "Richard Feynman", 1964, "física", "FIS002", 2),
            Libro("Cosmos", "Carl Sagan", 1980, "astronomía", "AST001", 1),
            Libro("Sapiens", "Yuval Noah Harari", 2011, "historia", "HIS001", 3),
            Libro("The Selfish Gene", "Richard Dawkins", 1976, "biología", "BIO001", 2)
        ]
        
        for libro in libros_ejemplo:
            self.libros[libro.codigo] = libro
        
        # Crear usuarios de ejemplo
        usuarios_ejemplo = [
            Usuario("Juan Pérez", "U001", "estudiante"),
            Usuario("María García", "U002", "profesor"),
            Usuario("Carlos López", "U003", "estudiante")
        ]
        
        for usuario in usuarios_ejemplo:
            self.usuarios[usuario.identificador] = usuario
    
    def agregar_prestamo(self, prestamo):
        """Agrega un préstamo a la lista de préstamos activos."""
        self.prestamos.append(prestamo)
    
    def remover_prestamo(self, prestamo):
        """Remueve un préstamo de la lista de préstamos activos."""
        if prestamo in self.prestamos:
            self.prestamos.remove(prestamo)
    
    def normalizar_texto(texto):
        """Elimina tildes y convierte a minúsculas para búsquedas insensibles"""
        texto = unicodedata.normalize('NFD', texto.lower())
        texto = ''.join(c for c in texto if not unicodedata.combining(c))
        return texto
    
    def obtener_libros_por_titulo(self, titulo):
        titulo_norm = normalizar_texto(titulo)
        return [libro for libro in self.libros.values() 
                if titulo_norm in normalizar_texto(libro.titulo)]

    def obtener_libros_por_autor(self, autor):
        autor_norm = normalizar_texto(autor)
        return [libro for libro in self.libros.values() 
                if autor_norm in normalizar_texto(libro.autor)]

    def obtener_libros_por_area(self, area):
        area_norm = normalizar_texto(area)
        return [libro for libro in self.libros.values() 
                if area_norm in normalizar_texto(libro.area)]
    
    def obtener_prestamos_usuario(self, identificador_usuario):
        """Obtiene los préstamos de un usuario específico."""
        return [p for p in self.prestamos if p.usuario.identificador == identificador_usuario and not p.devuelto]
    
    def listar_usuarios(self):
        """Devuelve lista de todos los usuarios registrados"""
        return list(self.usuarios.values())

    def buscar_usuario_por_nombre(self, nombre):
        """Busca usuarios por coincidencia parcial en el nombre"""
        return [u for u in self.usuarios.values() if nombre.lower() in u.nombre.lower()]

    def buscar_usuario_por_identificador(self, identificador):
        """Ahora case-insensitive"""
        identificador_norm = normalizar_texto(identificador)
        for usuario in self.usuarios.values():
            if normalizar_texto(usuario.identificador) == identificador_norm:
                return usuario
        return None
    
    def obtener_areas_tematicas(self):
        """Devuelve una lista de áreas temáticas únicas"""
        return list(set(libro.area for libro in self.libros.values()))