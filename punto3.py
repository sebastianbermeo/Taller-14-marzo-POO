class personita:
    def __init__(self,nombre,apellido,nacionalidad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nacionalidad = nacionalidad
    def saludo(self):
        print("Esta enviando un saludo")
    def bye(self):
        print("chao")
sebas = personita("sebastian","Bermeo","colombiano")
sebas.__saludo()