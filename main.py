from biblioteca import Biblioteca
import os
import sys

class VolverAMenu(Exception):
    """Excepción personalizada para regresar al menú principal"""
    pass

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_titulo_seccion(titulo):
    """Muestra un título de sección con formato"""
    print("\n" + "="*105)
    print(f"✨ {titulo.upper()} ✨".center(105))
    print("="*105 + "\n")

def input_con_volver(prompt):
    """Permite al usuario escribir 'volver' para regresar al menú"""
    user_input = input(f"\n{prompt} (o 'volver' para regresar): ")
    if user_input.lower() == 'volver':
        raise VolverAMenu()
    return user_input

def mostrar_menu():
    """Muestra el menú principal con diseño mejorado"""
    print("\n" + "="*105)
    print("      📚  SISTEMA DE GESTIÓN DE BIBLIOTECA  📚".center(105))
    print("="*105)
    
    opciones = [
        "Listar libros disponibles",
        "Buscar libros por título",
        "Buscar libros por autor",
        "Listar áreas temáticas",
        "Buscar libros por área",
        "Listar todos los usuarios",
        "Buscar usuario por nombre",
        "Buscar usuario por ID",
        "Realizar préstamo de libro",
        "Devolver libro prestado",
        "Consultar préstamos de usuario",
        "Consultar estado de usuario",
        "Salir del sistema"
    ]
    
    for i, opcion in enumerate(opciones, 1):
        print(f"{i:>2}. {opcion}")
    
    print("="*105)

def confirmar_accion(prompt):
    """Solicita confirmación al usuario (s/n)"""
    while True:
        resp = input(f"\n{prompt} (s/n): ").lower()
        if resp in ['s', 'n']:
            return resp == 's'
        print("Por favor ingrese 's' o 'n'.")

def main():
    """Función principal del sistema"""
    biblioteca = Biblioteca()
    
    while True:
        try:
            limpiar_pantalla()
            mostrar_menu()
            opcion = input("\nSeleccione una opción (1-13): ")
            
            if not opcion.isdigit() or not (1 <= int(opcion) <= 13):
                print("\n⚠️ Error: Ingrese un número entre 1 y 13.")
                input("\nPresione Enter para continuar...")
                continue
                
            opcion = int(opcion)
            
            # Opción 1: Listar libros disponibles
            if opcion == 1:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("libros disponibles")
                        biblioteca.listar_libros_disponibles()
                        input("\nPresione Enter para volver al menú...")
                        break
                    except VolverAMenu:
                        break
            
            # Opción 2: Buscar libros por título
            elif opcion == 2:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("buscar libros por título")
                        titulo = input_con_volver("Ingrese el título a buscar")
                        biblioteca.consultar_libros('titulo', titulo)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 3: Buscar libros por autor
            elif opcion == 3:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("buscar libros por autor")
                        autor = input_con_volver("Ingrese el autor a buscar")
                        biblioteca.consultar_libros('autor', autor)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 4: Listar áreas temáticas
            elif opcion == 4:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("áreas temáticas disponibles")
                        biblioteca.listar_areas_tematicas()
                        input("\nPresione Enter para volver al menú...")
                        break
                    except VolverAMenu:
                        break
            
            # Opción 5: Buscar libros por área
            elif opcion == 5:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("buscar libros por área")
                        area = input_con_volver("Ingrese el área temática a buscar")
                        biblioteca.consultar_libros('area', area)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 6: Listar usuarios
            elif opcion == 6:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("usuarios registrados")
                        biblioteca.listar_usuarios()
                        input("\nPresione Enter para volver al menú...")
                        break
                    except VolverAMenu:
                        break
            
            # Opción 7: Buscar usuario por nombre
            elif opcion == 7:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("buscar usuario por nombre")
                        nombre = input_con_volver("Ingrese el nombre a buscar")
                        biblioteca.buscar_usuario('nombre', nombre)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 8: Buscar usuario por ID
            elif opcion == 8:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("buscar usuario por ID")
                        identificador = input_con_volver("Ingrese el ID del usuario")
                        biblioteca.buscar_usuario('identificador', identificador)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 9: Realizar préstamo
            elif opcion == 9:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("realizar préstamo")
                        usuario_id = input_con_volver("Ingrese el ID del usuario")
                        codigo_libro = input_con_volver("Ingrese el código del libro")
                        biblioteca.realizar_prestamo(usuario_id, codigo_libro)
                        
                        if confirmar_accion("¿Desea realizar otro préstamo?"):
                            continue
                        break
                    except VolverAMenu:
                        break
            
            # Opción 10: Devolver libro
            elif opcion == 10:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("devolver libro")
                        usuario_id = input_con_volver("Ingrese el ID del usuario")
                        codigo_libro = input_con_volver("Ingrese el código del libro")
                        biblioteca.devolver_libro(usuario_id, codigo_libro)
                        
                        if confirmar_accion("¿Desea devolver otro libro?"):
                            continue
                        break
                    except VolverAMenu:
                        break
            
            # Opción 11: Consultar préstamos de usuario
            elif opcion == 11:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("préstamos de usuario")
                        usuario_id = input_con_volver("Ingrese el ID del usuario")
                        biblioteca.consultar_prestamos_usuario(usuario_id)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 12: Consultar estado de usuario
            elif opcion == 12:
                while True:
                    try:
                        limpiar_pantalla()
                        mostrar_titulo_seccion("estado de usuario")
                        usuario_id = input_con_volver("Ingrese el ID del usuario")
                        # Esta función sería similar a consultar_prestamos pero más detallada
                        biblioteca.consultar_prestamos_usuario(usuario_id)
                        input("\nPresione Enter para continuar...")
                    except VolverAMenu:
                        break
            
            # Opción 13: Salir
            elif opcion == 13:
                limpiar_pantalla()
                mostrar_titulo_seccion("saliendo del sistema")
                print("¡Gracias por usar el Sistema de Gestión de Biblioteca!".center(105))
                print("\nHasta pronto 👋".center(105))
                print("="*105)
                sys.exit(0)
        
        except KeyboardInterrupt:
            print("\n\nOperación cancelada por el usuario.")
            input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    try:
        main() # Llama a la función principal para iniciar el programa        
    except KeyboardInterrupt:
        # Si se interrumpe la ejecución (Ctrl+C), muestra un mensaje de salida
        print("\nHas abandonado el sistema de gestion de la biblioteca.")