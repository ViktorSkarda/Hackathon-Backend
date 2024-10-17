import requests
import pandas as pd
import json

POLICE_URL = "https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services/Slu%C5%BEebny_Policie_%C4%8CR/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
FIRE_URL = "https://services6.arcgis.com/ogJAiK65nXL1mXAW/arcgis/rest/services/Stanice_a_pracoviště_hasičského_záchranného_systému/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

def get_police_station_info():
    # Send a get request to the police API
    response = requests.get(POLICE_URL)
    
    # Only check if the request was successful
    if response.status_code == 200:
        # Parse the response data as JSON
        data = response.json()
        
        result_list = []

        try:
            # Iterace přes jednotlivé prvky a vytvoření n-tice
            for feature in data['features']:
                naz_stanice = feature['properties']['nazev_obvodu']  # Získání názvu stanice
                souradnice = feature['geometry']['coordinates']  # Získání souřadnic
                result_list.append((naz_stanice, souradnice))  # Přidání n-tice do seznamu

            data_collected = True

        except Exception as e:
            print(f"An error occurred: {e}")
            data_collected = False



        return [result_list, data_collected]

    else:
        print("Failed to retrieve police station information.")
    

def get_fire_station_info():
    # Odeslat GET požadavek na API požární stanice
    response = requests.get(FIRE_URL)
    
    # Kontrola, zda byl požadavek úspěšný
    if response.status_code == 200:
        # Parsování dat odpovědi jako JSON
        data = response.json()
        station_list = []

        try:
            stations_list = [
                (feature["properties"]["druh_pracoviste"], (feature["properties"]["y"], feature["properties"]["x"]))
                for feature in data["features"]
            ]

            data_collected = True

        except Exception as e:
            print(f"Chyba při zpracování dat: {e}")
            data_collected = False

        return [stations_list, data_collected]
    else:
        print("Nepodařilo se načíst informace o požárních stanicích.")
    


if __name__ == "__main__":
    assert get_police_station_info()[1] == True
    print("Test one passed.")
    assert get_fire_station_info()[1] == True
    print("Test two passed.")
