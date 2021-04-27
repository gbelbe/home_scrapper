from homescrapper.scrap_immo import SiteParse, ListParse

BASE_URL = "https://www.leboncoin.fr"
LIST_URL = "https://www.leboncoin.fr/recherche?category=9&locations=Pont-l%27Abb%C3%A9_29120__47.86686_-4.22395_4578_5000"
LIST_TAG = "div"
LIST_TAG_CLASS = "sc-bdvvaa xQQfJ"
ELEMENTS = {
    "img_tag": "img",
    "img_tag_class": "_1cnjm",
    "price_tag": "span",
    "price_tag_class": "AdCardPrice__Amount-bz31y2-1 dflscE",
    "link_tag": "a",
    "link_tag_class": "AdCard__AdCardLink-sc-1h74x40-0 cHZrAn",
    "date_tag": "span",
    "date_tag_class": "_2k43C _137P- P4PEa _3j0OU",
}


class LbcSiteParse(ListParse):
    def __init__(self, base_url, list_url, list_tag, list_tag_class, elements):
        # initialize list_url, tag and class from Parse_Site
        super().__init__(base_url, list_url, list_tag, list_tag_class, elements)
        # self.price_tag_class = elements['price_tag_property']

    def lbc_site_parse(self):
        # retrieve site_parse method from ParseSite Parent Class
        annonces_list = []


        html_list_elems = super().list_parse()


        for elem in html_list_elems:

            annonce_dict = {}

            annonce_dict['id'] = elem['id'].get_text().split()[1]

            annonce_dict['price'] = elem['price']

            annonce_dict['img'] = "http:" + elem['img']['src']
            annonce_dict['url'] = elem['url']["onclick"].replace("location.href=\'", self.base_url).strip("\'")

            annonces_list.append(annonce_dict)

        return annonces_list

# instantiate an object annonces from class Rozenn
annonces = LbcSiteParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)

print(annonces.lbc_site_parse())
# print what is returned from site_parse method of annonces object
# print(annonces.site_parse())

# print(help(Rozenn))
# print(annonces.site_parse())
