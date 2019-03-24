def listar_pelicula(doc):
    for info in doc:
        print("Titulo:",info["title"])
        print("Año:",info["year"])
        print("Duracion:",info["duration"])
def numactores(doc):
    listaP=[]
    for info in doc:
        print(info["title"])
        print("Hay",len(info["actors"]),"Actores.")

def sinopsis(doc,p1,p2):


########################
import json
import codecs
doc=json.load(codecs.open('movies.json', 'r', 'utf-8-sig'))
opciones='''1.Listar titulo año y duracion
2.Mostrar titulos y numero de actores
3.Mostrar peliculas en sinopsis dada.
4.Mostrar peliculas con actor.
5.Mostrar titulo y url poster de 3 peliculas media alta y entre fecha dada
0.Salir'''
opcion=int
while True:
    print(opciones)
    try:
        opcion=int(input("Dime la opción. "))
    except:
        print("Eso no es una opcion")
    else:
        if opcion==1:
            listar_pelicula(doc)
        elif opcion==2:
            numactores(doc)
        elif opcion==3:
            print("Hola")
        elif opcion==4:
            juego=str(input("Dime el nombre del juego. "))
            if juego_compañia(doc,juego)==None:
                print("Ese juego no tiene compañia.")
            else:
                print("Su compañia es",juego_compañia(doc,juego))
        elif opcion==5:
            juego=str(input("Dime el nombre del juego. "))
            try:
                lista=caracteristicas_juego(doc,juego)
            except:
                print("Ese juego no tiene caracteristicas.")
            else:
                print("Hola")
        elif opcion==0:
            print("Fin del programa.")
            break