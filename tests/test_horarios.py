from datetime import time
from arandu.horarios import Franja, chocan


# lunes 19:00–21:00 y lunes 20:00–22:00 → chocan;
def test_chocan():
    # Preparacion
    a = Franja(dia=0, inicio=time(19, 0), fin=time(21, 0))
    b = Franja(dia=0, inicio=time(20, 0), fin=time(22, 0))


    # Accion
    verificar_resultado = chocan(a, b)

    # Comprobacion
    assert verificar_resultado is True


# lunes 19:00–21:00 y martes 19:00–21:00 → no chocan
def test_no_chocan():
    # Preparacion
    a = Franja(dia=0, inicio=time(19, 0), fin=time(21, 0))
    b = Franja(dia=1, inicio=time(19, 0), fin=time(21, 0))


    # Accion
    verificar_resultado = chocan(a, b)

    # Comprobacion
    assert verificar_resultado is False


# lunes 19:00–21:00 y lunes 21:00–22:30 → no chocan (contiguas: el borde);
def test_horarios_contiguos_no_chocan():
    # Preparacion
    a = Franja(dia=0, inicio=time(19, 0), fin=time(21, 0))
    b = Franja(dia=0, inicio=time(21, 0), fin=time(22, 30))


    # Accion
    verificar_resultado = chocan(a, b)

    # Comprobacion
    assert verificar_resultado is False
