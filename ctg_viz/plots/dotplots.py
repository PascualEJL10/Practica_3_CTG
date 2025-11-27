# %%
"""
Dot plots para el dataset CTG.

Incluye:
- Gráfico de puntos simple
- Comparación por categorías (por ejemplo NSP o CLASS)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

__all__ = ["plot_dotplot_ctg"]


def plot_dotplot_ctg(
    df: pd.DataFrame,
    col: str,
    hue: str | None = None,
    figsize: tuple[int, int] = (10, 6),
    alpha: float = 0.7
) -> None:
    """
    Genera un dot plot (stripplot) para una variable numérica.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        col (str): Columna numérica a graficar.
        hue (str, opcional): Categoría para diferenciar puntos.
        figsize (tuple): Tamaño de la figura.
        alpha (float): Transparencia de los puntos.

    Returns:
        None
    """

    plt.figure(figsize=figsize)

    sns.stripplot(
        data=df,
        x=hue if hue else None,
        y=col,
        hue=hue if hue else None,
        dodge=True,
        alpha=alpha
    )

    titulo = f"Dot plot de {col}"
    if hue:
        titulo += f" por {hue}"

    plt.title(titulo)
    plt.xlabel(hue if hue else "")
    plt.ylabel(col)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()