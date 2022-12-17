import unittest   # The test framework
from Reporte_LigaArgentina import *
class Test_Reporte_LigaArgentina(unittest.TestCase):
    def setUp(self):
        self.lista = list()
        self.__url = "https://www.espn.com.ar/futbol/posiciones/_/liga/arg.1/primera-division-de-argentina"
        self.page = requests.get(self.__url)
        self.soup = BeautifulSoup(self.page.content, "lxml")

    def test_Registro(self):
        equiNombre = self.soup.find("abbr", tittle="")
        objeto = Reporte_LigaArgentina()
        lista = objeto.RegistrarEquipos()
        lis = list()
        for l in lista:
            lis.append(str(l))
        ejem1 = lis[0]
        self.assertIn(equiNombre.text, ejem1)
       

    def test_Escritura(self):
        equiNombre = self.soup.find("abbr", tittle="")
        objeto = Reporte_LigaArgentina()
        objeto.EscribirLosPrimeros10()
        leer = open("C:\\Users\\Dieguillo\\WorkspacePython\\Webscraping_Python\\TablaDeCalificaciones.txt", "r")
        lista = list()
        for l in leer:
            lista.append(l)
        self.assertIn(equiNombre.text, lista[0])    

if __name__ == "__main__":
    unittest.main()
