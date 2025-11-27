"""
Gráfica comparativa Before/After para columnas numéricas.

Muestra dos boxplots lado a lado:
- Antes del tratamiento (df_before)
- Después del tratamiento (df_after)
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


__all__ = ["plot_before_after"]


def plot_before_after(
    df_before: pd.DataFrame,
    df_after: pd.DataFrame,
    col: str,
    figsize: tuple = (10, 6),
):
    """
    Genera boxplots comparando la distribución de una columna antes y después
    del preprocesamiento (por ejemplo antes/después de eliminar outliers).

    Args:
        df_before (pd.DataFrame): DataFrame original (antes).
        df_after (pd.DataFrame): DataFrame procesado (después).
        col (str): Nombre de la columna numérica a comparar.
        figsize (tuple): Tamaño de la figura.

    Returns:
        None (muestra la gráfica).
    """

    # Validación básica
    if col not in df_before.columns:
        raise ValueError(f"La columna '{col}' no está en df_before.")
    if col not in df_after.columns:
        raise ValueError(f"La columna '{col}' no está en df_after.")

    # Construimos un DataFrame combinado
    df_plot = pd.DataFrame({
        "valor": pd.concat([df_before[col], df_after[col]], ignore_index=True),
        "estado": (["Antes"] * len(df_before)) + (["Después"] * len(df_after)),
    })

    plt.figure(figsize=figsize)
    sns.boxplot(
        data=df_plot,
        x="estado",
        y="valor"
    )

    plt.title(f"Comparación Before/After para '{col}'")
    plt.xlabel("")
    plt.ylabel(col)
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()