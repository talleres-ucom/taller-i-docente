from datetime import datetime

from arandu.ventana import en_ventana

APERTURA = datetime(2027, 2, 1, 8, 0)
CIERRE = datetime(2027, 2, 10, 23, 59)


def test_dentro_de_la_ventana_se_acepta():
    assert en_ventana(datetime(2027, 2, 5, 10, 0), APERTURA, CIERRE) is True


def test_antes_de_la_apertura_se_rechaza():
    assert en_ventana(datetime(2027, 2, 1, 7, 59), APERTURA, CIERRE) is False


def test_despues_del_cierre_se_rechaza():
    assert en_ventana(datetime(2027, 2, 11, 0, 0), APERTURA, CIERRE) is False


def test_exactamente_en_la_apertura_se_acepta():
    assert en_ventana(APERTURA, APERTURA, CIERRE) is True


def test_exactamente_en_el_cierre_se_acepta():
    assert en_ventana(CIERRE, APERTURA, CIERRE) is True
