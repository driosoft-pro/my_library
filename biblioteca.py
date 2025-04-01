from bd import BD
from prestamo import Prestamo

class Biblioteca:
    """
    Clase principal que gestiona las operaciones de la biblioteca.
    
    Atributos:
        bd (BD): Instancia de la base de datos.
    """
    
    def __init__(self):
        """Inicializa la biblioteca con una instancia de BD."""
        self.bd = BD()
    
    def listar_libros_disponibles(self):
        """Versión mejorada del listado de libros"""
        disponibles = [libro for libro in self.bd.libros.values() if libro.esta_disponible()]
        
        if not disponibles:
            print("No hay libros disponibles en este momento.")
            return
        
        print("\n" + " LIBROS DISPONIBLES ".center(90, '─'))
        print(f"{'No.':<4} {'Título':<30} {'Autor':<25} {'Área':<15} {'Disponibles'}")
        print("-"*90)
        
        for i, libro in enumerate(disponibles, 1):
            disp = f"{libro.disponibles}/{libro.unidades}"
            print(f"{i:<4} {libro.titulo[:28]:<30} {libro.autor[:23]:<25} {libro.area[:13]:<15} {disp}")
        
        print("─"*90 + "\n")

    def consultar_libros(self, criterio, valor):
        """
        Consulta libros según un criterio específico.
        
        Args:
            criterio (str): 'titulo', 'autor' o 'area'.
            valor (str): Valor a buscar.
        """
        if criterio == 'titulo':
            resultados = self.bd.obtener_libros_por_titulo(valor)
        elif criterio == 'autor':
            resultados = self.bd.obtener_libros_por_autor(valor)
        elif criterio == 'area':
            resultados = self.bd.obtener_libros_por_area(valor)
        else:
            print("Criterio de búsqueda no válido.")
            return
        
        if not resultados:
            print(f"No se encontraron libros con ese {criterio}.")
            return
        
        print(f"\nResultados de búsqueda por {criterio} '{valor}':")
        for i, libro in enumerate(resultados, 1):
            print(f"{i}. {libro.titulo} ({libro.autor}) - Área: {libro.area} - Disponibles: {libro.disponibles}/{libro.unidades}")
    
    def devolver_libro(self, identificador_usuario, codigo_libro):
        """
        Registra la devolución de un libro prestado.
        
        Args:
            identificador_usuario (str): ID del usuario.
            codigo_libro (str): Código del libro a devolver.
        """
        # Verificar que el usuario existe
        usuario = self.bd.usuarios.get(identificador_usuario)
        if not usuario:
            print("Usuario no encontrado.")
            return False
        
        # Buscar el préstamo activo
        prestamo = None
        for p in self.bd.prestamos:
            if (p.usuario.identificador == identificador_usuario and 
                p.libro.codigo == codigo_libro and 
                not p.devuelto):
                prestamo = p
                break
        
        if not prestamo:
            print("No se encontró un préstamo activo con esos datos.")
            return False
        
        # Registrar la devolución
        if prestamo.libro.devolver() and usuario.remover_prestamo(prestamo) and prestamo.devolver():
            self.bd.remover_prestamo(prestamo)
            
            if prestamo.esta_vencido():
                print("Libro devuelto con éxito, pero con retraso.")
            else:
                print("Libro devuelto con éxito.")
            return True
        
        print("Error al registrar la devolución.")
        return False
    
    def consultar_prestamos_usuario(self, identificador_usuario):
        """Muestra los préstamos activos de un usuario."""
        # Verificar que el usuario existe
        if identificador_usuario not in self.bd.usuarios:
            print("Usuario no encontrado.")
            return
        
        prestamos = self.bd.obtener_prestamos_usuario(identificador_usuario)
        
        if not prestamos:
            print("El usuario no tiene libros prestados actualmente.")
            return
        
        usuario = self.bd.usuarios[identificador_usuario]
        print(f"\nLibros prestados a {usuario.nombre}:")
        for i, prestamo in enumerate(prestamos, 1):
            estado = "VENCIDO" if prestamo.esta_vencido() else "En plazo"
            print(f"{i}. {prestamo.libro.titulo} - Devuelve: {prestamo.fecha_devolucion.strftime('%d/%m/%Y')} ({estado})")
            
    def verificar_disponibilidad(self, codigo_libro):
        """Verifica disponibilidad de un libro"""
        libro = self.bd.libros.get(codigo_libro)
        if not libro:
            return {'disponible': False, 'mensaje': 'Libro no encontrado'}
        if not libro.esta_disponible():
            return {'disponible': False, 'mensaje': 'No hay unidades disponibles'}
        return {'disponible': True, 'libro': libro.obtener_info_prestamo()}

    def verificar_usuario(self, identificador_usuario):
        """Verifica estado de un usuario"""
        usuario = self.bd.usuarios.get(identificador_usuario)
        if not usuario:
            return {'valido': False, 'mensaje': 'Usuario no encontrado'}
        return {
            'valido': True,
            'usuario': usuario,
            'puede_prestar': usuario.puede_prestar(),
            'limite': usuario.obtener_limite_prestamos(),
            'prestamos_actuales': len(usuario.libros_prestados)
        }

    def realizar_prestamo(self, identificador_usuario, codigo_libro):
        """Versión mejorada con validación completa"""
        # Verificar usuario
        usuario_info = self.verificar_usuario(identificador_usuario)
        if not usuario_info['valido']:
            print(usuario_info['mensaje'])
            return False
        
        # Verificar libro
        libro_info = self.verificar_disponibilidad(codigo_libro)
        if not libro_info['disponible']:
            print(libro_info['mensaje'])
            return False
        
        usuario = usuario_info['usuario']
        libro = self.bd.libros[codigo_libro]
        
        # Verificar si ya tiene el libro prestado
        if usuario.tiene_libro(codigo_libro):
            print("El usuario ya tiene este libro prestado.")
            return False
        
        # Verificar límite de préstamos
        if not usuario_info['puede_prestar']:
            print(f"Límite de préstamos alcanzado ({usuario_info['limite']} libros).")
            return False
        
        # Crear y registrar el préstamo
        prestamo = Prestamo(usuario, libro, 14 if usuario.tipo == "profesor" else 7)  # Más días para profesores
        
        if libro.prestar() and usuario.agregar_prestamo(prestamo):
            self.bd.agregar_prestamo(prestamo)
            print(f"Préstamo exitoso. Devolver antes de: {prestamo.fecha_devolucion.strftime('%d/%m/%Y')}")
            print(f"Libros prestados: {len(usuario.libros_prestados)}/{usuario_info['limite']}")
            return True
        
        print("Error al procesar el préstamo.")
        return False

    def consultar_estado_usuario(self, identificador_usuario):
        """Muestra información detallada del usuario"""
        usuario_info = self.verificar_usuario(identificador_usuario)
        if not usuario_info['valido']:
            print(usuario_info['mensaje'])
            return
        
        usuario = usuario_info['usuario']
        print(f"\nEstado de {usuario.nombre} ({usuario.identificador}):")
        print(f"Tipo: {usuario.tipo}")
        print(f"Préstamos: {len(usuario.libros_prestados)}/{usuario_info['limite']}")
        
        if usuario.libros_prestados:
            print("\nLibros prestados actualmente:")
            for i, libro in enumerate(usuario.obtener_libros_prestados(), 1):
                estado = "VENCIDO" if libro['vencido'] else "En plazo"
                print(f"{i}. {libro['titulo']} (Devuelve: {libro['fecha_devolucion']}) [{estado}]")
                
    def listar_usuarios(self):
        """Versión mejorada del listado de usuarios"""
        usuarios = self.bd.listar_usuarios()
        
        if not usuarios:
            print("No hay usuarios registrados en el sistema.")
            return
        
        print("\n" + " USUARIOS REGISTRADOS ".center(90, '─'))
        print(f"{'No.':<4} {'Nombre':<25} {'ID':<10} {'Tipo':<12} {'Préstamos Activos'}")
        print("-"*90)
        
        for i, usuario in enumerate(usuarios, 1):
            prestamos = len([p for p in self.bd.prestamos 
                            if p.usuario.identificador == usuario.identificador 
                            and not p.devuelto])
            print(f"{i:<4} {usuario.nombre[:23]:<25} {usuario.identificador:<10} "
                    f"{usuario.tipo.capitalize():<12} {prestamos}")
        
        print("─"*90 + "\n")

    def buscar_usuario(self, criterio, valor):
        """
        Busca usuarios según criterio
        Args:
            criterio: 'nombre' o 'identificador'
            valor: valor a buscar
        """
        if criterio == 'nombre':
            resultados = self.bd.buscar_usuario_por_nombre(valor)
        elif criterio == 'identificador':
            usuario = self.bd.buscar_usuario_por_identificador(valor)
            resultados = [usuario] if usuario else []
        else:
            print("Criterio de búsqueda no válido.")
            return
        
        if not resultados:
            print(f"No se encontraron usuarios con ese {criterio}.")
            return
        
        print(f"\nResultados de búsqueda por {criterio} '{valor}':")
        for i, usuario in enumerate(resultados, 1):
            prestamos = len([p for p in self.bd.prestamos if p.usuario.identificador == usuario.identificador and not p.devuelto])
            print(f"{i}. {usuario.nombre} ({usuario.identificador}) - Tipo: {usuario.tipo} - Préstamos activos: {prestamos}")
            
    def listar_areas_tematicas(self):
        """Lista todas las áreas temáticas disponibles"""
        areas = self.bd.obtener_areas_tematicas()
        if not areas:
            print("No hay áreas temáticas registradas.")
            return
        
        print("\nÁreas temáticas disponibles:")
        for i, area in enumerate(sorted(areas), 1):
            print(f"{i}. {area}")
        
        # Mostrar conteo de libros por área
        print("\nCantidad de libros por área:")
        conteo_areas = {}
        for libro in self.bd.libros.values():
            conteo_areas[libro.area] = conteo_areas.get(libro.area, 0) + 1
        
        for area, cantidad in sorted(conteo_areas.items()):
            print(f"- {area}: {cantidad} libro(s)")