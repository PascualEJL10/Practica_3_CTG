# %%
"""
Pruebas unitarias para el módulo ctg_viz.preprocessing

Funciones cubiertas:
- drop_null_columns
- simple_imputer
- remove_outliers_iqr
"""

import pandas as pd
import numpy as np

from ctg_viz.preprocessing import (
    drop_null_columns,
    simple_imputer,
    remove_outliers_iqr,
)


def test_drop_null_columns():
    """
    Verifica que drop_null_columns elimine las columnas
    cuyo porcentaje de nulos es mayor al threshold.
    """
    # Preparamos un DataFrame pequeño:
    # - Columna A: 2 de 3 valores son nulos → 66% de nulos
    # - Columna B: sin nulos
    df = pd.DataFrame({
        "A": [1, None, None],
        "B": [1, 2, 3],
    })

    # Aplicamos la función con threshold = 0.2 (20%)
    cleaned = drop_null_columns(df, threshold=0.2)

    # A debería eliminarse (66% > 20%), B debería quedarse
    assert "A" not in cleaned.columns
    assert "B" in cleaned.columns


def test_simple_imputer():
    """
    Verifica que simple_imputer rellene los valores faltantes
    tanto en columnas numéricas como categóricas.
    """
    # Creamos un DataFrame con:
    # - 'num': una columna numérica con un NaN
    # - 'cat': una columna categórica con un NaN
    df = pd.DataFrame({
        "num": [1, 2, np.nan],
        "cat": ["x", np.nan, "y"],  # usamos np.nan como en el CTG real
    })

    # Aplicamos el imputador general
    imputed = simple_imputer(df)

    # Esperamos que ya no haya NA en ninguna de las dos columnas
    assert imputed["num"].isna().sum() == 0
    assert imputed["cat"].isna().sum() == 0


def test_remove_outliers_iqr():
    """
    Verifica que remove_outliers_iqr elimine valores extremos (outliers)
    usando el método del rango intercuartílico (IQR).
    """
    # Data con un valor claramente extremo (200)
    df = pd.DataFrame({
        "x": [10, 11, 12, 13, 14, 200],
    })

    # Aplicamos la función sobre la columna 'x'
    cleaned = remove_outliers_iqr(df, cols=["x"], factor=1.5)

    # 1) El valor 200 no debería estar en la serie resultante
    assert 200 not in cleaned["x"].values

    # 2) El número de filas debería haber disminuido
    assert len(cleaned) < len(df)