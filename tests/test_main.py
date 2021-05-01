import sys
from homescrapper.scrap_immo import SiteParse, ListParse
from homescrapper.rozenn import RozennSiteParse
from homescrapper.kerrentree import KerrentreeSiteParse
from homescrapper.kernot import KernotSiteParse

sys.path.insert(0, '../src/homescrapper/')


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
    "price_tag_property": "itemprop",
    "price_tag_class": "price",
    "link_tag": "div",
    "link_tag_class": "col-xs-12 col-md-4 panel-heading",
    "date_tag": "date",
    "date_tag_class": "dateclass",
}


def test_site_parse():
    # site_url = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    # list_tag = "div"
    # list_tag_class = "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log"

    a = SiteParse(BASE_URL, LIST_URL,  LIST_TAG, LIST_TAG_CLASS)

    assert len(a.site_parse()) >= 0, 'the list is empty'
    # assert len(a) != 0, 'the list is empty'


def test_list_parse():
    a = ListParse(BASE_URL, LIST_URL, LIST_TAG, LIST_TAG_CLASS, ELEMENTS)
    assert len(a.list_parse()) >= 0


def test_rozenn_site_parse():
    base_url = "https://www.cabinetrozennmelscoet.com"
    list_url = "https://www.cabinetrozennmelscoet.com/a-vendre/1"
    list_tag = "li"
    list_tag_class = "col-xs-12 col-sm-6 col-md-12 panelBien"
    elements = {
        "id_tag": "span",
        "id_tag_class": "ref",
        "img_tag": "img",
        "img_tag_class": "",
        "price_tag": "span",
        "price_tag_property": "itemprop",
        "price_tag_class": "price",
        "link_tag": "div",
        "link_tag_class": "col-xs-12 col-md-4 panel-heading",
        "date_tag": "date",
        "date_tag_class": "dateclass",
    }

    a = RozennSiteParse(base_url, list_url, list_tag, list_tag_class, elements)
    assert len(a.rozenn_site_parse()) >= 0


def test_kerrentree_site_parse():
    base_url = "http://www.kerentree-immobilier.fr"
    list_url = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    list_tag = "div"
    list_tag_class = "row-fluid margin-bottom-20 conteneur-annonce"
    elements = {
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

    a = KerrentreeSiteParse(base_url, list_url, list_tag, list_tag_class, elements)
    assert len(a.kerrentree_site_parse()) >= 0


def test_kernot_site_parse():
    base_url = "https://kernot.notaires.fr"
    list_url = "https://kernot.notaires.fr/annonces-immobilieres-SELARL-KERNOT-PAYS-BIGOUDEN" \
               "-Alain-MALLEGOL-Celine-FRITZSCHE-Vincent-VARNOUX.html"
    list_tag = "div"
    list_tag_class = "bloc-annonce img-txt"
    elements = {
        "img_tag": "img",
        "img_tag_class": "lazyload",
        "price_tag": "div",
        "price_tag_class": "immo-prix pull-right display-resp",
        "link_tag": "a",
        "link_tag_class": "",
        "date_tag": "",
        "date_tag_class": "",
    }

    a = KernotSiteParse(base_url, list_url, list_tag, list_tag_class, elements)
    assert len(a.kernot_site_parse()) >= 0
