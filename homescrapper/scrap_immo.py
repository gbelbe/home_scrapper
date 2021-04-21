# convert scraped date text to proper date format
from datetime import datetime

# requests import curl type library and beautiful soup html parser library
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.cabinetrozennmelscoet.com"
LIST_URL = "https://www.cabinetrozennmelscoet.com/a-vendre/1"
LIST_TAG = "li"
LIST_TAG_CLASS = "col-xs-12 col-sm-6 col-md-12 panelBien"
REF_LABEL = "ref"
ELEMENTS = {
    "id_tag": "span",
    "id_tag_class": "ref",
    "img_tag": "img",
    "img_tag_class": "",
    "price_tag": "span",
    "price_tag_class": "price",
    "link_tag": "div",
    "link_tag_class": "col-xs-12 col-md-4 panel-heading",
    "date_tag": "date",
}


class SiteParse():
    """parse l\'url d\'un site d'immobilier"""

    def __init__(self, base_url, list_url, list_tag, list_tag_class=''):
        self.base_url = base_url
        self.list_url = list_url
        self.list_tag = list_tag
        self.list_tag_class = list_tag_class
        self.html_list_elems = ""

    def site_parse(self):
        '''
        Function to parse a site URL
        @param url: properly formated url of a page displaying a list of homes
        @param tags: dictionary formated like annonce_tags, showing the different things to parse from the list of homes.
        @return: list of dictionary containing informations from each property on the scrapped site
        '''

        # retrieve the url from the web address
        website = requests.get(self.list_url)
        # check if status is ok http200
        # print(website)
        soup = BeautifulSoup(website.content, 'html.parser')
        # print(soup)

        # Grab all div tags with ID starting with "annonceXXX", that is showing the recap infos from the houses

        div_tag = soup.find_all(name=self.list_tag, class_=self.list_tag_class)
        self.html_list_elems = div_tag

        return self.html_list_elems


class RozennSiteParse(SiteParse):
    def __init__(self, base_url, list_url, list_tag, list_tag_class, elements):
        # initialize list_url, tag and class from Parse_Site
        super().__init__(base_url, list_url, list_tag, list_tag_class)

        self.id_tag = elements["id_tag"]
        self.id_tag_class = elements["id_tag_class"]
        self.img_tag = elements["img_tag"]
        self.img_tag_class = elements["img_tag_class"]
        self.price_tag = elements["price_tag"]
        self.price_tag_class = elements["price_tag_class"]
        self.link_tag = elements["link_tag"]
        self.link_tag_class = elements["link_tag_class"]
        # self.date_tag = elements["date_tag"]

        # Store list of annonces from each div element
        self.annonces_list = []

    def site_parse(self):
        # retrieve site_parse method from ParseSite Parent Class

        html_list_elems = super().site_parse()

        for elem in html_list_elems:
            annonce_dict = {}
            id_annonce = elem.find(name=self.id_tag, class_=self.id_tag_class)
            html_stripped_text = id_annonce.get_text()
            word_list = html_stripped_text.split()
            id_annonce = word_list[1]
            annonce_dict["id"] = id_annonce

            price = elem.find(name=self.price_tag, itemprop=self.price_tag_class)
            price = price["content"]
            annonce_dict["price"] = price

            img = elem.find(name=self.img_tag, class_=self.img_tag_class)
            src = img['src']
            img = "http:" + src
            annonce_dict["img"] = img

            link = elem.find(name=self.link_tag, class_=self.link_tag_class)["onclick"]
            stripped_link = link.replace("location.href=\'", self.base_url)
            last_quote = stripped_link[-1]
            link_without_final_quote = stripped_link.strip(last_quote)
            # print(link_without_final_quote)
            annonce_dict["url"] = link_without_final_quote

            # TODO: continue with other elements of the list from rozenn.py


            self.annonces_list.append(annonce_dict)
        return self.annonces_list
            # annonce_dict["id"] = id_annonce
            #
            # annonce_dict["id"] = tag.find(self.id_tag)
            # annonce_dict["img"] = tag.find(self.img_tag)
            #
            # annonce_dict["price"] = tag.find(self.price_tag)
            #
            # annonce_dict["link"] = tag.find(self.link_tag)
            #
            # annonce_dict["date"] = tag.find(self.date_tag)
            #
            #

# instantiate an object annonces from class Rozenn
annonces = RozennSiteParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)

# print what is returned from site_parse method of annonces object
print(annonces.site_parse())

# print(help(Rozenn))
# print(annonces.site_parse())
