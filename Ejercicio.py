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
    listaPeliculas=[]
    for peliculas in doc:
        sinopsis=peliculas["storyline"]
        if sinopsis.count(p1)>0 and sinopsis.count(p2)>0:
            listaPeliculas.append(peliculas["title"])
    return listaPeliculas

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
            palabra=str(input("Dime la primera palabra. "))
            palabra2=str(input("Dime la segunda palabra. "))
            for titulo in sinopsis(doc,palabra,palabra2):
                print(titulo)
            
        elif opcion==0:
            print("Fin del programa.")
            break