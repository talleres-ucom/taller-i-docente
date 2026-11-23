"""R1 · Ventana de inscripción."""
from datetime import datetime


def en_ventana(instante: datetime, apertura: datetime, cierre: datetime) -> bool:
    """La solicitud se acepta solo si el instante cae en [apertura, cierre], extremos incluidos."""
    return apertura <= instante <= cierre
