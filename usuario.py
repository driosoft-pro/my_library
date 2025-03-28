class Usuario:
    LIMITE_PRESTAMOS = 3  # Configurable

    def __init__(self, codigo, nombre, tipo_usuario):
        self.codigo = codigo
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        self.prestamos = []

    def puede_prestar(self):
        return len(self.prestamos) < self.LIMITE_PRESTAMOS

    def agregar_prestamo(self, prestamo):
        if len(self.prestamos) < 3:
            self.prestamos.append(prestamo)
            return True
        return False

    def remover_prestamo(self, prestamo):
        self.prestamos.remove(prestamo)

    def __str__(self):
        return f"{self.nombre} ({self.tipo_usuario}) - ID: {self.codigo}"