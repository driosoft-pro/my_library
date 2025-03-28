from biblioteca import Biblioteca  # Importa la clase Biblioteca para gestionar libros, usuarios y préstamos.
from usuario import Usuario  # Importa la clase Usuario para representar a los usuarios de la biblioteca.
from libro import Libro  # Importa la clase Libro para representar los libros de la biblioteca.
from bd import BaseDatos  # Importa la clase BaseDatos para cargar datos predefinidos de libros y usuarios.

def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles para el usuario.
    """
    print("\n=== Menú Principal ===")
    print("1. Listar libros")
    print("2. Buscar libro")
    print("3. Realizar préstamo")
    print("4. Devolver libro")
    print("5. Consultar préstamos de un usuario")
    print("6. Listar usuarios")
    print("7. Salir")

def listar_libros(biblioteca):
    """
    Lista los libros disponibles en la biblioteca.
    """
    print("\nLista de libros en la biblioteca:")
    print("=" * 90)
    print(f"{'Código':<8} {'Título':<35} {'Autor':<25} {'Año':<6} {'Disponibles'}")
    print("=" * 90)
    # Itera sobre los libros disponibles y los muestra en formato tabular.
    for libro in biblioteca.listar_libros_disponibles():
        print(f"{libro.codigo:<8} {libro.titulo:<35} {libro.autor:<25} {libro.anio:<6} {libro.disponibles}")
    print("=" * 90)

def buscar_libro(biblioteca):
    """
    Permite buscar libros en la biblioteca según diferentes criterios.
    """
    print("\nBuscar libro por:")
    print("1. Código")
    print("2. Título")
    print("3. Autor")
    print("4. Área")
    opcion_busqueda = input("Seleccione una opción: ")

    # Determina el criterio de búsqueda según la opción seleccionada.
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

    # Busca libros que coincidan con el criterio y valor proporcionados.
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
    """
    Lista los usuarios registrados en la biblioteca.
    """
    print("=" * 60)
    print(f"{'Código':<10} {'Nombre':<25} {'Tipo de Usuario'}")
    print("=" * 60)
    # Itera sobre los usuarios registrados y los muestra en formato tabular.
    for usuario in biblioteca.usuarios:
        print(f"{usuario.codigo:<10} {usuario.nombre:<25} {usuario.tipo_usuario:<15}")
    print("=" * 60)

def realizar_prestamo(biblioteca):
    """
    Permite realizar un préstamo de un libro a un usuario.
    """
    usuario_id = input("ID del usuario: ").strip()
    libro_codigo = input("Código del libro: ").strip()
    dias = int(input("Días de préstamo: "))

    # Busca al usuario y al libro en la biblioteca.
    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)
    libro = next((l for l in biblioteca.libros if l.codigo == libro_codigo), None)

    # Intenta realizar el préstamo y muestra el resultado.
    if usuario and libro and biblioteca.realizar_prestamo(usuario, libro, dias):
        print("Préstamo realizado con éxito.")
    else:
        print("No se pudo realizar el préstamo.")

def devolver_libro(biblioteca):
    """
    Permite devolver un libro prestado por un usuario.
    """
    usuario_id = input("ID del usuario: ").strip()
    libro_codigo = input("Código del libro: ").strip()

    # Busca al usuario y al libro en la biblioteca.
    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)
    libro = next((l for l in biblioteca.libros if l.codigo == libro_codigo), None)

    # Intenta devolver el libro y muestra el resultado.
    if usuario and libro and biblioteca.devolver_libro(usuario, libro):
        print("Libro devuelto con éxito.")
    else:
        print("No se pudo devolver el libro.")

def consultar_prestamos_usuario(biblioteca):
    """
    Consulta los préstamos activos de un usuario específico.
    """
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
    """
    Función principal que inicializa la biblioteca y gestiona el flujo del programa.
    """
    biblioteca = Biblioteca()  # Crea una instancia de la biblioteca.
    bd = BaseDatos()  # Crea una instancia de la base de datos.
    biblioteca.libros = bd.obtener_libros()  # Carga los libros desde la base de datos.
    biblioteca.usuarios = bd.obtener_usuarios()  # Carga los usuarios desde la base de datos.

    while True:
        mostrar_menu()  # Muestra el menú principal.
        opcion = input("Seleccione una opción: ").strip()

        # Ejecuta la acción correspondiente según la opción seleccionada.
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

# Verifica si el script se está ejecutando directamente.
if __name__ == "__main__":
    main()  # Llama a la función principal.