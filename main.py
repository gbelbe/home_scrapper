# convert scraped date text to proper date format
from datetime import datetime

# requests import curl type library and beautiful soup html parser library
import requests
from bs4 import BeautifulSoup

# import regular expressions
import re


# retrieve the url from the web address
website = requests.get('http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2')
# check if status is ok http200
print(website)

soup = BeautifulSoup(website.content, 'html.parser')

# Grab all div tags with ID starting with "annonceXXX", that is showing the recap infos from the houses
div_tag = soup.find_all(name="div", id=re.compile('^annonce*'))

annonces_list = []

for tag in div_tag:

    annonce_dict = {}

    id_annonce = tag.find(name="div", class_="btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log")["data-idannonce"]
    annonce_dict["id"]=id_annonce

    img = tag.find("img")
    # print(img['src'])

    # annonce_dict["img"] = img['src']
    # print(annonce_dict["img"])

    # annonce_dict["long_desc"] = img['longdesc']

    MAJ = tag.find("p", class_="margin-top-10 height-50").find_all(text=True, recursive=False)
    # print(MAJ)
    # retrieve the date, 2nd element of the text list received from MAJ
    majdate = datetime.strptime(MAJ[1].strip().split()[2], '%d/%m/%Y')
    #print(majdate)
    annonce_dict["maj_date"] = majdate

    lien = tag.find(name="a")
    url = lien.get("href")
    titre = lien.get("title")

    # annonce_dict["url"] = url
    # annonce_dict["titre"] = titre

    annonces_list.append(annonce_dict)

# We order the list by its most recent element: we must order a list with nested dictionary by one elem of the dict
sorted_annonces = sorted(annonces_list, key=lambda k: k['maj_date'], reverse=True)

print(annonces_list)
print(sorted_annonces)

