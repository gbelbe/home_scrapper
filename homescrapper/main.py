# convert scraped date text to proper date format
from datetime import datetime

# requests import curl type library and beautiful soup html parser library
import requests
from bs4 import BeautifulSoup

# import regular expressions
import re

URL = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
#URL = "https://www.cabinetrozennmelscoet.com/a-vendre/1"

TAG = "li"
DIV_CLASS = "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log"
REGEX = "^annonce*"
class ParseSite():
    """parse l\'url d\'un site d'immobilier"""

    def __init__(self, url, div, regex=""):
        self.url = url
        self.main_tag = "div"
        self.inner_tag = "div"
        self.inner_div_class = div
        self.regex = regex


    def site_parse(self):
        '''
        Function to parse a site URL
        @param url: properly formated url of a page displaying a list of homes
        @param tags: dictionary formated like annonce_tags, showing the different things to parse from the list of homes.
        @return: list of dictionary containing informations from each property on the scrapped site
        '''

        # retrieve the url from the web address
        website = requests.get(self.url)
        # check if status is ok http200
        # print(website)
        soup = BeautifulSoup(website.content, 'html.parser')


        # Grab all div tags with ID starting with "annonceXXX", that is showing the recap infos from the houses
        div_tag = soup.find_all(name=self.main_tag, id=re.compile(self.regex))

        annonces_list = []

        for tag in div_tag:
            annonce_dict = {}

            id_annonce = tag.find(name=self.inner_tag, class_=self.inner_div_class)["data-idannonce"]
            annonce_dict["id"] = id_annonce

            img = tag.find("img")
            # print(img['src'])

            # annonce_dict["img"] = img['src']
            # print(annonce_dict["img"])

            # annonce_dict["long_desc"] = img['longdesc']

            MAJ = tag.find("p", class_="margin-top-10 height-50").find_all(text=True, recursive=False)
            # print(MAJ)
            # retrieve the date, 2nd element of the text list received from MAJ
            majdate = datetime.strptime(MAJ[1].strip().split()[2], '%d/%m/%Y')
            # print(majdate)
            annonce_dict["maj_date"] = majdate

            lien = tag.find(name="a")
            url = lien.get("href")
            titre = lien.get("title")

            annonce_dict["url"] = url
            # annonce_dict["titre"] = titre

            annonces_list.append(annonce_dict)

        # We order the list by its most recent element: we must order a list with nested dictionary by one elem of the dict
        sorted_annonces = sorted(annonces_list, key=lambda k: k['maj_date'], reverse=True)

        return sorted_annonces
        # print(annonces_list)
        # print(sorted_annonces)


annonces = ParseSite(URL, DIV_CLASS, REGEX)

print(annonces.site_parse())


# print(site_parse(site_url, annonce_tags))