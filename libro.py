class Libro:
    def __init__(self, titulo, autor, anio, genero, codigo, ejemplares, disponibles):
        """
        Constructor de la clase Libro.
        Inicializa los atributos del libro con los valores proporcionados.
        """
        self._titulo = titulo  # Título del libro.
        self._autor = autor  # Autor del libro.
        self._anio = anio  # Año de publicación del libro.
        self._genero = genero  # Género literario del libro.
        self._codigo = codigo  # Código único que identifica al libro.
        self._ejemplares = ejemplares  # Número total de ejemplares del libro.
        self._disponibles = disponibles  # Número de ejemplares disponibles para préstamo.

    def prestar(self):
        """
        Reduce en 1 el número de ejemplares disponibles si hay ejemplares disponibles.
        Retorna True si el préstamo se realizó con éxito, de lo contrario False.
        """
        if self._disponibles > 0:  # Verifica si hay ejemplares disponibles.
            self._disponibles -= 1  # Reduce en 1 los ejemplares disponibles.
            return True  # Indica que el préstamo fue exitoso.
        return False  # Indica que no hay ejemplares disponibles para préstamo.

    def devolver(self):
        """
        Incrementa en 1 el número de ejemplares disponibles si no supera el total de ejemplares.
        """
        if self._disponibles < self._ejemplares:  # Verifica que no se exceda el total de ejemplares.
            self._disponibles += 1  # Incrementa en 1 los ejemplares disponibles.

    def __str__(self):
        """
        Retorna una representación en cadena del libro, mostrando su código, título, autor,
        año de publicación, género y la cantidad de ejemplares disponibles.
        """
        return f"{self._codigo} - {self._titulo} - {self._autor} ({self._anio}) [{self._genero}] ({self._disponibles}/{self._ejemplares} disponibles)"

    # Getters y Setters
    @property
    def titulo(self):
        """
        Getter para el atributo 'titulo'.
        Retorna el título del libro.
        """
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        """
        Setter para el atributo 'titulo'.
        Permite actualizar el título del libro.
        """
        self._titulo = nuevo_titulo

    @property
    def autor(self):
        """
        Getter para el atributo 'autor'.
        Retorna el autor del libro.
        """
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor):
        """
        Setter para el atributo 'autor'.
        Permite actualizar el autor del libro.
        """
        self._autor = nuevo_autor

    @property
    def anio(self):
        """
        Getter para el atributo 'anio'.
        Retorna el año de publicación del libro.
        """
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio):
        """
        Setter para el atributo 'anio'.
        Permite actualizar el año de publicación del libro.
        """
        self._anio = nuevo_anio

    @property
    def genero(self):
        """
        Getter para el atributo 'genero'.
        Retorna el género literario del libro.
        """
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero):
        """
        Setter para el atributo 'genero'.
        Permite actualizar el género literario del libro.
        """
        self._genero = nuevo_genero

    @property
    def codigo(self):
        """
        Getter para el atributo 'codigo'.
        Retorna el código único del libro.
        """
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        """
        Setter para el atributo 'codigo'.
        Permite actualizar el código único del libro.
        """
        self._codigo = nuevo_codigo

    @property
    def ejemplares(self):
        """
        Getter para el atributo 'ejemplares'.
        Retorna el número total de ejemplares del libro.
        """
        return self._ejemplares

    @ejemplares.setter
    def ejemplares(self, nuevos_ejemplares):
        """
        Setter para el atributo 'ejemplares'.
        Permite actualizar el número total de ejemplares del libro.
        """
        self._ejemplares = nuevos_ejemplares

    @property
    def disponibles(self):
        """
        Getter para el atributo 'disponibles'.
        Retorna el número de ejemplares disponibles para préstamo.
        """
        return self._disponibles

    @disponibles.setter
    def disponibles(self, nuevos_disponibles):
        """
        Setter para el atributo 'disponibles'.
        Permite actualizar el número de ejemplares disponibles para préstamo.
        """
        self._disponibles = nuevos_disponibles