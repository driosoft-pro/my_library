from libro import Libro
from usuario import Usuario
from prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []
        
    def listar_usuarios(self):
        print("\nUsuarios registrados:")
        print("=" * 50)
        print(f"{'Código':<10} {'Nombre':<20} {'Tipo de Usuario':<15}")
        print("=" * 50)
        
        for usuario in self.usuarios:
            print(f"{usuario.codigo:<10} {usuario.nombre:<20} {usuario.tipo_usuario:<15}")

    def listar_libros(self):
        print("\nLista de libros en la biblioteca:")
        print("=" * 80)
        print(f"{'Código':<10} {'Título':<30} {'Autor':<25} {'Año':<6} {'Disponibles':<10}")
        print("=" * 80)

        for libro in self.libros:
            print(f"{libro.codigo:<10} {libro.titulo:<30} {libro.autor:<25} {libro.anio:<6} {libro.disponibles:<10}")

    def listar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponibles > 0]

    def buscar_libro(self, criterio, valor):
        return [libro for libro in self.libros if getattr(libro, criterio, '').lower() == valor.lower()]

    def realizar_prestamo(self, usuario, libro, dias):
        if libro.prestar() and usuario.agregar_prestamo(libro):
            prestamo = Prestamo(usuario, libro, dias)
            self.prestamos.append(prestamo)
            return True
        return False

    def devolver_libro(self, usuario, libro):
        for prestamo in self.prestamos:
            if prestamo.usuario == usuario and prestamo.libro == libro:
                usuario.remover_prestamo(libro)
                libro.devolver()
                self.prestamos.remove(prestamo)
                return True
        return False

    def consultar_prestamos_usuario(self, usuario):
        return [prestamo for prestamo in self.prestamos if prestamo.usuario == usuario]