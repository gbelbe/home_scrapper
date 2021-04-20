import sys
from homescrapper.kerrentree import ParseSite
sys.path.insert(0, '../src/homescrapper/')


def test_site_parse():
    site_url = "http://www.kerentree-immobilier.fr/recherche,basic.htm?idp=568148&idtt=2&idtypebien=2"
    list_tag = "div"
    list_tag_class = "btn btn-important btn-block bouton-ajouter-selection-detail btn-tooltip not-log"
    ref_label = "data-idannonce"
    regex = "^annonce*"

    a = ParseSite(site_url, list_tag, list_tag_class, ref_label, regex)

    assert len(a.site_parse()) != 0, 'the list is empty'
    # assert len(a) != 0, 'the list is empty'
