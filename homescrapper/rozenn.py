from homescrapper.scrap_immo import SiteParse, ListParse

BASE_URL = "https://www.cabinetrozennmelscoet.com"
LIST_URL = "https://www.cabinetrozennmelscoet.com/a-vendre/1"
LIST_TAG = "li"
LIST_TAG_CLASS = "col-xs-12 col-sm-6 col-md-12 panelBien"
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
    "date_tag_class": "dateclass",
}


class RozennSiteParse(ListParse):
    def __init__(self, base_url, list_url, list_tag, list_tag_class, elements):
        # initialize list_url, tag and class from Parse_Site
        super().__init__(base_url, list_url, list_tag, list_tag_class, elements)

    def rozenn_site_parse(self):
        # retrieve site_parse method from ParseSite Parent Class
        annonces_list = []

        html_list_elems = super().list_parse()

        for elem in html_list_elems:

            annonce_dict = {}

            annonce_dict['id'] = elem['id'].get_text().split()[1]
            annonce_dict['price'] = elem['price']["content"]
            annonce_dict['img'] = "http:" + elem['img']['src']
            annonce_dict['url'] = elem['url']["onclick"].replace("location.href=\'", self.base_url).strip("\'")

            annonces_list.append(annonce_dict)

        return annonces_list

# instantiate an object annonces from class Rozenn
annonces = RozennSiteParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)

print(annonces.rozenn_site_parse())
# print what is returned from site_parse method of annonces object
# print(annonces.site_parse())

# print(help(Rozenn))
# print(annonces.site_parse())
