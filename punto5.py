#Property
class usuario:
    def __init__(self,nombre_usuario,contraseña,email):
        self.nombre_usuario = nombre_usuario
        self.__contraseña = self.__generar_contraseña(contraseña)
        self.email = email
    def __generar_contraseña(self,contraseña):
        return contraseña.upper()
    @property
    def contraseña(self):
        return self.__contraseña
    @property.setter
    def contraseña(self,valor):
        self.__contraseña = self.__generar_contraseña(valor)
sebastian = usuario("sebastian","sebotas1317","sebastian@gmail.com")
print( sebastian.contraseña )
sebastian.contraseña = "Nueva contraseña"
print(sebastian.contraseña)
