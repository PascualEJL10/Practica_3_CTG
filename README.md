# Práctica 3 – Análisis Exploratorio y Construcción de Librería `ctg_viz`

## Autor

- **Pascual Enrique Juárez Luna**  
  *Diplomado en Ciencia de Datos – G33 – UNAM*

---

## 📌 Descripción del Proyecto

En esta práctica se desarrolló un **análisis exploratorio de datos (EDA)** usando el dataset **Cardiotocografía (CTG)** y, además, se construyó una **librería personalizada en Python llamada `ctg_viz`**, diseñada para automatizar tareas de:

- Preprocesamiento  
- Clasificación de variables  
- Visualización  
- Diagnóstico de calidad de datos  

El objetivo central fue **estandarizar el flujo analítico**, desde la limpieza inicial hasta la generación de visualizaciones avanzadas, permitiendo un análisis más claro, reproducible y profesional.

---

## 📁 Estructura del Proyecto

### **1. Paquete principal `ctg_viz/`**

ctg_viz/
├── init.py
├── preprocessing.py
├── categorization.py
├── utils.py
└── plots/
├── init.py
├── histograms.py
├── boxplots.py
├── bars.py
├── lines.py
├── dotplots.py
├── density.py
├── violin.py
├── heatmap.py
└── before_after.py

### **2. Carpeta de pruebas**

tests/
├── test_preprocessing.py
├── test_categorization.py
└── test_utils.py

### **3. Notebook principal**

- **`Practica3_CTG.ipynb`** – Contiene todo el desarrollo del análisis exploratorio, el proceso de limpieza, las visualizaciones y el uso de la librería creada.

---

## 🧪 Funcionalidades principales de la librería `ctg_viz`

### **🔹 Preprocesamiento (`preprocessing.py`)**

- `drop_null_columns()` – Elimina columnas con alto porcentaje de nulos.  
- `simple_imputer()` – Imputa valores faltantes para numéricas y categóricas.  
- `remove_outliers_iqr()` – Detecta y elimina outliers usando IQR.

### **🔹 Clasificación de columnas (`categorization.py`)**

- `classify_columns_ctg()` – Clasifica variables en **continuas** y **discretas** según su cardinalidad.

### **🔹 Utilidades (`utils.py`)**

- `check_data_completeness_Pascual_Enrique_Juarez_Luna()`  
  Reporte completo incluyendo:
  - tipos de dato  
  - nulos  
  - ceros  
  - columnas constantes  
  - estadísticos básicos  

### **🔹 Visualizaciones (`plots/`)**

Incluye gráficos personalizados:

- Histogramas  
- Boxplots  
- Barras horizontales  
- Series de línea  
- Dot plots  
- Densidad (KDE)  
- Violin plots  
- Heatmaps  
- Comparación “antes vs después" del IQR  

Todas las funciones fueron diseñadas para:

- Estandarizar colores  
- Ajustar títulos automáticos  
- Facilitar segmentación por clase objetivo  

---

## ⚙️ Instrucciones para ejecutar el proyecto

### **1. Instalar dependencias**

Instala todo con:

```bash
pip install -r requirements.txt

Ejecutar el notebook principal

Abre:

Practica_3.ipynb

y sigue el flujo:
	1.	Importación de librerías
	2.	Carga del dataset CTG.csv
	3.	Preprocesamiento:
	•	eliminación de columnas con nulos
	•	imputación
	•	detección y eliminación de outliers
	4.	Clasificación de columnas
	5.	Análisis Exploratorio
	6.	Visualizaciones (más de 20 gráficas)
	7.	Recomendaciones finales

Principales Visualizaciones y Hallazgos

1. Efecto del IQR (Antes vs Después)

El IQR eliminó valores extremos sin alterar la tendencia central (mediana), mejorando la robustez de la variable Mean.

2. Histogramas

Las variables continuas muestran distribuciones estables; Mean es unimodal con ligera asimetría a la derecha.

3. Boxplots segmentados por NSP y CLASS

Revelan diferencias claras entre grupos, siendo NSP una variable altamente explicativa.

4. Barras horizontales

NSP y CLASS están desbalanceadas, aspecto relevante para modelado.

5. Dot plots y violines

Permiten comparar grupos de forma más intuitiva e identificar rangos dominantes.

6. Heatmaps

Se observa correlación muy alta entre Mean y Median; MLTV destaca por ser casi independiente.

⸻

🏁 Conclusiones del Análisis
	•	Los datos tienen muy pocos valores faltantes, por lo que la imputación tiene bajo impacto.
	•	Varias variables son discretas o binarias (DS, DP, Tendency), útiles como indicadores.
	•	La eliminación de outliers mejora la estabilidad sin afectar la estructura general.
	•	Las correlaciones indican grupos de variables redundantes, candidatos a reducción de dimensionalidad.
	•	Las visualizaciones segmentadas permiten identificar patrones por clase objetivo.

Archivo requirements.txt

Incluye todas las librerías necesarias para reproducir el análisis:

pandas
numpy
matplotlib
seaborn
scipy

Licencia

Este proyecto se desarrolla con fines académicos como parte del Diplomado en Ciencia de Datos- G33 – UNAM.