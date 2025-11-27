# %%
"""
Histogramas para el CTG.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

__all__ = ["plot_histogram_ctg", "plot_histogram_plotly_ctg"]


def plot_histogram_ctg(
    df: pd.DataFrame,
    column: str,
    by: str | None = None,
    bins: int = 30,
    kde: bool = True,
    density: bool = False,
    alpha: float = 0.6,
    figsize: tuple[int, int] = (8, 4),
) -> None:
    """
    Dibuja un histograma simple o segmentado por una columna categórica.

    Args:
        df: DataFrame con los datos.
        column: Nombre de la columna numérica a graficar.
        by: Columna para segmentar el histograma (ej. "NSP" o "CLASS").
        bins: Número de bins.
        kde: Si True, agrega la curva de densidad.
        density: Si True, normaliza el histograma (en lugar de conteos).
        alpha: Transparencia de las barras.
        figsize: Tamaño de la figura.
    """
    plt.figure(figsize=figsize)

    stat_value = "density" if density else "count"

    # Histograma simple
    if by is None:
        sns.histplot(
            data=df,
            x=column,
            bins=bins,
            kde=kde,
            alpha=alpha,
            stat=stat_value,
            element="step",
        )
        title = f"Histograma de {column}"

    # Histograma segmentado
    else:
        sns.histplot(
            data=df,
            x=column,
            hue=by,
            bins=bins,
            kde=kde,
            alpha=alpha,
            stat=stat_value,
            multiple="layer",
            element="step",
        )
        title = f"Histograma de {column} por {by}"

    plt.title(title)
    plt.xlabel(column)
    plt.ylabel("Densidad" if density else "Frecuencia")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_histogram_plotly_ctg(
    df: pd.DataFrame,
    column: str,
    color: str | None = None,
    nbins: int = 30,
):
    """
    Histograma interactivo con Plotly para el dataset CTG.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame con los datos.
    column : str
        Nombre de la columna numérica a graficar.
    color : str, opcional
        Columna categórica para colorear la distribución (ej. 'NSP' o 'CLASS').
    nbins : int, opcional
        Número de bins del histograma.

    Devuelve
    --------
    fig : plotly.graph_objects.Figure
        Figura de Plotly lista para usar (fig.show() o embebida en Streamlit).
    """
    fig = px.histogram(
        df,
        x=column,
        color=color,
        nbins=nbins,
        histnorm=None,
        marginal="box",
        title=f"Histograma interactivo de {column}",
    )
    return fig