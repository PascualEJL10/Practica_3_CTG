# %%
"""
Pruebas unitarias para el módulo ctg_viz.categorization

Función cubierta:
- classify_columns_ctg
"""

import pandas as pd
from ctg_viz.categorization import classify_columns_ctg


def test_classify_columns_ctg():
    """
    Prueba que la función identifique correctamente:
    - columnas continuas
    - columnas discretas
    - columnas no numéricas (las ignora)
    """

    df = pd.DataFrame({
        "cont": list(range(12)),                 # 12 valores únicos → continua
        "disc": [0, 1, 2] * 4,                   # 3 valores únicos → discreta
        "texto": ["a", "b", "c"] * 4,            # no numérica → ignorar
    })

    resultado = classify_columns_ctg(df)

    assert "cont" in resultado["continuas"]
    assert "disc" in resultado["discretas"]
    assert "texto" not in resultado["continuas"]
    assert "texto" not in resultado["discretas"]