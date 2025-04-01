from biblioteca import Biblioteca
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal con un diseño mejorado"""
    print("\n" + "="*90)
    print("      📚  SISTEMA DE GESTIÓN DE BIBLIOTECA  📚".center(90))
    print("="*90)
    
    opciones = [
        "Listar libros disponibles",
        "Buscar libros por título",
        "Buscar libros por autor",
        "Listar áreas temáticas disponibles",
        "Buscar libros por área temática",
        "Listar todos los usuarios",
        "Buscar usuario por nombre",
        "Buscar usuario por identificador",
        "Realizar préstamo de libro",
        "Devolver libro prestado",
        "Consultar libros prestados por usuario",
        "Consultar estado completo de usuario",
        "Salir"
    ]
    
    for i, opcion in enumerate(opciones, 1):
        print(f"{i:>2}. {opcion}")
    
    print("="*90)

def esperar():
    input("\nPresione Enter para continuar...")

def mostrar_titulo_seccion(titulo):
    """Muestra un título de sección con formato especial"""
    print("\n" + "="*90)
    print(f"  {titulo.upper()}  ".center(0, '✨'))
    print("="*90 + "\n")
    
def main():
    """Función principal que ejecuta la aplicación."""
    biblioteca = Biblioteca()
    
    while True:
        mostrar_menu()
        try:
            opcion = input("\nSeleccione una opción (1-13): ")
            opcion = int(opcion)
            
            if opcion == 1:
                mostrar_titulo_seccion("Libros Disponibles")
                biblioteca.listar_libros_disponibles()
            
            elif opcion == 2:
                mostrar_titulo_seccion("Buscar Libros por Título")
                titulo = input("Ingrese el título a buscar: ")
                biblioteca.consultar_libros('titulo', titulo)
            
            elif opcion == 3:
                mostrar_titulo_seccion("Buscar Libros por Autor")
                autor = input("Ingrese el autor a buscar: ")
                biblioteca.consultar_libros('autor', autor)
            
            elif opcion == 4:
                mostrar_titulo_seccion("Áreas Temáticas Disponibles")
                biblioteca.listar_areas_tematicas()
            
            elif opcion == 5:
                mostrar_titulo_seccion("Buscar Libros por Área")
                area = input("Ingrese el área temática a buscar: ")
                biblioteca.consultar_libros('area', area)
            
            elif opcion == 6:
                mostrar_titulo_seccion("Listado de Usuarios")
                biblioteca.listar_usuarios()
            
            elif opcion == 7:
                mostrar_titulo_seccion("Buscar Usuario por Nombre")
                nombre = input("Ingrese el nombre a buscar: ")
                biblioteca.buscar_usuario('nombre', nombre)
            
            elif opcion == 8:
                mostrar_titulo_seccion("Buscar Usuario por ID")
                identificador = input("Ingrese el identificador a buscar: ")
                biblioteca.buscar_usuario('identificador', identificador)
            
            elif opcion == 9:
                mostrar_titulo_seccion("Realizar Préstamo")
                usuario_id = input("Ingrese el ID del usuario: ")
                codigo_libro = input("Ingrese el código del libro: ")
                biblioteca.realizar_prestamo(usuario_id, codigo_libro)
            
            elif opcion == 10:
                mostrar_titulo_seccion("Devolver Libro")
                usuario_id = input("Ingrese el ID del usuario: ")
                codigo_libro = input("Ingrese el código del libro: ")
                biblioteca.devolver_libro(usuario_id, codigo_libro)
            
            elif opcion == 11:
                mostrar_titulo_seccion("Préstamos de Usuario")
                usuario_id = input("Ingrese el ID del usuario: ")
                biblioteca.consultar_prestamos_usuario(usuario_id)
            
            elif opcion == 12:
                mostrar_titulo_seccion("Estado de Usuario")
                usuario_id = input("Ingrese el ID del usuario: ")
                biblioteca.consultar_estado_usuario(usuario_id)
            
            elif opcion == 13:
                mostrar_titulo_seccion("Saliendo del Sistema")
                print("¡Gracias por usar el Sistema de Gestión de Biblioteca!".center(90))
                print("Vuelva pronto".center(90))
                print("="*90)
                break
            
            else:
                print("\n⚠️ Opción no válida. Por favor seleccione un número entre 1 y 13.")
        
        except ValueError:
            print("\n⚠️ Error: Por favor ingrese solo números para seleccionar una opción.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()