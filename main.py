print("Web scrapping")

import requests

url = "https://timesofindia.indiatimes.com/india/delhi"


def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)



fetchAndSaveToFile(url, "data/times.html")