import streamlit as st  # pyright: ignore[reportMissingImports]
import pandas as pd

from ctg_viz.preprocessing import (
    drop_null_columns,
    simple_imputer,
    remove_outliers_iqr,
)

import plotly.express as px


@st.cache_data
def load_data():
    df = pd.read_csv("CTG.csv")

    df_step1 = drop_null_columns(df, threshold=0.2)
    df_step2 = simple_imputer(df_step1, numeric_strategy="median",
                              categorical_strategy="most_frequent")

    cols_outliers = [
        "LB", "ASTV", "ALTV", "MSTV", "MLTV",
        "Width", "Min", "Max", "Mean", "Median", "Variance",
    ]
    df_step3 = remove_outliers_iqr(df_step2, cols=cols_outliers, factor=1.5)
    return df_step3


def main():
    st.title("CTG - Explorador interactivo")
    st.write(
        "Aplicación sencilla en Streamlit para explorar el dataset CTG "
        "usando la librería `ctg_viz` y gráficos interactivos con Plotly."
    )

    df = load_data()

    # Selector de variable numérica
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    col_select = st.selectbox("Selecciona una variable numérica:", numeric_cols, index=numeric_cols.index("Mean") if "Mean" in numeric_cols else 0)

    st.subheader(f"Histograma interactivo de {col_select}")
    fig = px.histogram(
        df,
        x=col_select,
        nbins=30,
        marginal="box",  # añade boxplot arriba
        title=f"Distribución de {col_select}",
    )
    st.plotly_chart(fig, use_container_width=True)

    # Opcional: segmentar por NSP
    if "NSP" in df.columns:
        st.subheader(f"Densidad por NSP para {col_select}")
        fig_kde = px.histogram(
            df,
            x=col_select,
            color="NSP",
            nbins=30,
            histnorm="probability density",
            barmode="overlay",
            opacity=0.5,
            title=f"Densidad de {col_select} por NSP",
        )
        st.plotly_chart(fig_kde, use_container_width=True)


if __name__ == "__main__":
    main()