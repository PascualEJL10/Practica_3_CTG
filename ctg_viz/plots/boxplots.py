# %%
"""
Boxplots del dataset CTG:

- Boxplots simples
- Boxplots por grupos (CLASS, NSP)
- Subgráficos automáticos cuando se usa hue
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

__all__ = ["plot_boxplot_ctg"]


def plot_boxplot_ctg(df: pd.DataFrame, col: str, hue: str = None,
                     figsize: tuple = (10, 6)):
    """
    Genera un boxplot para una columna numérica.

    Si se proporciona `hue`, se generan subgráficos separados
    para cada categoría.

    Args:
        df (pd.DataFrame): DataFrame del CTG.
        col (str): columna numérica a graficar.
        hue (str, opcional): columna categórica para separar boxplots.
        figsize (tuple): tamaño de la figura.

    Returns:
        None
    """

    # Caso 1: boxplot simple
    if hue is None:
        plt.figure(figsize=figsize)
        sns.boxplot(data=df, y=col)
        plt.title(f"Boxplot de {col}")
        plt.grid(axis="y", alpha=0.3)
        plt.tight_layout()
        plt.show()
        return

    # Caso 2: subplots por categoría
    categorias = df[hue].unique()
    n = len(categorias)

    filas = 1 if n <= 3 else 2
    columnas = n if n <= 3 else (n + 1) // 2

    plt.figure(figsize=(columnas * 5, filas * 5))

    for i, categoria in enumerate(categorias, start=1):
        plt.subplot(filas, columnas, i)
        subset = df[df[hue] == categoria]

        sns.boxplot(data=subset, y=col)
        plt.title(f"{col} para {hue} = {categoria}")
        plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.show()