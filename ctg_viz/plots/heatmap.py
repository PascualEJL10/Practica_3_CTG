# %%
"""
Gráficas de heatmap de correlación para el dataset CTG.

Incluye:
- Heatmap completo
- Opción de usar Pearson o Spearman
- Anotaciones opcionales
- Máscara para mostrar solo el triángulo inferior
- Filtro opcional de columnas numéricas
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

__all__ = ["plot_heatmap_ctg"]


def plot_heatmap_ctg(
    df: pd.DataFrame,
    cols: list = None,
    method: str = "pearson",
    annot: bool = True,
    mask_upper: bool = True,
    figsize: tuple = (12, 8),
    cmap: str = "coolwarm"
):
    """
    Genera un heatmap de correlación para columnas numéricas.

    Args:
        df (pd.DataFrame): DataFrame del CTG.
        cols (list): Columnas a incluir en el análisis.
        method (str): Método de correlación ('pearson' o 'spearman').
        annot (bool): Si True, muestra los valores dentro del mapa.
        mask_upper (bool): Si True, oculta el triángulo superior.
        figsize (tuple): Tamaño de la figura.
        cmap (str): Paleta de colores.

    Returns:
        None
    """

    # Si no se especifican columnas → usar solo las numéricas
    df_corr = df[cols] if cols is not None else df.select_dtypes(include="number")

    # Matriz de correlación
    corr_matrix = df_corr.corr(method=method)

    # Máscara para triángulo superior
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool)) if mask_upper else None

    # Gráfica
    plt.figure(figsize=figsize)
    sns.heatmap(
        corr_matrix,
        annot=annot,
        cmap=cmap,
        mask=mask,
        fmt=".2f",
        linewidths=0.5,
        square=True
    )

    plt.title(f"Heatmap de correlación ({method})", fontsize=14)
    plt.tight_layout()
    plt.show()