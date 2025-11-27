# %%
"""
Gráficas de densidad (KDE) para el dataset CTG.

Se pueden hacer:
- Gráficas de densidad simples
- Gráficas de densidad separadas por grupos (por ejemplo CLASS o NSP)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

__all__ = ["plot_density_ctg"]


def plot_density_ctg(
    df: pd.DataFrame,
    col: str,
    hue: str | None = None,
    figsize: tuple[int, int] = (10, 6),
    alpha: float = 0.6,
    fill: bool = True,
) -> None:
    """
    Dibuja una gráfica de densidad (KDE) para una columna numérica.

    Si se pasa una columna en `hue`, se dibuja una curva por cada categoría.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        col (str): Columna numérica a graficar.
        hue (str | None): Columna categórica para separar las curvas.
        figsize (tuple[int, int]): Tamaño de la figura.
        alpha (float): Transparencia de las curvas.
        fill (bool): Si es True, se rellena el área bajo la curva.

    Returns:
        None
    """
    plt.figure(figsize=figsize)

    # Caso 1: una sola densidad
    if hue is None:
        sns.kdeplot(
            data=df,
            x=col,
            fill=fill,
            alpha=alpha,
            linewidth=2,
        )
        plt.title(f"Densidad de {col}")
        plt.xlabel(col)
        plt.ylabel("Densidad")
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
        return

    # Caso 2: densidad por categoría
    categorias = df[hue].unique()

    for categoria in categorias:
        subset = df[df[hue] == categoria]

        sns.kdeplot(
            data=subset,
            x=col,
            fill=fill,
            alpha=alpha,
            linewidth=2,
            label=f"{hue} = {categoria}",
        )

    plt.title(f"Densidad de {col} por {hue}")
    plt.xlabel(col)
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()