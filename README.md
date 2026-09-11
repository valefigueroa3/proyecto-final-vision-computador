# Clasificación de condiciones foliares

Proyecto final de la asignatura Visión por Computador de la Maestría en Analítica de Datos.

## Objetivo

Comparar un enfoque clásico basado en características de textura Local Binary Patterns (LBP) y una SVM lineal frente a un enfoque de transferencia de aprendizaje con MobileNetV2 para clasificar imágenes de hojas en tres clases:

- `Healthy`: hoja sana.
- `Powdery`: hoja con mildiu polvoriento.
- `Rust`: hoja con roya.

El resultado corresponde únicamente a las tres clases visuales del dataset. No constituye un diagnóstico agrícola general.

## Dataset

Se utilizó el [Plant Disease Recognition Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset), disponible en Kaggle. La versión descargada contiene imágenes en las carpetas `Train`, `Validation` y `Test`, organizadas por las tres clases.

Las imágenes no se incluyen en este repositorio. Después de descargar y extraer el archivo de Kaggle, ubica el contenido así:

```text
Proyecto final/
├── 01_Exploracion_dataset.ipynb
├── dataset_plant_disease/
│   ├── Train/Train/Healthy/
│   ├── Train/Train/Powdery/
│   ├── Train/Train/Rust/
│   ├── Validation/Validation/...
│   └── Test/Test/...
├── requirements.txt
└── README.md
```

## Metodología

```text
Imagen de hoja
    ↓
Exploración y preprocesamiento
    ↓
LAB y CLAHE en el canal de luminosidad
    ↓
Enfoque 1: LBP espacial + SVM lineal
Enfoque 2: MobileNetV2 preentrenada + capa final
    ↓
Accuracy, F1 macro y matrices de confusión
```

## Ejecución

1. Crear y activar un entorno virtual de Python.
2. Instalar dependencias con `pip install -r requirements.txt`.
3. Abrir `01_Exploracion_dataset.ipynb` en Jupyter o VS Code.
4. Seleccionar el kernel que contiene las dependencias.
5. Ejecutar las celdas en orden.

La primera ejecución de MobileNetV2 descarga sus pesos preentrenados y los guarda en `torch_cache/`. La extracción de LBP y de embeddings puede tardar algunos minutos en CPU.

## Métricas

Los dos modelos se evalúan con la misma partición de prueba. Se reportan Accuracy, F1 macro, reporte de clasificación y matriz de confusión.

## Tecnologías

Python, OpenCV, scikit-image, scikit-learn, PyTorch y Torchvision.

## Referencias

- Rashik Rahman. *Plant Disease Recognition Dataset*. Kaggle.
- Ojala, T., Pietikäinen, M., & Mäenpää, T. (2002). Multiresolution gray-scale and rotation invariant texture classification with local binary patterns. IEEE TPAMI, 24(7), 971-987.
- Sandler, M., Howard, A., Zhu, M., Zhmoginov, A., & Chen, L.-C. (2018). MobileNetV2: Inverted residuals and linear bottlenecks. CVPR.
