#INIT
class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
persona1 = persona("Sebitas uwu",89)
persona2 = persona("Rodrigo",45)
print(persona1.nombre)
print(persona1.edad)
print(persona1.nombre)
if persona1.edad > persona2.edad:
    print(persona1.nombre + "es mayor")

#REPR/STR
class humano:
    def __init__(self,nombre,apellido,comidaFavorita):
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.comidaFavorita = comidaFavorita
        self.__contraseñaDelFeis = "1317"
    def __str__(self):
        return f"soy {self.nombre} {self.apellido} y me gusta mucho la {self.comidaFavorita}"
    def __repr__(self):
        return f"humano(nombre={self.nombre}, apellido={self.apellido}, comidaFavorita{self.comidaFavorita})"
objeto1 = humano("Sebastian","Bermeo","Hamburguesa")

print(objeto1)
print(str(objeto1))
print(repr(objeto1))

#FORMAT
dia=14
mes="Marzo"
print("Hoy es el dia {0} de {1}".format(dia,mes))

#HASH
class cliente:
    def __init__(self,valor):
        self.valor = valor
    def __hash__(self):
        return hash(self.valor)
    def __eq__(self,otro):
        return self is otro
    
karen = cliente(1000)
sebastian = cliente(1000)

print(karen == sebastian)
print(karen is sebastian)
print(hash(karen) == hash (sebastian))

#BYTES
class widget:
    def _init_(self, nombre):
        self.nombre = nombre

    def _bytes_(self):
        return bytes(self.nombre, "utf-8")

print(bytes(widget("Dave"))) # b'Dave'
print(bytes("Dave", "utf-8")) # b'Dave'

#BOOL
class Personita:
    def _init_(self, nombre, edad):
        self.nombre = NameError
        self.edad = edad

    def _bool_(self):
        if self.edad < 21 or self.edad > 75:
            return False
        return True

#if _nombre_ == '_main_':
    #person = Personita('camilo', 92)
    #print(bool(Personita))

#NEW
class autos(object):
    def _new_(cls):
        print("Mi carro es color morado oscuro")
        #return sample()
 
autos()