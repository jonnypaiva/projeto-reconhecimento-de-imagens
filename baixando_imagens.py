import requests
from bs4 import BeautifulSoup
import urllib.request
import os

url = "https://br.pinterest.com/emorockstar121/monster-drink-aesthetics/"

resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, "html.parser")

img_tags = soup.find_all("img")

if not os.path.exists("download_imagens"):
    os.makedirs("download_imagens")

for imagem in img_tags:
    img_url = imagem["src"]

    if "monster" or "energy" or \
            "energético" or "drink" or "Monster" or "Energy" in img_url:
        filename = img_url.split("/")[-1]
        filepath = os.path.join("download_imagens", filename)
        urllib.request.urlretrieve(img_url, filepath)
