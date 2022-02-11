import pandas as pd
import requests
import json
import os

# url
url = "https://www.starz.com/ar/es/movies"
series_json_url = "https://playdata.starz.com/metadata-service/play/partner/Web_AR/v8/content?lang=es-419&contentType=Series_with_Season"

s = requests.Session()

series_responce = s.get(series_json_url)

state = series_responce.raise_for_status()

if(state == None):
    data = series_responce.json()
else:
    "Error: " + str(state)

content = data['playContentArray']['playContents']


def obtener_series():
    os.makedirs('export', exist_ok=True)
    series_list = []
    for serie in content:
        series_list.append(serie['title'])
    save_json(series_list, 'Series_List')
    save_csv(series_list, 'Series_List')


def obtener_series_con_detalle():
    os.makedirs('export', exist_ok=True)
    series_full_list = []
    for serie in content:
        series_info = {"Title": serie['title'],
                       "Year": serie['minReleaseYear'],
                       "Sinopsis": serie['logLine'],
                       "Cant. Temporadas": len(serie['childContent']),
                       "Studio": serie['studio'],
                       "Rating Name": serie['ratingName']
                       }

        series_full_list.append(series_info)
    save_json(series_full_list, 'Series_List_Detail')
    save_csv(series_full_list, 'Series_List_Detail')


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


obtener_series()
obtener_series_con_detalle()
