from bd import BD
from prestamo import Prestamo
from datetime import datetime
import unicodedata

class Biblioteca:
    """
    Clase principal que gestiona las operaciones de la biblioteca.
    
    Atributos:
        bd (BD): Instancia de la base de datos.
    """
    
    def __init__(self):
        """Inicializa la biblioteca con una instancia de BD."""
        self.bd = BD()
    
    @staticmethod
    def normalizar_texto(texto):
        """Elimina tildes y convierte a minúsculas para búsquedas insensibles"""
        texto = unicodedata.normalize('NFD', texto.lower())
        texto = ''.join(c for c in texto if not unicodedata.combining(c))
        return texto
    
    def listar_libros_disponibles(self):
        """Lista todos los libros disponibles con formato de tabla mejorado"""
        disponibles = [libro for libro in self.bd.libros.values() if libro.esta_disponible()]
        
        if not disponibles:
            print("\n⚠️ No hay libros disponibles en este momento.")
            return
        
        print("\n" + " LIBROS DISPONIBLES ".center(105, '─'))
        print(f"{'No.':<4} {'Código':<8} {'Título':<30} {'Autor':<25} {'Área':<20} {'Disponibles'}")
        print("-"*105)
        
        for i, libro in enumerate(disponibles, 1):
            disp = f"{libro.disponibles}/{libro.unidades}"
            print(f"{i:<4} {libro.codigo:<8} {libro.titulo[:28]:<30} {libro.autor[:23]:<25} {libro.area[:18]:<20} {disp}")
        
        print("─"*105)
    
    def listar_areas_tematicas(self):
        """Lista todas las áreas temáticas disponibles con conteo de libros"""
        areas = list(set(libro.area for libro in self.bd.libros.values()))
        
        if not areas:
            print("\n⚠️ No hay áreas temáticas registradas.")
            return
        
        # Conteo de libros por área
        conteo = {}
        for libro in self.bd.libros.values():
            conteo[libro.area] = conteo.get(libro.area, 0) + 1
        
        print("\n" + " ÁREAS TEMÁTICAS DISPONIBLES ".center(50, '─'))
        for i, area in enumerate(sorted(areas), 1):
            print(f"{i}. {area} ({conteo[area]} libro{'s' if conteo[area] > 1 else ''})")
        print("─"*50)
    
    def consultar_libros(self, criterio, valor):
        """
        Consulta libros según un criterio específico con formato mejorado.
        
        Args:
            criterio (str): 'titulo', 'autor' o 'area'.
            valor (str): Valor a buscar.
        """
        valor_norm = self.normalizar_texto(valor)
        
        if criterio == 'titulo':
            resultados = [libro for libro in self.bd.libros.values() 
                            if valor_norm in self.normalizar_texto(libro.titulo)]
        elif criterio == 'autor':
            resultados = [libro for libro in self.bd.libros.values() 
                            if valor_norm in self.normalizar_texto(libro.autor)]
        elif criterio == 'area':
            resultados = [libro for libro in self.bd.libros.values() 
                            if valor_norm in self.normalizar_texto(libro.area)]
        else:
            print("\n⚠️ Criterio de búsqueda no válido.")
            return
        
        if not resultados:
            print(f"\n🔍 No se encontraron libros con {criterio} '{valor}'.")
            return
        
        print("\n" + f" RESULTADOS DE BÚSQUEDA ({criterio.upper()}: '{valor}') ".center(105, '─'))
        print(f"{'No.':<4} {'Código':<8} {'Título':<30} {'Autor':<25} {'Área':<20} {'Disponibles'}")
        print("-"*105)
        
        for i, libro in enumerate(resultados, 1):
            disp = f"{libro.disponibles}/{libro.unidades}"
            print(f"{i:<4} {libro.codigo:<8} {libro.titulo[:28]:<30} {libro.autor[:23]:<25} {libro.area[:18]:<20} {disp}")
        
        print("─"*105)
    
    def listar_usuarios(self):
        """Lista todos los usuarios con información de préstamos"""
        usuarios = list(self.bd.usuarios.values())
        
        if not usuarios:
            print("\n⚠️ No hay usuarios registrados.")
            return
        
        print("\n" + " USUARIOS REGISTRADOS ".center(80, '─'))
        print(f"{'No.':<4} {'Nombre':<25} {'ID':<10} {'Tipo':<12} {'Préstamos Activos'}")
        print("-"*80)
        
        for i, usuario in enumerate(usuarios, 1):
            activos = len([p for p in self.bd.prestamos if not p.devuelto and p.usuario.identificador == usuario.identificador])
            print(f"{i:<4} {usuario.nombre[:23]:<25} {usuario.identificador:<10} "
                    f"{usuario.tipo.capitalize():<12} {activos}")
        
        print("─"*80)
    
    def buscar_usuario(self, criterio, valor):
        """
        Busca usuarios por nombre o ID con búsqueda insensible.
        
        Args:
            criterio (str): 'nombre' o 'identificador'
            valor (str): Valor a buscar
        """
        valor_norm = self.normalizar_texto(valor)
        resultados = []
        
        if criterio == 'nombre':
            resultados = [usuario for usuario in self.bd.usuarios.values() 
                            if valor_norm in self.normalizar_texto(usuario.nombre)]
        elif criterio == 'identificador':
            usuario = next((u for u in self.bd.usuarios.values() 
                            if self.normalizar_texto(u.identificador) == valor_norm), None)
            if usuario:
                resultados = [usuario]
        else:
            print("\n⚠️ Criterio no válido. Use 'nombre' o 'identificador'.")
            return
        
        if not resultados:
            print(f"\n🔍 No se encontraron usuarios con {criterio} '{valor}'.")
            return
        
        print("\n" + f" RESULTADOS DE BÚSQUEDA ({criterio.upper()}: '{valor}') ".center(70, '─'))
        for i, usuario in enumerate(resultados, 1):
            activos = len([p for p in self.bd.prestamos if not p.devuelto and p.usuario.identificador == usuario.identificador])
            print(f"\n{i}. {usuario.nombre} ({usuario.identificador})")
            print(f"   Tipo: {usuario.tipo.capitalize()}")
            print(f"   Préstamos activos: {activos}")
        print("─"*70)
    
    def realizar_prestamo(self, identificador_usuario, codigo_libro):
        """Realiza un préstamo con validaciones mejoradas"""
        try:
            # Validar usuario
            usuario = next((u for u in self.bd.usuarios.values() 
                            if self.normalizar_texto(u.identificador) == self.normalizar_texto(identificador_usuario)), None)
            if not usuario:
                raise ValueError("Usuario no encontrado.")
            
            # Validar libro
            libro = self.bd.libros.get(codigo_libro)
            if not libro:
                raise ValueError("Libro no encontrado.")
            
            # Validar disponibilidad
            if not libro.esta_disponible():
                raise ValueError("No hay unidades disponibles de este libro.")
            
            # Validar límite de préstamos
            prestamos_activos = len([p for p in usuario.libros_prestados if not p.devuelto])
            limite = 5 if usuario.tipo == "profesor" else 3
            if prestamos_activos >= limite:
                raise ValueError(f"Límite de préstamos alcanzado ({limite} libros).")
            
            # Validar si ya tiene el libro
            if any(p.libro.codigo == codigo_libro and not p.devuelto for p in usuario.libros_prestados):
                raise ValueError("El usuario ya tiene este libro prestado.")
            
            # Crear préstamo
            dias_prestamo = 14 if usuario.tipo == "profesor" else 7
            prestamo = Prestamo(usuario, libro, dias_prestamo)
            
            # Registrar
            libro.prestar()
            usuario.agregar_prestamo(prestamo)
            self.bd.agregar_prestamo(prestamo)
            
            print(f"\n✅ Préstamo registrado exitosamente:")
            print(f"   Libro: {libro.titulo}")
            print(f"   Usuario: {usuario.nombre}")
            print(f"   Fecha de devolución: {prestamo.fecha_devolucion.strftime('%d/%m/%Y')}")
            return True
            
        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
            return False
    
    def devolver_libro(self, identificador_usuario, codigo_libro):
        """Registra la devolución de un libro con validaciones"""
        try:
            # Validar usuario
            usuario = next((u for u in self.bd.usuarios.values() 
                            if self.normalizar_texto(u.identificador) == self.normalizar_texto(identificador_usuario)), None)
            if not usuario:
                raise ValueError("Usuario no encontrado.")
            
            # Buscar préstamo activo
            prestamo = next((p for p in usuario.libros_prestados 
                            if p.libro.codigo == codigo_libro and not p.devuelto), None)
            
            if not prestamo:
                raise ValueError("No se encontró un préstamo activo con estos datos.")
            
            # Registrar devolución
            prestamo.libro.devolver()
            prestamo.devolver()
            usuario.remover_prestamo(prestamo)
            
            # Mensaje según estado
            if prestamo.esta_vencido():
                print("\n⚠️ Libro devuelto con retraso.")
            else:
                print("\n✅ Libro devuelto exitosamente.")
            
            print(f"   Libro: {prestamo.libro.titulo}")
            print(f"   Usuario: {usuario.nombre}")
            return True
            
        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
            return False
    
    def consultar_prestamos_usuario(self, identificador_usuario):
        """Muestra los préstamos activos de un usuario con formato mejorado"""
        try:
            usuario = next((u for u in self.bd.usuarios.values() 
                            if self.normalizar_texto(u.identificador) == self.normalizar_texto(identificador_usuario)), None)
            if not usuario:
                raise ValueError("Usuario no encontrado.")
            
            prestamos = [p for p in usuario.libros_prestados if not p.devuelto]
            
            if not prestamos:
                print(f"\nℹ️ {usuario.nombre} no tiene libros prestados actualmente.")
                return
            
            print("\n" + f" PRÉSTAMOS ACTIVOS DE {usuario.nombre.upper()} ".center(105, '─'))
            print(f"{'No.':<4} {'Código':<8} {'Título':<30} {'Fecha Préstamo':<15} {'Fecha Devolución':<15} {'Estado'}")
            print("-"*105)
            
            for i, p in enumerate(prestamos, 1):
                estado = "VENCIDO" if p.esta_vencido() else "En plazo"
                print(f"{i:<4} {p.libro.codigo:<8} {p.libro.titulo[:28]:<30} "
                        f"{p.fecha_prestamo.strftime('%d/%m/%Y'):<15} "
                        f"{p.fecha_devolucion.strftime('%d/%m/%Y'):<15} "
                        f"{estado}")
            
            print("─"*105)
            
        except ValueError as e:
            print(f"\n❌ Error: {str(e)}")
    
    def consultar_estado_usuario(self, identificador_usuario):
        """Muestra información detallada del usuario"""
        self.consultar_prestamos_usuario(identificador_usuario)