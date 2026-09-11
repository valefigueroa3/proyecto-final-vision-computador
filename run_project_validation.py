"""Ejecuta las celdas de código del cuadernillo en modo no interactivo.

Este archivo solo se usa para validar el proyecto durante su construcción.
"""

from __future__ import annotations

import json
import os
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
warnings.filterwarnings("ignore")

WORKSPACE = Path(__file__).resolve().parent
NOTEBOOK = WORKSPACE / "01_Exploracion_dataset.ipynb"
PROJECT = Path(
    r"C:\Users\Valentina Figueroa\OneDrive - Universidad del Norte\PERSONAL\MAESTRÍA ANALÍTICA DE DATOS\Visión por computador\Proyecto final"
)
OUTPUT = WORKSPACE / "validation_metrics.json"
DETAILS_OUTPUT = WORKSPACE / "validation_details.json"

os.chdir(PROJECT)
with NOTEBOOK.open(encoding="utf-8") as file:
    notebook = json.load(file)

namespace = {"display": lambda value: None}
for index, cell in enumerate(notebook["cells"]):
    if cell.get("cell_type") == "code":
        print(f"Ejecutando celda {index}...", flush=True)
        exec("".join(cell["source"]), namespace)

metrics = {
    "accuracy_lbp_svm": float(namespace["accuracy_lbp_svm"]),
    "f1_lbp_svm": float(namespace["f1_lbp_svm"]),
    "mejores_parametros_svm": namespace["mejores_parametros"],
    "accuracy_cnn": float(namespace["accuracy_cnn"]),
    "f1_cnn": float(namespace["f1_cnn"]),
    "mejor_accuracy_validacion_cnn": float(namespace["mejor_accuracy_val"]),
    "epocas_cnn": int(len(namespace["df_historial_cnn"])),
}

with OUTPUT.open("w", encoding="utf-8") as file:
    json.dump(metrics, file, ensure_ascii=False, indent=2)

details = {
    "historial_cnn": namespace["df_historial_cnn"].to_dict(orient="list"),
    "clases": namespace["CLASES"],
    "y_prueba": namespace["y_prueba"].tolist(),
    "prediccion_lbp": namespace["prediccion_prueba"].tolist(),
    "y_prueba_cnn": namespace["y_prueba_cnn"].tolist(),
    "prediccion_cnn": namespace["prediccion_cnn"].tolist(),
}
with DETAILS_OUTPUT.open("w", encoding="utf-8") as file:
    json.dump(details, file, ensure_ascii=False, indent=2)

print("Validación terminada.")
print(json.dumps(metrics, ensure_ascii=False, indent=2))
