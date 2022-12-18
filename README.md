# WebScraping_POO_TEST
# TABLA DE CONTENIDOS
- [Tecnologias](#tecnologias)
- [Orden](#orden)
- [Funcionamiento](#funcionamiento)
  * [Class_Equipos](#class_equipos)
  * [Class_Reporte_LigaArgentina](#class_reporte_ligaArgentina)
  * [Class_Reporte_LigaArgentina_test](#class_reporte_ligaArgentina_test)
  
    
   
 


# Descripcion

> Este es un simple WebScraping donde se obtiene informacion de la pagina https://www.espn.com.ar/futbol/posiciones/_/liga/arg.1/primera-division-de-argentina para guardar la informacion en un archivo de texto con preferencias personalizables

<!-- toc -->

## Tecnologias
* Librerias: BeautifulSoup, request, lxml y os

## Orden

Se divide en dos clases, en una tenemos las caracteristicas de los equipos y en la otra el funcionamiento principal


## Funcionamiento

* Se tienen dos metodos donde en uno se extrae la informacion y en el otro se escribe la informacion en un archiivo txt

### Class_Equipos

En esta clase se muestra las caracteristicas especificas que se quieren obtener, en este caso solo se busca obtener la posicion del equipo, los puntos y el nombre 

https://github.com/DMAlmeyda/WebScraping_POO_TEST/blob/3252dfaec6645393ab7babe9aefef63e1c632541/Equipos.py#L2-L20

### Class_Reporte_LigaArgentina

Aqui es donde estan las funciones principales, como dijimos anteriormente solo queremos obtener dos cosas especificas, el nombre del equipo y sus puntos.

![image](https://user-images.githubusercontent.com/108648799/208282414-631caebd-613f-47bb-9704-41a35f6fecbf.png)

En este caso solo estamos interesados en extraer los 10 primeros en la tabla y no los 28 equipos.

https://github.com/DMAlmeyda/WebScraping_POO_TEST/blob/cdd53fb1fc3a9691b3c0a604bbb2307a7cb3a18c/Reporte_LigaArgentina.py#L1-L54

En el caso de los puntos como el html tenian los puntajes alojados a todos con el mismo nombre y bs4 no soporta xpath entonces como va en 8 y solo queremos el puntaje final con unas setencias se puede obtener especificamente lo que se busca.

### Class_Reporte_LigaArgentina_test

En este caso se testea de una manera dinamica para ver incluso con el cambio de informacion que todo sigue funcionando como deberia 

https://github.com/DMAlmeyda/WebScraping_POO_TEST/blob/cdd53fb1fc3a9691b3c0a604bbb2307a7cb3a18c/Reporte_LigaArgentina_test.py#L1-L32








