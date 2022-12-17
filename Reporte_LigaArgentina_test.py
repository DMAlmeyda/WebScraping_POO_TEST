import unittest   # The test framework
from Reporte_LigaArgentina import *
class Test_Reporte_LigaArgentina(unittest.TestCase):
    def test_Registro(self):
        objeto = Reporte_LigaArgentina()
        lista = objeto.RegistrarEquipos()
        lis = list()
        for l in lista:
            lis.append(str(l))
        ejem1 = lis[0]
        ejem2 = lis[1]
        self.assertEqual('Posicion:  1   Nombre:  CABJ  Puntos:   52  \n ',ejem1)
        self.assertEqual('Posicion:  2   Nombre:  RAC  Puntos:   50  \n ',ejem2)

    def test_Escritura(self):
        objeto = Reporte_LigaArgentina()
        objeto.EscribirLosPrimeros10()
        leer = open("C:\\Users\\Dieguillo\\WorkspacePython\\Webscrapping_Python\\TablaDeCalificaciones.txt", "r")
        lista = list()
        for l in leer:
            lista.append(l)
        self.assertEqual("Posicion:  1   Nombre:  CABJ  Puntos:   52  \n", lista[0])    

if __name__ == "__main__":
    unittest.main()
