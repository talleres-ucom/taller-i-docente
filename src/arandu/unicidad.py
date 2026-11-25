"""R7 · Unicidad."""


def ya_cursa(materia: str, materias_activas: list[str]) -> bool:
    """True si la materia pedida ya está entre las materias de las inscripciones activas."""
    return materia in materias_activas
