"""El borde del sistema: el comando `arandu evaluar <caso.json>` (contrato v1)."""
import argparse
import json
from datetime import datetime
from pathlib import Path

from arandu.ventana import en_ventana


def leer_caso(ruta: str) -> dict:
    """Lee el archivo y devuelve solo la parte "entrada" (contrato v1)."""
    datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    return datos["entrada"]


def evaluar(entrada: dict) -> dict:
    """Aplica las reglas en el orden de R8 y devuelve el resultado."""
    # Forma: el texto se convierte en datos una sola vez, acá en el borde.
    instante = datetime.fromisoformat(entrada["solicitud"]["instante"])
    apertura = datetime.fromisoformat(entrada["periodo"]["apertura"])
    cierre = datetime.fromisoformat(entrada["periodo"]["cierre"])

    # Negocio: las reglas reciben datos ya convertidos, en el orden de R8.
    if not en_ventana(instante, apertura, cierre):
        return {"resultado": "rechazada", "motivo": "R1"}
    # Las demás reglas van acá, en este orden: R2, R7, R4, R5, R3.
    return {"resultado": "aceptada"}


def main() -> None:
    parser = argparse.ArgumentParser(prog="arandu")
    sub = parser.add_subparsers(dest="comando", required=True)
    p_evaluar = sub.add_parser("evaluar", help="evalúa un caso con el formato del contrato v1")
    p_evaluar.add_argument("caso", help="ruta del archivo JSON del caso")
    args = parser.parse_args()

    if args.comando == "evaluar":
        resultado = evaluar(leer_caso(args.caso))
        print(json.dumps(resultado, ensure_ascii=False))
