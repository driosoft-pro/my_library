from libro import Libro  # Importa la clase Libro desde el módulo libro.
from usuario import Usuario  # Importa la clase Usuario desde el módulo usuario.
from prestamo import Prestamo  # Importa la clase Prestamo desde el módulo prestamo.

class Biblioteca:
    def __init__(self):
        """
        Constructor de la clase Biblioteca.
        Inicializa las listas de libros, usuarios y préstamos.
        """
        self.libros = []  # Lista para almacenar los libros disponibles en la biblioteca.
        self.usuarios = []  # Lista para almacenar los usuarios registrados en la biblioteca.
        self.prestamos = []  # Lista para almacenar los préstamos realizados.

    def listar_usuarios(self):
        """
        Muestra en pantalla la lista de usuarios registrados en la biblioteca.
        """
        print("\nUsuarios registrados:")
        print("=" * 50)
        print(f"{'Código':<10} {'Nombre':<20} {'Tipo de Usuario':<15}")
        print("=" * 50)
        
        # Itera sobre la lista de usuarios y muestra sus datos.
        for usuario in self.usuarios:
            print(f"{usuario.codigo:<10} {usuario.nombre:<20} {usuario.tipo_usuario:<15}")

    def listar_libros(self):
        """
        Muestra en pantalla la lista de libros disponibles en la biblioteca.
        """
        print("\nLista de libros en la biblioteca:")
        print("=" * 80)
        print(f"{'Código':<10} {'Título':<30} {'Autor':<25} {'Año':<6} {'Disponibles':<10}")
        print("=" * 80)

        # Itera sobre la lista de libros y muestra sus datos.
        for libro in self.libros:
            print(f"{libro.codigo:<10} {libro.titulo:<30} {libro.autor:<25} {libro.anio:<6} {libro.disponibles:<10}")

    def listar_libros_disponibles(self):
        """
        Retorna una lista de libros que tienen ejemplares disponibles.
        """
        return [libro for libro in self.libros if libro.disponibles > 0]

    def buscar_libro(self, criterio, valor):
        """
        Busca libros en la biblioteca según un criterio (atributo) y un valor.
        Retorna una lista de libros que coincidan con el criterio y valor.
        """
        return [libro for libro in self.libros if getattr(libro, criterio, '').lower() == valor.lower()]

    def realizar_prestamo(self, usuario, libro, dias):
        """
        Realiza un préstamo de un libro a un usuario por un número de días.
        - Verifica si el libro puede ser prestado y si el usuario puede recibir el préstamo.
        - Si es posible, crea un objeto Prestamo y lo agrega a la lista de préstamos.
        Retorna True si el préstamo se realizó con éxito, de lo contrario False.
        """
        if libro.prestar() and usuario.agregar_prestamo(libro):
            prestamo = Prestamo(usuario, libro, dias)  # Crea un nuevo préstamo.
            self.prestamos.append(prestamo)  # Agrega el préstamo a la lista de préstamos.
            return True
        return False

    def devolver_libro(self, usuario, libro):
        """
        Permite a un usuario devolver un libro prestado.
        - Busca el préstamo correspondiente en la lista de préstamos.
        - Si se encuentra, elimina el préstamo, actualiza el estado del libro y del usuario.
        Retorna True si la devolución se realizó con éxito, de lo contrario False.
        """
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.libro == libro:
                usuario.remover_prestamo(libro)  # Elimina el libro de los préstamos del usuario.
                libro.devolver()  # Incrementa la cantidad de ejemplares disponibles del libro.
                self.prestamos.remove(prestamo)  # Elimina el préstamo de la lista de préstamos.
                return True
        return False

    def consultar_prestamos_usuario(self, usuario):
        """
        Retorna una lista de préstamos realizados por un usuario específico.
        """
        return [prestamo for prestamo in self.prestamos if prestamo.usuario == usuario]