class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    
    Atributos:
        nombre (str): Nombre completo del usuario.
        identificador (str): Identificador único del usuario.
        tipo (str): Tipo de usuario (estudiante/profesor).
        libros_prestados (list): Lista de libros actualmente prestados.
    """
    
    def __init__(self, nombre, identificador, tipo):
        """
        Inicializa un nuevo usuario con los datos proporcionados.
        
        Args:
            nombre (str): Nombre completo.
            identificador (str): ID único.
            tipo (str): Tipo de usuario (estudiante/profesor).
        """
        self.nombre = nombre
        self.identificador = identificador
        self.tipo = tipo.lower()
        self.libros_prestados = []
        
    def __str__(self):
        """Representación en string del usuario."""
        return f"Usuario: {self.nombre} ({self.identificador}) - Tipo: {self.tipo}"
    
    def puede_prestar(self):
        """
        Verifica si el usuario puede pedir prestado otro libro.
        
        Returns:
            bool: True si puede prestar (menos de 3 libros), False en caso contrario.
        """
        return len(self.libros_prestados) < 3
    
    def agregar_prestamo(self, prestamo):
        """Agrega un préstamo a la lista de libros prestados del usuario."""
        if self.puede_prestar():
            self.libros_prestados.append(prestamo)
            return True
        return False
    
    def remover_prestamo(self, prestamo):
        """Remueve un préstamo de la lista de libros prestados del usuario."""
        if prestamo in self.libros_prestados:
            self.libros_prestados.remove(prestamo)
            return True
        return False
    
    def tiene_libro(self, codigo_libro):
        """Verifica si el usuario tiene prestado un libro específico."""
        for prestamo in self.libros_prestados:
            if prestamo.libro.codigo == codigo_libro:
                return True
        return False
    
    def obtener_limite_prestamos(self):
        """Devuelve el límite de préstamos según tipo de usuario"""
        return 5 if self.tipo == "profesor" else 3  # Profesores pueden más libros
    
    def puede_prestar(self):
        """Verifica si el usuario puede pedir prestado otro libro"""
        return len(self.libros_prestados) < self.obtener_limite_prestamos()
    
    def obtener_libros_prestados(self):
        """Devuelve información de libros prestados"""
        return [{
            'codigo': p.libro.codigo,
            'titulo': p.libro.titulo,
            'fecha_prestamo': p.fecha_prestamo.strftime('%d/%m/%Y'),
            'fecha_devolucion': p.fecha_devolucion.strftime('%d/%m/%Y'),
            'vencido': p.esta_vencido()
        } for p in self.libros_prestados if not p.devuelto]