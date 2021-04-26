# convert scraped date text to proper date format
from datetime import datetime

# requests import curl type library and beautiful soup html parser library
import requests
from bs4 import BeautifulSoup

class SiteParse:
    """parse l\'url d\'un site d'immobilier et renvoie un objet BeautifulSoup"""

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

class ListParse(SiteParse):
    """retrieve the HTMl from a site parsed with BeautifulSoup and retrieve the List
    a list of dictionaries with elements of home"""


    def __init__(self, base_url, list_url, list_tag, list_tag_class, elements):
        # initialize list_url, tag and class from Parse_Site
        super().__init__(base_url, list_url, list_tag, list_tag_class)

        self.id_tag = elements["id_tag"]
        self.id_tag_class = elements["id_tag_class"]
        self.img_tag = elements["img_tag"]
        self.img_tag_class = elements["img_tag_class"]
        self.price_tag = elements["price_tag"]

        if "price_tag_property" in elements:
            self.price_tag_property = elements["price_tag_property"]
        else:
            self.price_tag_property = ""

        self.price_tag_class = elements["price_tag_class"]
        self.link_tag = elements["link_tag"]
        self.link_tag_class = elements["link_tag_class"]
        self.date_tag = elements["date_tag"]
        self.date_tag_class = elements["date_tag_class"]
        # Store list of annonces from each div element
        self.annonces_list = []

    def list_parse(self):
        """retrieve html elements of each element of the list"""

        html_list_elems = super().site_parse()

        for elem in html_list_elems:
            annonce_dict = {}

            id_annonce = elem.find(name=self.id_tag, class_=self.id_tag_class)
            annonce_dict["id"] = id_annonce


            # manage the case that the price div tag has a property "itemprop" instead of the traditional "class" property
            # we default as "class" as it is the standard

            if self.price_tag_property == 'itemprop':
                price = elem.find(name=self.price_tag, itemprop=self.price_tag_class)
            else:
                price = elem.find(name=self.price_tag, class_=self.price_tag_class)

            price = price.get_text().replace(" ", "")
            annonce_dict["price"] = price


            img = elem.find(name=self.img_tag, class_=self.img_tag_class)
            annonce_dict["img"] = img

            link = elem.find(name=self.link_tag, class_=self.link_tag_class)
            annonce_dict["url"] = link

            date = elem.find(name=self.date_tag, class_=self.date_tag_class)
            annonce_dict["date"] = date

            self.annonces_list.append(annonce_dict)

        return self.annonces_list


