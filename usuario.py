class Usuario:
    LIMITE_PRESTAMOS = 3  # Límite máximo de préstamos que un usuario puede tener al mismo tiempo.

    def __init__(self, codigo, nombre, tipo_usuario):
        """
        Constructor de la clase Usuario.
        Inicializa los atributos del usuario con los valores proporcionados.
        """
        self.codigo = codigo  # Código único que identifica al usuario.
        self.nombre = nombre  # Nombre del usuario.
        self.tipo_usuario = tipo_usuario  # Tipo de usuario (por ejemplo, "Estudiante" o "Profesor").
        self.prestamos = []  # Lista para almacenar los préstamos activos del usuario.

    def puede_prestar(self):
        """
        Verifica si el usuario puede realizar un nuevo préstamo.
        Retorna True si el número de préstamos actuales es menor al límite permitido, de lo contrario False.
        """
        return len(self.prestamos) < self.LIMITE_PRESTAMOS

    def agregar_prestamo(self, libro):
        """Agrega un libro a la lista de préstamos del usuario si no supera el límite."""
        if len(self.prestamos) >= 3:
            print("No puedes tomar más de 3 libros prestados a la vez.")
            return False  # Evita el préstamo si ya tiene 3 libros
        
        if libro in self.prestamos:
            print("No puedes pedir el mismo libro más de una vez.")
            return False  # Evita el préstamo duplicado

        self.prestamos.append(libro)
        return True

    def remover_prestamo(self, prestamo):
        """
        Elimina un préstamo de la lista de préstamos del usuario.
        """
        self.prestamos.remove(prestamo)  # Elimina el préstamo especificado de la lista.

    def __str__(self):
        """
        Retorna una representación en cadena del usuario.
        Muestra el nombre, tipo de usuario y código del usuario.
        """
        return f"{self.nombre} ({self.tipo_usuario}) - ID: {self.codigo}"