# La Isla delas Tentaciones api

![portada](http://www.eltelevisero.com/wp-content/uploads/2020/01/IMG_20200117_140346_445-750x375.jpg)

Este proyecto se ha desarrollado durante el bootcamp de data analysis de Ironhack.

## Objetivos del proyecto

El objetivo del proyecto es desarrollar una api capaz de servir información sobre una base de datos determinada (en este caso sobre frases expresadas durante la emisión del reality show "La Isla de las Tentaciones". Asi como de permitir introducirlas y analizar el grado de postividad o negatividad de cada frase.


## Estructuras del repositorio

El repositorio está organizado de la siguiente manera:
En al carpeta principal encontramos los archivos en los que se desarrolla el codigo propio de la api.
En la carpeta "data" se recogen los archivos .csv y .json de la base de datos con los datos previos a inserciones ejecutadas desde la api.
La base de datos se ha realizado con Mongodb y se compone de 3 colecciones: Participantes, Grupos y Frases.

En participantes recogemos los datos personales de cada uno de los usuarios.
En Grupos sólo están incluidos los datos de a qué grupos de comunicación pertenece cada participante (algunos participantes pueden pertenecer a varios grupos)
En Frases incluiremos todas las frases que se han considerados interesantes para analizar durante cualquiera de las 3 ediciones del reality.

Por último encontramos un notebook en el que se realizan algunos ejemplos de request a la api.

## Endpoints

URL : http://127.0.0.1:5000/

Si no sabes qué es La Isla de las Tentaciones, en el siguiente endpoint encontrarás más información:

/inicio

#### Get endpoints
/mensajes nos muestra todos los mensajes recogidos en nuestra database
/participantes nos muestra todos los participantes
/participantes/details/<participante_id> nos muestra los detalle del participante concreto que se introduzca

#### Post endpoints

/participantes/new nos permite introducir un nuevo participante


## Technology Stack

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Pandas](https://pandas.pydata.org/docs/)
- [Mongodb](https://www.mongodb.com/)