# %%
"""
Pruebas unitarias para el módulo ctg_viz.utils

Función cubierta:
- check_data_completeness_Pascual_Enrique_Juarez_Luna
"""

import pandas as pd
from ctg_viz.utils import check_data_completeness_Pascual_Enrique_Juarez_Luna


def test_check_data_completeness(capsys):
    """
    Verifica que la función imprima un reporte sin errores.
    Se usa capsys para capturar la salida estándar.
    """

    df = pd.DataFrame({
        "num": [1, 2, None, 4],
        "cat": ["x", "y", None, "z"]
    })

    # La función imprime y retorna None
    result = check_data_completeness_Pascual_Enrique_Juarez_Luna(df)

    # Debe regresar None
    assert result is None

    # Capturamos el texto impreso
    captured = capsys.readouterr()

    # Debe contener partes clave del reporte
    assert "RESUMEN GENERAL" in captured.out
    assert "TIPOS DE DATOS" in captured.out
    assert "NULOS POR COLUMNA" in captured.out
    assert "CEROS POR COLUMNA" in captured.out
    assert "ANÁLISIS COMPLETADO" in captured.out