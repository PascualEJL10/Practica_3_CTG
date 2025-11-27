from setuptools import setup, find_packages

setup(
    name="ctg_viz",
    version="0.1.0",
    description="Librería de preprocesamiento y visualización para el dataset CTG",
    author="Pascual Enrique Juárez Luna",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "plotly",
    ],
)