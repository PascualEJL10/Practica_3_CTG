# %%
"""
Paquete ctg_viz

Módulos de preprocesamiento, diagnóstico y visualización
para el dataset de cardiotocografía (CTG).
"""

from .preprocessing import (
    drop_null_columns,
    simple_imputer,
    remove_outliers_iqr,
)

from .categorization import (
    classify_columns_ctg,
)

from .utils import (
    check_data_completeness_Pascual_Enrique_Juarez_Luna,
)

from .plots import (
    plot_before_after,
    plot_histogram_ctg,
    plot_barh_ctg,
    plot_line_ctg,
    plot_dotplot_ctg,
    plot_density_ctg,
    plot_violin_ctg,
    plot_heatmap_ctg,
    plot_boxplot_ctg,
)

__all__ = [
    # Preprocesamiento
    "drop_null_columns",
    "simple_imputer",
    "remove_outliers_iqr",

    # Clasificación
    "classify_columns_ctg",

    # Utilidades
    "check_data_completeness_Pascual_Enrique_Juarez_Luna",

    # Gráficas
    "plot_before_after",
    "plot_histogram_ctg",
    "plot_barh_ctg",
    "plot_line_ctg",
    "plot_dotplot_ctg",
    "plot_density_ctg",
    "plot_violin_ctg",
    "plot_heatmap_ctg",
    "plot_boxplot_ctg",
]


