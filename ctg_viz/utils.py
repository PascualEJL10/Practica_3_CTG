# %%
"""
Funciones de apoyo para revisar el dataset CTG.

Incluye:
- Conteo y porcentaje de nulos
- Conteo y porcentaje de ceros en columnas numéricas
- Tipos de datos y número de valores únicos
- Detección de columnas constantes
"""

import pandas as pd

__all__ = ["check_data_completeness_Pascual_Enrique_Juarez_Luna"]


def check_data_completeness_Pascual_Enrique_Juarez_Luna(df: pd.DataFrame):
    """
    Muestra un resumen completo del estado del dataset:

    - Shape (número de filas y columnas)
    - Tipo de dato por columna
    - Número de valores únicos
    - Conteo de nulos por columna
    - Porcentaje de nulos
    - Columnas ordenadas por % de nulos
    - Conteo y porcentaje de ceros en columnas numéricas
    - Columnas constantes (sin variación)

    Args:
        df (pd.DataFrame): DataFrame del CTG

    Returns:
        None (solo imprime)
    """

    print("\n========== RESUMEN GENERAL ==========")
    print(f"Shape del DataFrame: {df.shape}")

    print("\n========== TIPOS DE DATOS ==========")
    print(df.dtypes)

    print("\n========== VALORES ÚNICOS POR COLUMNA ==========")
    print(df.nunique())

    print("\n========== NULOS POR COLUMNA ==========")
    null_counts = df.isna().sum()
    print(null_counts)

    print("\n========== PORCENTAJE DE NULOS ==========")
    null_pct = (null_counts / len(df)).round(4)
    print(null_pct)

    print("\n========== COLUMNAS ORDENADAS POR % DE NULOS ==========")
    print(null_pct.sort_values(ascending=False))

    print("\n========== CEROS POR COLUMNA NUMÉRICA ==========")
    numeric_cols = df.select_dtypes(include=["number"])
    zero_counts = (numeric_cols == 0).sum()
    print(zero_counts)

    print("\n========== PORCENTAJE DE CEROS ==========")
    zero_pct = (zero_counts / len(df)).round(4)
    print(zero_pct)

    print("\n========== COLUMNAS CONSTANTES (sin variación) ==========")
    const_cols = df.columns[df.nunique() == 1]
    if len(const_cols) == 0:
        print("Ninguna columna es constante.")
    else:
        print(const_cols.tolist())

    print("\n========== ANÁLISIS COMPLETADO ==========\n")