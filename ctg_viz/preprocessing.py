# %%
"""
Módulo de preprocesamiento para el dataset CTG.

Incluye funciones para:
- Eliminar columnas con alto porcentaje de valores nulos
- Imputar valores faltantes
- Eliminar outliers mediante el método IQR
"""

from typing import List
import pandas as pd
from sklearn.impute import SimpleImputer  # pyright: ignore[reportMissingImports]


__all__ = [
    "drop_null_columns",
    "simple_imputer",
    "remove_outliers_iqr",
]


def drop_null_columns(df: pd.DataFrame, threshold: float = 0.2) -> pd.DataFrame:
    """
    Elimina columnas que superan el porcentaje dado de valores nulos.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        threshold (float): Límite máximo permitido (0.2 = 20%).

    Returns:
        pd.DataFrame: DataFrame sin columnas que exceden el umbral.
    """
    null_ratio = df.isna().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index
    return df.drop(columns=cols_to_drop)


def simple_imputer(
    df: pd.DataFrame,
    numeric_strategy: str = "median",
    categorical_strategy: str = "most_frequent",
) -> pd.DataFrame:
    """
    Imputa valores faltantes en columnas numéricas y categóricas.

    Args:
        df (pd.DataFrame): DataFrame con valores faltantes.
        numeric_strategy (str): Método para imputar valores numéricos.
        categorical_strategy (str): Método para imputar valores categóricos.

    Returns:
        pd.DataFrame: DataFrame con los valores faltantes imputados.
    """
    df_imputed = df.copy()

    num_cols = df_imputed.select_dtypes(include=["number"]).columns
    cat_cols = df_imputed.select_dtypes(exclude=["number"]).columns

    if len(num_cols) > 0:
        imp_num = SimpleImputer(strategy=numeric_strategy)
        df_imputed[num_cols] = imp_num.fit_transform(df_imputed[num_cols])

    if len(cat_cols) > 0:
        imp_cat = SimpleImputer(strategy=categorical_strategy)
        df_imputed[cat_cols] = imp_cat.fit_transform(df_imputed[cat_cols])

    return df_imputed


def remove_outliers_iqr(
    df: pd.DataFrame,
    cols: List[str],
    factor: float = 1.5,
) -> pd.DataFrame:
    """
    Elimina outliers mediante el método (IQR).

    Args:
        df (pd.DataFrame): DataFrame original.
        cols (List[str]): Columnas a evaluar.
        factor (float): Multiplicador estándar del IQR.

    Returns:
        pd.DataFrame: DataFrame filtrado sin valores extremos.
    """
    df_clean = df.copy()

    for col in cols:
        if not pd.api.types.is_numeric_dtype(df_clean[col]):
            continue

        q1 = df_clean[col].quantile(0.25)
        q3 = df_clean[col].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - factor * iqr
        upper = q3 + factor * iqr

        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]

    return df_clean