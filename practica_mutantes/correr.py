"""Taller I · S6 · Corre casos contra las cuatro versiones de chocan().

Uso, desde la raíz del repositorio:
    uv run python practica_mutantes/correr.py                 (usa practica_mutantes/mis_casos.py)
    uv run python practica_mutantes/correr.py casos_agente    (usa practica_mutantes/casos_agente.py)
"""
import importlib
import sys
from datetime import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import versiones as v

# La versión correcta se revela recién al correr: es la que cumple R5.
CORRECTA = v.version_b
CON_ERROR = {"A": v.version_a, "C": v.version_c, "D": v.version_d}


def franja(t):
    dia, inicio, fin = t
    return v.Franja(dia, time.fromisoformat(inicio), time.fromisoformat(fin))


def main() -> int:
    nombre = Path(sys.argv[1]).stem if len(sys.argv) > 1 else "mis_casos"
    casos = importlib.import_module(nombre).CASOS
    if not casos:
        print(f"{nombre}.py no tiene casos todavía.")
        return 1
    detectadas = set()
    for titulo, a, b, esperado in casos:
        fa, fb = franja(a), franja(b)
        if CORRECTA(fa, fb) != esperado:
            print(f"✗ {titulo}: el esperado no coincide con la regla R5. Revisar el caso.")
            continue
        quien = [k for k, f in CON_ERROR.items() if f(fa, fb) != esperado]
        detectadas.update(quien)
        print(f"✓ {titulo}: detecta {', '.join(quien) if quien else 'ninguna versión con error'}")
    vivas = [k for k in CON_ERROR if k not in detectadas]
    print(f"\nVersiones con error detectadas: {len(detectadas)} de 3.")
    if vivas:
        print("Sin detectar: " + ", ".join(vivas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
