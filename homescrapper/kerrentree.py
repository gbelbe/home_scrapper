from homescrapper.scrap_immo import ListParse
import re

BASE_URL = "http://www.kerentree-immobilier.fr"
LIST_URL = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
LIST_TAG = "div"
LIST_TAG_CLASS = "row-fluid margin-bottom-20 conteneur-annonce"
ELEMENTS = {
    "id_tag": "div",
    "id_tag_class": "h4-like typo-action refannonce",
    "img_tag": "img",
    "img_tag_class": "recherche-annonces-photo",
    "price_tag": "span",
    "price_tag_property": "itemprop",
    "price_tag_class": "price",
    "link_tag": "a",
    "link_tag_class": "recherche-annonces-lien",
    "date_tag": "p",
    "date_tag_class": "margin-top-10 height-50",
}


#     # annonce_dict["long_desc"] = img['longdesc']
#
#
#     lien = tag.find(name="a")
#     url = lien.get("href")
#     titre = lien.get("title")
#
#     annonce_dict["url"] = url
#     annonce_dict["titre"] = titre
#
#     annonces_list.append(annonce_dict)
#
# # We order the list by its most recent element: we must order a list with nested dictionary by one elem of the dict
# sorted_annonces = sorted(annonces_list, key=lambda k: k['maj_date'], reverse=True)
#
# return sorted_annonces
#

class KerrentreeSiteParse(ListParse):
    def __init__(self, base_url, list_url, list_tag, list_tag_class, elements):
        # initialize list_url, tag and class from Parse_Site
        super().__init__(base_url, list_url, list_tag, list_tag_class, elements)

    def kerrentree_site_parse(self):
        # retrieve site_parse method from ParseSite Parent Class
        annonces_list = []

        html_list_elems = super().list_parse()

        for elem in html_list_elems:
            annonce_dict = {}

            annonce_dict['id'] = elem['id'].get_text().split()[2]
            string_price = elem['price']
            annonce_dict['price'] = re.sub(r"[\n\t\s]*", "", string_price)
            annonce_dict['img'] = elem['img']['src']
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


annonces = KerrentreeSiteParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)

print(annonces.kerrentree_site_parse())
