from Equipos import *
from bs4 import BeautifulSoup
import requests
import os

class Reporte_LigaArgentina():
    def __init__(self):
        self.lista = list()
        self.__url = "https://www.espn.com.ar/futbol/posiciones/_/liga/arg.1/primera-division-de-argentina"
        self.page = requests.get(self.__url)
        self.soup = BeautifulSoup(self.page.content, "lxml")

    def RegistrarEquipos(self):
        equipos = self.soup.find_all("abbr", tittle="")
        posicion = self.soup.find_all("span", class_="team-position ml2 pr3")
        puntos = self.soup.find_all("span", class_="stat-cell")
        team = list()
        pos = list()
        pt = list()
        flag = 0
        flag2 = 0

        for e in posicion:
            if flag == 10:
                flag = 0
                break
            p = e.text
            pos.append(int(p))
            flag += 1
        
        for e in equipos:
            if flag == 10:
                flag = 0
                break
            flag += 1
            team.append(e.text)
        
        for e in puntos:
            flag += 1
            flag2 += 1
            if flag == 8:
                flag = 0
                p = e.text
                pt.append(int(p))
                if flag2 >= 80:
                    break

        for i in range(10):
            equipo = Equipo(pos[i],team[i], pt[i])
            self.lista.append(equipo)

        return self.lista

    def EscribirLosPrimeros10(self):
        try:
            lista = self.RegistrarEquipos()
            nombre = os.path.join('C:\\Users\\Dieguillo\\WorkspacePython\\Webscrapping_Python' , "TablaDeCalificaciones.txt")
            with open(nombre, "w") as esc:
                for l  in lista:
                 esc.write(str(l))
             
            esc.close()    
        except IOError:
            print("Error " + IOError)    




