"""Taller I · S6 · Cuatro versiones de chocan() para R5.

Una es correcta y tres tienen un error puesto a propósito. Este archivo no se modifica.
"""
from dataclasses import dataclass
from datetime import time


@dataclass(frozen=True)
class Franja:
    dia: int        # 1 = lunes ... 7 = domingo
    inicio: time
    fin: time


def version_a(a: Franja, b: Franja) -> bool:
    return a.dia == b.dia and a.inicio < b.fin


def version_b(a: Franja, b: Franja) -> bool:
    return a.dia == b.dia and a.inicio < b.fin and b.inicio < a.fin


def version_c(a: Franja, b: Franja) -> bool:
    return a.dia == b.dia and a.inicio <= b.inicio < a.fin


def version_d(a: Franja, b: Franja) -> bool:
    return a.dia == b.dia and a.inicio <= b.fin and b.inicio <= a.fin
