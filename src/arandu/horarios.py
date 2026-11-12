# una Franja (día, inicio y fin) y la función chocan(a, b),
#que devuelve True si las dos franjas comparten día y sus intervalos se solapan;
from dataclasses import dataclass
from datetime import time


@dataclass
class Franja:
    dia: int
    inicio: time
    fin: time


#as: 19-21
#b:20-22:30
def chocan(a: Franja, b: Franja) -> bool:
    if a.dia != b.dia:
        return False
    return a.inicio < b.fin and b.inicio < a.fin