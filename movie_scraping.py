import requests
import pandas as pd
import json
import os

url = "https://www.starz.com/ar/es/movies"
movies_json_url = "https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentType=Movie"

s = requests.Session()

movies_responce = s.get(movies_json_url)

state = movies_responce.raise_for_status()

if state == None:
    data = movies_responce.json()
else:
    "Error: " + str(state)

play_contents = data["playContentArray"]['playContents']


def obtener_peliculas():
    os.makedirs('export', exist_ok=True)
    movies_list = []
    for k in play_contents:
        movies_list.append(k['title'])
    save_csv(movies_list, 'Movies List')
    save_json(movies_list, 'Movies List')


def crear_link(title, content_id):
    os.makedirs('export', exist_ok=True)
    link_path = 'https://www.starz.com/ar/es/movies/'
    link_name = title.replace(' ', '-')
    full_link = link_path + link_name + "-" + str(content_id)
    return full_link


def calcular_duracion(dur_seg):
    duracion = "{0:.0f}".format(dur_seg/60)
    return duracion


def obtener_peliculas_con_detalle():
    full_movies_info = []
    for movie in play_contents:
        movie_info = {"title": movie['title'],
                      "year": movie['releaseYear'],
                      "sinopsis": movie['logLine'],
                      "link": crear_link(movie['title'], movie['contentId']),
                      "duration": calcular_duracion(movie['runtime'])}

        full_movies_info.append(movie_info)
    save_csv(full_movies_info, 'Movies_List_Detail')
    save_json(full_movies_info, 'Movies_List_Detail')
    save_html(full_movies_info,'Movies_List_Detail')


def save_csv(list, name):    
    df = pd.DataFrame(list)
    df.to_csv(f'export/{name}.csv')
    print(f'Archivo CSV creado con el nombre: {name}.csv')


def save_json(list, output_name):
    with open(f'export/{output_name}.json', "w") as outfile:
        json.dump(list, outfile)
        print(f'Archivo JSON creado con el nombre: {output_name}.json')

def save_html(list, output_name):
    df = pd.DataFrame(list)
    df.to_html(f'export/{output_name}.html')      


obtener_peliculas()
obtener_peliculas_con_detalle()
