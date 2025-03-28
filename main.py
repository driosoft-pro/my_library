from biblioteca import Biblioteca
from usuario import Usuario
from libro import Libro
from bd import BaseDatos

def mostrar_menu():
    """
    Muestra el menú principal con opciones mejoradas.
    """
    print("\n📚 === Menú Principal === 📚")
    print("1️⃣  📖 Listar libros")
    print("2️⃣  🔍 Buscar libro")
    print("3️⃣  📥 Realizar préstamo")
    print("4️⃣  📤 Devolver libro")
    print("5️⃣  📑 Consultar préstamos de un usuario")
    print("6️⃣  👥 Listar usuarios")
    print("7️⃣  🚪 Salir")

def input_validado(mensaje, tipo="texto"):
    """
    Valida la entrada del usuario según el tipo de dato esperado.
    """
    while True:
        entrada = input(f"{mensaje}: ").strip()
        
        if not entrada:
            print("⛔ Entrada no puede estar vacía. Intente de nuevo.")
            continue
        
        if tipo == "numero":
            if entrada.isdigit():
                return int(entrada)
            else:
                print("⛔ Solo se permiten números. Intente de nuevo.")
        elif tipo == "texto":
            if entrada.isalpha() or " " in entrada:
                return entrada
            else:
                print("⛔ Solo se permiten letras y espacios. Intente de nuevo.")
        else:
            return entrada  # Para otros tipos, retornar tal cual

def listar_libros(biblioteca):
    """
    Lista los libros disponibles con formato mejorado.
    """
    print("\n📚 📖 Lista de libros en la biblioteca 📖 📚")
    print("=" * 90)
    print(f"{'📑 Código':<10} {'📕 Título':<35} {'✍️ Autor':<25} {'📅 Año':<6} {'📦 Disponibles'}")
    print("=" * 90)
    for libro in biblioteca.listar_libros_disponibles():
        print(f"{libro.codigo:<10} {libro.titulo:<35} {libro.autor:<25} {libro.anio:<6} {libro.disponibles}")
    print("=" * 90)

def buscar_libro(biblioteca):
    """
    Permite buscar libros con opciones claras.
    """
    print("\n🔍 Buscar libro por:")
    print("1️⃣  Código")
    print("2️⃣  Título")
    print("3️⃣  Autor")
    print("4️⃣  Área")

    opcion_busqueda = input_validado("Seleccione una opción (1-4)", "numero")

    criterios = {1: "codigo", 2: "titulo", 3: "autor", 4: "area"}
    
    if opcion_busqueda in criterios:
        valor = input_validado(f"Ingrese el {criterios[opcion_busqueda]}")
        resultados = biblioteca.buscar_libro(criterios[opcion_busqueda], valor)

        if resultados:
            print("\n✅ Libros encontrados:")
            print("=" * 90)
            for libro in resultados:
                print(f"{libro.codigo:<10} {libro.titulo:<35} {libro.autor:<25} {libro.anio:<6} {libro.disponibles}")
            print("=" * 90)
        else:
            print("🚫 No se encontraron libros con ese criterio.")
    else:
        print("⛔ Opción inválida.")

def listar_usuarios(biblioteca):
    """
    Muestra los usuarios registrados en formato tabla.
    """
    print("\n👥 Usuarios registrados:")
    print("=" * 60)
    print(f"{'🆔 Código':<10} {'👤 Nombre':<25} {'🎓 Tipo de Usuario'}")
    print("=" * 60)
    for usuario in biblioteca.usuarios:
        print(f"{usuario.codigo:<10} {usuario.nombre:<25} {usuario.tipo_usuario:<15}")
    print("=" * 60)

def realizar_prestamo(biblioteca):
    """
    Permite realizar un préstamo con validaciones.
    """
    print("\n📥 Realizar un préstamo:")
    usuario_id = input_validado("🆔 ID del usuario")
    libro_codigo = input_validado("📖 Código del libro")
    dias = input_validado("📆 Días de préstamo (máx. 30)", "numero")

    if dias > 30:
        print("⚠️ No se pueden prestar libros por más de 30 días.")
        return
    
    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)
    libro = next((l for l in biblioteca.libros if l.codigo == libro_codigo), None)

    if usuario and libro and biblioteca.realizar_prestamo(usuario, libro, dias):
        print("✅ ¡Préstamo realizado con éxito!")
    else:
        print("🚫 No se pudo realizar el préstamo.")

def devolver_libro(biblioteca):
    """
    Permite devolver un libro con validaciones.
    """
    print("\n📤 Devolver un libro:")
    usuario_id = input_validado("🆔 ID del usuario")
    libro_codigo = input_validado("📖 Código del libro")

    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)
    libro = next((l for l in biblioteca.libros if l.codigo == libro_codigo), None)

    if usuario and libro and biblioteca.devolver_libro(usuario, libro):
        print("✅ ¡Libro devuelto con éxito!")
    else:
        print("🚫 No se pudo devolver el libro.")

def consultar_prestamos_usuario(biblioteca):
    """
    Consulta los préstamos de un usuario.
    """
    usuario_id = input_validado("🆔 ID del usuario")
    usuario = next((u for u in biblioteca.usuarios if u.identificador == usuario_id), None)

    if usuario:
        prestamos = biblioteca.consultar_prestamos_usuario(usuario)
        if prestamos:
            print("\n📑 Préstamos activos:")
            for prestamo in prestamos:
                print(f"📖 {prestamo}")
        else:
            print("ℹ️  El usuario no tiene préstamos activos.")
    else:
        print("🚫 Usuario no encontrado.")

def main():
    """
    Función principal que maneja el menú del sistema.
    """
    biblioteca = Biblioteca()
    bd = BaseDatos()
    biblioteca.libros = bd.obtener_libros()
    biblioteca.usuarios = bd.obtener_usuarios()

    while True:
        mostrar_menu()
        opcion = input_validado("Seleccione una opción", "numero")

        if opcion == 1:
            listar_libros(biblioteca)
        elif opcion == 2:
            buscar_libro(biblioteca)
        elif opcion == 3:
            realizar_prestamo(biblioteca)
        elif opcion == 4:
            devolver_libro(biblioteca)
        elif opcion == 5:
            consultar_prestamos_usuario(biblioteca)
        elif opcion == 6:
            listar_usuarios(biblioteca)
        elif opcion == 7:
            print("👋 ¡Gracias por usar la biblioteca! 📚")
            break
        else:
            print("⛔ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
