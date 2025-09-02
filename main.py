print("Web scrapping")

import requests
import os

url = "https://timesofindia.indiatimes.com/india/delhi"

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    # Make sure directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Write with UTF-8 encoding
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

fetchAndSaveToFile(url, "data/times.html")
