import requests

# Definuj URL API
url = "http://127.0.0.1:8000/blog/api/posts/"

# Připrav data pro příspěvek
data = {
    "title": "Nový příspěvek",
    "content": "Toto je obsah nového příspěvku."
}

# Odeslání POST požadavku
response = requests.post(url, json=data)

# Zkontroluj, zda byl požadavek úspěšný
if response.status_code == 201:
    print("Příspěvek byl úspěšně vytvořen:")
    print(response.json())  # Zobrazí vrácená data
else:
    print("Nastala chyba při vytváření příspěvku:")
    print(response.status_code, response.text)
