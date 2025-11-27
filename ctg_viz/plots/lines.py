# %%
"""
Gráficos de líneas para variables numéricas del dataset CTG.

Incluye:
- Línea simple usando el índice como referencia temporal
- Línea segmentada por categoría (por ejemplo CLASS o NSP)
"""

import matplotlib.pyplot as plt
import pandas as pd

__all__ = ["plot_line_ctg"]


def plot_line_ctg(
    df: pd.DataFrame,
    col: str,
    hue: str = None,
    figsize: tuple = (12, 6),
    alpha: float = 0.8
) -> None:
    """
    Genera un gráfico de líneas para una columna numérica.

    Si no se especifica 'hue', se dibuja una sola línea.
    Si se pasa una columna categórica en 'hue', se genera una línea por categoría.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        col (str): Columna numérica a graficar.
        hue (str, opcional): Columna categórica para separar líneas.
        figsize (tuple): Tamaño de la figura.
        alpha (float): Transparencia de las líneas.

    Returns:
        None
    """

    plt.figure(figsize=figsize)

    # Caso 1: línea simple
    if hue is None:
        plt.plot(df.index, df[col], alpha=alpha)
        plt.title(f"Evolución de {col} a lo largo del índice")
        plt.xlabel("Índice (simulación de tiempo)")
        plt.ylabel(col)
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()
        return

    # Caso 2: varias líneas según la categoría indicada
    categorias = df[hue].unique()

    for categoria in categorias:
        subset = df[df[hue] == categoria]

        plt.plot(
            subset.index,
            subset[col],
            alpha=alpha,
            label=f"{hue} = {categoria}"
        )

    plt.title(f"Evolución de {col} segmentada por {hue}")
    plt.xlabel("Índice (simulación de tiempo)")
    plt.ylabel(col)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()