from homescrapper.scrap_immo import SiteParse, ListParse
from datetime import datetime
import re

BASE_URL = "https://kernot.notaires.fr"
LIST_URL = "https://kernot.notaires.fr/annonces-immobilieres-SELARL-KERNOT-PAYS-BIGOUDEN-Alain-MALLEGOL-Celine-FRITZSCHE-Vincent-VARNOUX.html"
LIST_TAG = "div"
LIST_TAG_CLASS = "bloc-annonce img-txt"
ELEMENTS = {
    "img_tag": "img",
    "img_tag_class": "lazyload",
    "price_tag": "div",
    "price_tag_class": "immo-prix pull-right display-resp",
    "link_tag": "a",
    "link_tag_class": "",
    "date_tag": "",
    "date_tag_class": "",
}


class KernotSiteParse(ListParse):
    def __init__(self, base_url, list_url, list_tag, list_tag_class, elements):
        # initialize list_url, tag and class from Parse_Site
        super().__init__(base_url, list_url, list_tag, list_tag_class, elements)

    def kernot_site_parse(self):
        # retrieve site_parse method from ParseSite Parent Class
        annonces_list = []

        html_list_elems = super().list_parse()

        for elem in html_list_elems:

            annonce_dict = {}

            # annonce_dict['price'] = elem['price']

            # print(annonce_dict)
            # string_price = elem['price'].get_text()



            price = elem['price']
            special_char = '€'
            annonce_dict['price'] = price.split(special_char, 1)[0]

            annonce_dict['img'] = elem['img']['data-src']
            annonce_dict['url'] = elem['url']['href']
            # date = elem['date'].get_text()
            # date = date.strip().split()
            # print(date)
            # annonce_dict['date'].strip().split()[2]
            # date = datetime.strptime(date, '%d/%m/%Y')

            # TODO: finir l'intégration de la date avec datetime

            # MAJ = tag.find("p", class_="margin-top-10 height-50").find_all(text=True, recursive=False)

            #     majdate = datetime.strptime(MAJ[1].strip().split()[2], '%d/%m/%Y')

            #     annonce_dict["maj_date"] = majdate



            annonces_list.append(annonce_dict)

        return annonces_list


annonces = KernotSiteParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)

print(annonces.kernot_site_parse())
