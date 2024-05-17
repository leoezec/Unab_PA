#clase Canción

class Cancion():
    def __init__(self,titulo,autor) -> None:
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    

    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self,nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self,nuevo_autor):
        self.autor = nuevo_autor

  
mi_cancion = Cancion('Bohemian Rapsody ','Queen ')
print(mi_cancion)

