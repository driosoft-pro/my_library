class Libro:
    def __init__(self, titulo, autor, anio, genero, codigo, ejemplares, disponibles):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._genero = genero
        self._codigo = codigo
        self._ejemplares = ejemplares
        self._disponibles = disponibles

    def prestar(self):
        if self._disponibles > 0:
            self._disponibles -= 1
            return True
        return False

    def devolver(self):
        if self._disponibles < self._ejemplares:
            self._disponibles += 1

    def __str__(self):
        return f"{self._codigo} - {self._titulo} - {self._autor} ({self._anio}) [{self._genero}] ({self._disponibles}/{self._ejemplares} disponibles)"

    # Getters y Setters
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        self._autor = nuevo_autor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio):
        self._anio = nuevo_anio

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero):
        self._genero = nuevo_genero

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self._codigo = nuevo_codigo

    @property
    def ejemplares(self):
        return self._ejemplares

    @ejemplares.setter
    def ejemplares(self, nuevos_ejemplares):
        self._ejemplares = nuevos_ejemplares

    @property
    def disponibles(self):
        return self._disponibles

    @disponibles.setter
    def disponibles(self, nuevos_disponibles):
        self._disponibles = nuevos_disponibles