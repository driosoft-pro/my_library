from libro import Libro  # Importa la clase Libro desde el módulo libro.
from usuario import Usuario  # Importa la clase Usuario desde el módulo usuario.

class BaseDatos:
    def __init__(self):
        """
        Constructor de la clase BaseDatos.
        Inicializa la base de datos con una lista de libros y usuarios predefinidos.
        """
        # Lista de libros disponibles en la base de datos, cada uno es una instancia de la clase Libro.
        self.libros = [
            Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Literatura", "L001", 5, 5),
            Libro("1984", "George Orwell", 1949, "Ficción", "L002", 4, 4),
            Libro("El principito", "Antoine de Saint-Exupéry", 1943, "Infantil", "L003", 6, 6),
            Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981, "Literatura", "L004", 3, 3),
            Libro("El código Da Vinci", "Dan Brown", 2003, "Misterio", "L005", 4, 4),
            Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, "Fantasía", "L006", 5, 5),
            Libro("El Hobbit", "J.R.R. Tolkien", 1937, "Fantasía", "L007", 3, 3),
            Libro("Los juegos del hambre", "Suzanne Collins", 2008, "Ciencia ficción", "L008", 6, 6),
            Libro("Orgullo y prejuicio", "Jane Austen", 1813, "Romance", "L009", 4, 4),
            Libro("Moby Dick", "Herman Melville", 1851, "Aventura", "L010", 3, 3),
            Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Clásico", "L011", 2, 2),
            Libro("El arte de la guerra", "Sun Tzu", -500, "Estrategia", "L012", 5, 5),
            Libro("Sapiens", "Yuval Noah Harari", 2011, "Historia", "L013", 4, 4),
            Libro("La divina comedia", "Dante Alighieri", 1320, "Clásico", "L014", 3, 3),
            Libro("Drácula", "Bram Stoker", 1897, "Terror", "L015", 4, 4),
            Libro("It", "Stephen King", 1986, "Terror", "L016", 5, 5),
            Libro("Fundación", "Isaac Asimov", 1951, "Ciencia ficción", "L017", 3, 3),
            Libro("El nombre del viento", "Patrick Rothfuss", 2007, "Fantasía", "L018", 6, 6),
            Libro("Dune", "Frank Herbert", 1965, "Ciencia ficción", "L019", 4, 4),
            Libro("Frankenstein", "Mary Shelley", 1818, "Terror", "L020", 5, 5),
            Libro("La Odisea", "Homero", -700, "Clásico", "L021", 2, 2),
            Libro("Cumbres Borrascosas", "Emily Brontë", 1847, "Romance", "L022", 3, 3),
            Libro("El retrato de Dorian Gray", "Oscar Wilde", 1890, "Filosofía", "L023", 4, 4),
            Libro("Sherlock Holmes: Estudio en escarlata", "Arthur Conan Doyle", 1887, "Misterio", "L024", 5, 5),
            Libro("Los pilares de la Tierra", "Ken Follett", 1989, "Histórico", "L025", 4, 4),
            Libro("Rayuela", "Julio Cortázar", 1963, "Literatura", "L026", 3, 3),
            Libro("El perfume", "Patrick Süskind", 1985, "Misterio", "L027", 4, 4),
            Libro("La sombra del viento", "Carlos Ruiz Zafón", 2001, "Misterio", "L028", 5, 5),
            Libro("Ensayo sobre la ceguera", "José Saramago", 1995, "Filosofía", "L029", 4, 4),
            Libro("El señor de los anillos", "J.R.R. Tolkien", 1954, "Fantasía", "L030", 3, 3)
        ]

        # Lista de usuarios registrados en la base de datos, cada uno es una instancia de la clase Usuario.
        self.usuarios = [
            Usuario("U001", "Juan Pérez", "Estudiante"),
            Usuario("U002", "María López", "Profesor"),
            Usuario("U003", "Carlos Gómez", "Estudiante"),
            Usuario("U004", "Ana Rodríguez", "Estudiante"),
            Usuario("U005", "Pedro Martínez", "Profesor")
        ]

    def obtener_libros(self):
        """
        Retorna la lista de libros disponibles en la base de datos.
        """
        return self.libros
    
    def obtener_usuarios(self):
        """
        Retorna la lista de usuarios registrados en la base de datos.
        """
        return self.usuarios