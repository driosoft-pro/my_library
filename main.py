from biblioteca import Biblioteca
from usuario import Usuario
from libro import Libro
from bd import BaseDatos  # Importar la base de datos


def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Listar libros")
    print("2. Buscar libro")
    print("3. Realizar préstamo")
    print("4. Devolver libro")
    print("5. Consultar préstamos de un usuario")
    print("6. Listar usuarios")
    print("7. Salir")


def listar_libros(biblioteca):
    print("\nLista de libros en la biblioteca:")
    print("=" * 90)
    print(f"{'Código':<8} {'Título':<35} {'Autor':<25} {'Año':<6} {'Disponibles'}")
    print("=" * 90)
    for libro in biblioteca.listar_libros_disponibles():
        print(f"{libro.codigo:<8} {libro.titulo:<35} {libro.autor:<25} {libro.anio:<6} {libro.disponibles}")
    print("=" * 90)


def buscar_libro(biblioteca):
    print("\nBuscar libro por:")
    print("1. Código")
    print("2. Título")
    print("3. Autor")
    print("4. Área")
    opcion_busqueda = input("Seleccione una opción: ")

    if opcion_busqueda == "1":
        criterio, valor = "codigo", input("Ingrese el código del libro: ").strip()
    elif opcion_busqueda == "2":
        criterio, valor = "titulo", input("Ingrese el título del libro: ").strip()
    elif opcion_busqueda == "3":
        criterio, valor = "autor", input("Ingrese el nombre del autor: ").strip()
    elif opcion_busqueda == "4":
        criterio, valor = "area", input("Ingrese el área de conocimiento: ").strip()
    else:
        print("Opción no válida.")
        return

    resultados = biblioteca.buscar_libro(criterio, valor)
    if resultados:
        print("\nLibros encontrados:")
        print("=" * 90)
        for libro in resultados:
            print(f"{libro.codigo:<8} {libro.titulo:<35} {libro.autor:<25} {libro.anio:<6} {libro.disponibles}")
        print("=" * 90)
    else:
        print("No se encontraron libros con ese criterio.")

def listar_usuarios(biblioteca):
    print("=" * 60)
    print(f"{'Código':<10} {'Nombre':<25} {'Tipo de Usuario'}")
    print("=" * 60)
    for usuario in biblioteca.usuarios:
        print(f"{usuario.codigo:<10} {usuario.nombre:<25} {usuario.tipo_usuario:<15}")
    print("=" * 60)


def realizar_prestamo(biblioteca):
    usuario_id = input("ID del usuario: ").strip()
    libro_codigo = input("Código del libro: ").strip()
    dias = int(input("Días de préstamo: "))

    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)
    libro = next((l for l in biblioteca.libros if l.codigo == libro_codigo), None)

    if usuario and libro and biblioteca.realizar_prestamo(usuario, libro, dias):
        print("Préstamo realizado con éxito.")
    else:
        print("No se pudo realizar el préstamo.")


def devolver_libro(biblioteca):
    usuario_id = input("ID del usuario: ").strip()
    libro_codigo = input("Código del libro: ").strip()

    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)
    libro = next((l for l in biblioteca.libros if l.codigo == libro_codigo), None)

    if usuario and libro and biblioteca.devolver_libro(usuario, libro):
        print("Libro devuelto con éxito.")
    else:
        print("No se pudo devolver el libro.")


def consultar_prestamos_usuario(biblioteca):
    usuario_id = input("ID del usuario: ").strip()
    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)

    if usuario:
        prestamos = biblioteca.consultar_prestamos_usuario(usuario)
        if prestamos:
            print("\nPréstamos activos:")
            for prestamo in prestamos:
                print(prestamo)
        else:
            print("El usuario no tiene préstamos activos.")
    else:
        print("Usuario no encontrado.")


def main():
    biblioteca = Biblioteca()
    bd = BaseDatos()  # Crear instancia de BaseDatos
    biblioteca.libros = bd.obtener_libros()  # Cargar libros desde la base de datos
    biblioteca.usuarios = bd.obtener_usuarios()  # Cargar usuarios desde la base de datos

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_libros(biblioteca)
        elif opcion == "2":
            buscar_libro(biblioteca)
        elif opcion == "3":
            realizar_prestamo(biblioteca)
        elif opcion == "4":
            devolver_libro(biblioteca)
        elif opcion == "5":
            consultar_prestamos_usuario(biblioteca)
        elif opcion == "6":
            listar_usuarios(biblioteca)
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()