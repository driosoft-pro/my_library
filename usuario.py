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

    def agregar_prestamo(self, prestamo):
        """
        Agrega un préstamo a la lista de préstamos del usuario si no ha alcanzado el límite.
        Retorna True si el préstamo se agregó con éxito, de lo contrario False.
        """
        if len(self.prestamos) < self.LIMITE_PRESTAMOS:  # Verifica si el usuario no ha alcanzado el límite de préstamos.
            self.prestamos.append(prestamo)  # Agrega el préstamo a la lista.
            return True  # Indica que el préstamo se agregó con éxito.
        return False  # Indica que no se pudo agregar el préstamo porque se alcanzó el límite.

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