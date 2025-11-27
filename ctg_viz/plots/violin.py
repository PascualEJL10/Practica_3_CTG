# %%
"""
Gráfica de violín para el dataset CTG.

Opciones:
- Violín simple o dividido por grupos
- Overlay opcional con puntos (swarm o strip)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

__all__ = ["plot_violin_ctg"]


def plot_violin_ctg(
    df: pd.DataFrame,
    col: str,
    hue: str = None,
    figsize: tuple = (10, 6),
    add_points: bool = True,
    points_type: str = "swarm",
    alpha: float = 0.7,
):
    """
    Crea un violin plot para una columna numérica del CTG.

    Args:
        df (pd.DataFrame): Datos.
        col (str): Columna numérica a graficar.
        hue (str): Columna categórica para separar grupos.
        figsize (tuple): Tamaño de la figura.
        add_points (bool): Si True, agrega puntos sobre el violín.
        points_type (str): 'swarm' o 'strip' para los puntos.
        alpha (float): Transparencia de los puntos.

    Returns:
        None
    """

    plt.figure(figsize=figsize)

    # Violín principal
    sns.violinplot(
        data=df,
        x=hue if hue else None,
        y=col,
        hue=hue if hue else None,
        inner="box",
        linewidth=1.2
    )

    # Puntos opcionales
    if add_points:
        if points_type == "swarm":
            sns.swarmplot(
                data=df,
                x=hue if hue else None,
                y=col,
                color="black",
                alpha=alpha,
                size=3
            )
        else:
            sns.stripplot(
                data=df,
                x=hue if hue else None,
                y=col,
                color="black",
                alpha=alpha
            )

    titulo = f"Violin plot de {col}"
    if hue:
        titulo += f" por {hue}"

    plt.title(titulo)
    plt.xlabel(hue if hue else "")
    plt.ylabel(col)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()