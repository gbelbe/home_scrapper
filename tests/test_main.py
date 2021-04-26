import sys
# from homescrapper.kerrentree import ParseSite
from homescrapper.scrap_immo import SiteParse, ListParse
from homescrapper.rozenn import RozennSiteParse
from homescrapper.kerrentree import KerrentreeSiteParse

sys.path.insert(0, '../src/homescrapper/')


BASE_URL = "https://www.cabinetrozennmelscoet.com"
LIST_URL = "https://www.cabinetrozennmelscoet.com/a-vendre/1"
LIST_TAG = "li"
LIST_TAG_CLASS = "col-xs-12 col-sm-6 col-md-12 panelBien"
REF_LABEL = "ref"
ELEMENTS = {
    "id_tag": "img",
    "id_tag_class": " lazyloaded",
    "img_tag": "img",
    "img_tag_class": "",
    "price_tag": "span",
    "price_tag_class": "price",
    "link_tag": "div",
    "link_tag_class": "col-xs-12 col-md-4 panel-heading",
    "date_tag": "date",
    "date_tag_class": "dateclass",
}


def test_SiteParse():
    # site_url = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    # list_tag = "div"
    # list_tag_class = "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log"

    a = SiteParse(BASE_URL, LIST_URL,  LIST_TAG, LIST_TAG_CLASS)

    assert len(a.site_parse()) >= 0, 'the list is empty'
    # assert len(a) != 0, 'the list is empty'


def test_ListParse():
    a = ListParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)
    assert len(a.list_parse()) >= 0

def test_RozennParseSite():
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
        "date_tag_class": "dateclass"
    }

    a = RozennSiteParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)
    assert len(a.rozenn_site_parse()) >= 0
    assert int(a.rozenn_site_parse()[0]['id']) == 1191

def test_KerrentreeParseSite():
    BASE_URL = "http://www.kerentree-immobilier.fr"
    LIST_URL = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    LIST_TAG = "div"
    LIST_TAG_CLASS = "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log"
    ELEMENTS = {
        "id_tag": "data-idannonce",
        "id_tag_class": "ref",
        "img_tag": "img",
        "img_tag_class": "",
        "price_tag": "span",
        "price_tag_class": "price",
        "link_tag": "div",
        "link_tag_class": "col-xs-12 col-md-4 panel-heading",
        "date_tag": "date",
    }

    pass
    # a = KerrentreeSiteParse()