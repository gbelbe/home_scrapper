import sys
sys.path.insert(0, '../src/homescrapper/')

from homescrapper.main import ParseSite

def test_site_parse():
    site_url = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    # annonce_tags = {
    #     "main_tag": "div",
    #     "id_regular_exp": "^annonce*",
    #     "inner_tag": "div",
    #     "inner_class": "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log",
    # }
    div = "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log"
    regex = "^annonce*"

    a = ParseSite(site_url, div, regex)
    assert len(a.site_parse()) != 0, 'the list is empty'
    # assert len(a) != 0, 'the list is empty'

