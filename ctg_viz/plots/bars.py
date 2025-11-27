# %%
"""
Gráficos de barras horizontales para variables categóricas del dataset CTG.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

__all__ = ["plot_barh_ctg"]


def plot_barh_ctg(df: pd.DataFrame, col: str, hue: str = None,
                  figsize: tuple = (10, 6), palette: str = "viridis"):
    """
    Genera un gráfico de barras horizontales ordenado por frecuencia.

    Args:
        df (pd.DataFrame): DataFrame de entrada.
        col (str): Columna categórica a graficar.
        hue (str): Columna para segmentar (opcional).
        figsize (tuple): Tamaño de la figura.
        palette (str): Colores de la gráfica.

    Returns:
        None
    """

    plt.figure(figsize=figsize)

    if hue is None:
        conteo = df[col].value_counts().sort_values(ascending=True)

        conteo.plot(kind="barh", color=sns.color_palette(palette, len(conteo)))
        plt.title(f"Frecuencias de {col}")
        plt.xlabel("Frecuencia")
        plt.ylabel(col)
        plt.grid(axis="x", alpha=0.3)
        plt.tight_layout()
        plt.show()
        return

    conteo = df.groupby([col, hue]).size().reset_index(name="counts")

    sns.barplot(
        data=conteo,
        y=col,
        x="counts",
        hue=hue,
        palette=palette
    )

    plt.title(f"Frecuencias de {col} segmentado por {hue}")
    plt.xlabel("Frecuencia")
    plt.ylabel(col)
    plt.grid(axis="x", alpha=0.3)
    plt.tight_layout()
    plt.show()