
#Clase equipos donde se establece las entidades importantes a destacar

class Equipo():
    def __init__(self, pos, nombre, pt):
        self.__pos = pos
        self.__nombre = nombre
        self.__pt = pt

    def toGetPT(self):
        return self.__pt    

    def toGetNombre(self):
        return self.__nombre

    def toGetPos(self):
        return self.__pos        

    def __str__(self):
        return f'Posicion:  {self.__pos}   Nombre:  {self.__nombre}  Puntos:   {self.__pt}  \n '
