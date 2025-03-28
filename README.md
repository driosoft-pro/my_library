# Sistema de Gestión de Libros de Biblioteca

## Descripción
Este proyecto implementa un sistema de gestión de libros para una biblioteca, utilizando el paradigma de Programación Orientada a Objetos (POO) en Python. El sistema permite la gestión de libros, usuarios y préstamos, garantizando el cumplimiento de ciertas reglas establecidas.

## Características Principales
- **Gestor de Libros:** Permite almacenar y consultar libros por título, autor o área.
- **Gestor de Usuarios:** Administra los usuarios registrados en la biblioteca.
- **Préstamos y Devoluciones:** Realiza el préstamo y la devolución de libros con validaciones.
- **Consulta de Libros Prestados:** Permite a los usuarios ver los libros que han solicitado en préstamo.
- **Gestión de Multas:** Registra y calcula multas en caso de retrasos en la devolución de libros.
- **Historial de Préstamos:** Permite visualizar los libros prestados anteriormente por cada usuario.

## 📌 Requerimientos
El sistema cuenta con tres clases principales:

### 📚 Clase `Libro`
**Atributos:**
- `titulo`: Título del libro.
- `autor`: Autor del libro.
- `anio_publicacion`: Año de publicación.
- `area`: Área del conocimiento.
- `codigo`: Código único del libro.
- `unidades`: Cantidad total de ejemplares.
- `disponibles`: Cantidad de libros disponibles para préstamo.

### 👤 Clase `Usuario`
**Atributos:**
- `nombre`: Nombre del usuario.
- `identificador`: Código único del usuario.
- `tipo_usuario`: Tipo de usuario (estudiante o profesor).
- `libros_prestados`: Lista de libros actualmente prestados por el usuario.

### ♻️ Clase `Prestamo`
**Atributos:**
- `usuario`: Objeto de la clase `Usuario`.
- `libro`: Objeto de la clase `Libro`.
- `fecha_prestamo`: Fecha en la que se realizó el préstamo.
- `dias_prestamo`: Duración del préstamo.
- `fecha_devolucion`: Fecha límite para devolver el libro.
- `multa`: Monto de la multa en caso de devolución tardía.

## 🎯 Funcionalidades del Sistema
✅ Listar todos los libros disponibles.  
✅ Consultar libros por título, autor o área.  
✅ Realizar un préstamo de un libro.  
✅ Devolver un libro prestado.  
✅ Consultar libros prestados por un usuario.  
✅ Calcular multas en caso de retrasos en la devolución.  
✅ Generar un historial de préstamos para cada usuario.  

## 📜 Reglas del Sistema
⚠ Un libro solo puede ser prestado si hay unidades disponibles.  
⚠ Un usuario puede tener un máximo de tres libros prestados simultáneamente.  
⚠ Al devolver un libro, se verifica que la fecha de devolución sea válida.  
⚠ Si un usuario devuelve un libro después de la fecha límite, se aplicará una multa.  
⚠ Se implementan validaciones para garantizar una ejecución coherente y robusta.  

---

## 🚀 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/sistema_biblioteca.git
cd sistema_biblioteca
```

### 2️⃣ Crear y activar un entorno virtual
```bash
python -m venv venv
```

#### Para Linux/Mac:
```bash
source venv/bin/activate
```

#### Para Windows:
```bash
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el programa
```bash
python main.py
```
---

## 📊 Entregables
- 📌 **Diagrama UML** de las clases implementadas.
- 📌 **Código Python** modularizado con cada clase en un archivo independiente.
- 📌 **Implementación documentada** siguiendo las recomendaciones del PEP8.
- 📌 **Casos de prueba** para verificar el correcto funcionamiento del sistema.

---

## 🛠 Tecnologías Utilizadas
- **Python 3**
- **Programación Orientada a Objetos (POO)**

🚀 ¡Gracias por usar el sistema de gestión de biblioteca! 📚

---  

📝 **Desarrollado por:** **Deyton Riasco Ortiz**  
📅 **Fecha:** 2025  
📧 **Contacto:** [deyton007@gmail.com](mailto:deyton007@gmail.com)