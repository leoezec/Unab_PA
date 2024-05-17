class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"


class Libro:
    def __init__(self, titulo, autor, isbn, paginas, edicion, editorial, lugar, fecha_edicion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.lugar = lugar  # lugar ahora es una tupla (ciudad, país)
        self.fecha_edicion = fecha_edicion

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_isbn(self):
        return self.isbn

    def get_paginas(self):
        return self.paginas

    def get_edicion(self):
        return self.edicion

    def get_editorial(self):
        return self.editorial

    def get_lugar(self):
        return self.lugar

    def get_fecha_edicion(self):
        return self.fecha_edicion

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def set_isbn(self, nuevo_isbn):
        self.isbn = nuevo_isbn

    def set_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas

    def set_edicion(self, nueva_edicion):
        self.edicion = nueva_edicion

    def set_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial

    def set_lugar(self, nueva_ciudad, nuevo_pais):
        self.lugar = (nueva_ciudad, nuevo_pais)

    def set_fecha_edicion(self, nueva_fecha_edicion):
        self.fecha_edicion = nueva_fecha_edicion

    def leer_informacion(self):
        # Aquí podrías leer la información desde algún lugar, como una base de datos o un archivo
        pass

    def mostrar_informacion(self):
        ciudad, pais = self.lugar
        return f"Título: {self.titulo} {self.edicion} edición\n" \
               f"Autor: {self.autor}\n" \
               f"ISBN: {self.isbn}\n" \
               f"{self.editorial}, {ciudad} ({pais})\n" \
               f"{self.fecha_edicion}\n" \
               f"{self.paginas} páginas"


# Ejemplo de uso
autor = Persona("Y. Daniel", "Liang")
libro = Libro("Introduction to Java Programming", autor, "0-13-031997-X", 784, "3a.", "Prentice-Hall", ("New Jersey", "USA"), "viernes 16 de noviembre de 2001")
print(libro.mostrar_informacion())
