# %%
"""
Clasificación de columnas según los requisitos de la práctica:

- Continuas: columnas numéricas con más de 10 valores únicos
- Discretas: columnas numéricas con 10 o menos valores únicos
"""

import pandas as pd

__all__ = ["classify_columns_ctg"]

def classify_columns_ctg(df: pd.DataFrame) -> dict:
    """
    Clasifica columnas numéricas en continuas o discretas.

    Reglas:
    - Continuas: dtype numérico y >10 valores únicos
    - Discretas: dtype numérico y <=10 valores únicos

    Args:
        df (pd.DataFrame)

    Returns:
        dict con dos listas:
            - "continuas"
            - "discretas"
    """

    continuas = []
    discretas = []

    for col in df.columns:
        serie = df[col]

        # Solo analizamos columnas numéricas
        if pd.api.types.is_numeric_dtype(serie):

            if serie.nunique() > 10:
                continuas.append(col)
            else:
                discretas.append(col)

    return {
        "continuas": continuas,
        "discretas": discretas
    }