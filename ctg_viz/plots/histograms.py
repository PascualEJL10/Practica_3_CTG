# %%
"""
Histogramas para el CTG.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

__all__ = ["plot_histogram_ctg"]


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