import sys
sys.path.insert(0, '../src/')

from homescrapper.main import site_parse

def test_site_parse():
    site_url = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    annonce_tags = {
        "main_tag": "div",
        "id_regular_exp": "^annonce*",
        "inner_tag": "div",
        "inner_class": "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log",
    }

    a = site_parse(site_url, annonce_tags)
    assert len(a) != 0, 'the list is empty'

