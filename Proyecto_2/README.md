# Análisis Inicial y Selección de Problema

## Descripción
Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre varios conjuntos de datos para seleccionar el problema más adecuado para aplicar técnicas de Machine Learning. A través de este proceso, se identifican patrones, relaciones y problemas que pueden ser modelados para obtener resultados predictivos. La selección del problema y la justificación del modelo utilizado es fundamental para la creación de soluciones de inteligencia artificial efectivas.

## Conjuntos de Datos Analizados

A continuación se describen los cuatro conjuntos de datos analizados:

### 1. **Conjunto de Datos de Seguro de Salud**
Este conjunto de datos tiene como objetivo predecir los costos del seguro de salud en función de diversas características del asegurado.

**Fuente:** [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)

**Columnas principales:**
- Edad, género, IMC, número de hijos cubiertos, si fuma o no, región y cargos médicos.

**Problema seleccionado:** Predicción de los costos médicos de los pacientes.

**Justificación del modelo de regresión lineal:**
- **Simplicidad y comprensión:** Fácil de entender e interpretar.
- **Relación lineal entre variables:** Las características como edad e IMC tienen una relación lineal con los cargos médicos.

---

### 2. **Conjunto de Datos de Animales del Zoológico**
Este conjunto contiene información sobre 101 animales con 16 características para predecir su clasificación en 7 clases diferentes: Mamífero, Ave, Reptil, Pez, Anfibio, Insecto e Invertebrado.

**Fuente:** [UCI Machine Learning Repository: Zoo Dataset](https://archive.ics.uci.edu/ml/datasets/Zoo)

**Columnas principales:**
- Nombre del animal, si tiene cabello, plumas, huevos, leche, puede volar, es acuático, etc.

**Problema seleccionado:** Clasificación multiclase de animales.

**Justificación del modelo de Random Forest:**
- **Precisión:** Random Forest alcanzó una precisión superior en comparación con KNN.
- **Manejo de variables categóricas y binarias:** Random Forest maneja bien estas variables sin necesidad de normalización.
- **Robustez al sobreajuste:** Random Forest es menos susceptible al sobreajuste en comparación con KNN.

---

### 3. **Conjunto de Datos de Aprobación de Préstamos**
Este conjunto de datos contiene información financiera utilizada para predecir la aprobación de préstamos en función de características como el puntaje CIBIL, ingresos, estado de empleo, monto del préstamo, entre otros.

**Fuente:** [UCI Machine Learning Repository: Loan Approval Dataset](https://archive.ics.uci.edu/ml/datasets/Loan+Approval)

**Columnas principales:**
- `loan_id`, número de dependientes, nivel educativo, estado de empleo, ingresos anuales, monto del préstamo, puntaje CIBIL, etc.

**Problema seleccionado:** Clasificación binaria de aprobación/rechazo de préstamos.

**Hallazgos iniciales:**
- El puntaje CIBIL tiene la mayor correlación con el estado del préstamo, indicando que es un factor importante para predecir la aprobación.
- La distribución de `loan_status` muestra un sesgo hacia las aprobaciones, lo que podría afectar la precisión del modelo.

---

### 4. **Conjunto de Datos de Clientes**
Este conjunto de datos contiene información sobre los clientes y su comportamiento de compra, lo que permite predecir el churn (abandono de clientes).

**Fuente:** [Kaggle: Customer Churn Dataset](https://www.kaggle.com/datasets)

**Columnas principales:**
- `CustomerID`, género, edad, región, productos adquiridos, valor de compra, etc.

**Problema seleccionado:** Predicción del abandono de clientes (churn).

---

## Resumen del EDA Inicial
A través de los análisis exploratorios realizados, se identificaron patrones en las relaciones entre las características y las variables objetivo en los distintos conjuntos de datos. Esto permitió seleccionar el problema de predicción más relevante y viable para un análisis más profundo.

## Problema Seleccionado
Después de analizar los distintos conjuntos de datos, se seleccionó el **problema de predicción de los costos del seguro de salud**. Este problema es relevante tanto desde el punto de vista práctico como académico, ya que permite explorar cómo diferentes factores, como la edad, el índice de masa corporal (IMC) y el hábito de fumar, pueden influir en los costos de la salud.

**Objetivos específicos:**
1. Realizar un análisis exploratorio detallado para entender las relaciones entre las características y los costos médicos.
2. Construir un modelo predictivo para estimar los costos de salud en función de estas variables.
3. Evaluar el desempeño del modelo y ajustar parámetros para mejorar su precisión.

## Instrucciones para Ejecutar

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <url_del_repositorio>


Aquí tienes el archivo README.md solicitado:

markdown
Copy code
# Análisis Inicial y Selección de Problema

## Descripción
Este proyecto tiene como objetivo realizar un análisis exploratorio de datos (EDA) sobre varios conjuntos de datos para seleccionar el problema más adecuado para aplicar técnicas de Machine Learning. A través de este proceso, se identifican patrones, relaciones y problemas que pueden ser modelados para obtener resultados predictivos. La selección del problema y la justificación del modelo utilizado es fundamental para la creación de soluciones de inteligencia artificial efectivas.

## Conjuntos de Datos Analizados

A continuación se describen los cuatro conjuntos de datos analizados:

### 1. **Conjunto de Datos de Seguro de Salud**
Este conjunto de datos tiene como objetivo predecir los costos del seguro de salud en función de diversas características del asegurado.

**Fuente:** [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)

**Columnas principales:**
- Edad, género, IMC, número de hijos cubiertos, si fuma o no, región y cargos médicos.

**Problema seleccionado:** Predicción de los costos médicos de los pacientes.

**Justificación del modelo de regresión lineal:**
- **Simplicidad y comprensión:** Fácil de entender e interpretar.
- **Relación lineal entre variables:** Las características como edad e IMC tienen una relación lineal con los cargos médicos.

---

### 2. **Conjunto de Datos de Animales del Zoológico**
Este conjunto contiene información sobre 101 animales con 16 características para predecir su clasificación en 7 clases diferentes: Mamífero, Ave, Reptil, Pez, Anfibio, Insecto e Invertebrado.

**Fuente:** [UCI Machine Learning Repository: Zoo Dataset](https://archive.ics.uci.edu/ml/datasets/Zoo)

**Columnas principales:**
- Nombre del animal, si tiene cabello, plumas, huevos, leche, puede volar, es acuático, etc.

**Problema seleccionado:** Clasificación multiclase de animales.

**Justificación del modelo de Random Forest:**
- **Precisión:** Random Forest alcanzó una precisión superior en comparación con KNN.
- **Manejo de variables categóricas y binarias:** Random Forest maneja bien estas variables sin necesidad de normalización.
- **Robustez al sobreajuste:** Random Forest es menos susceptible al sobreajuste en comparación con KNN.

---

### 3. **Conjunto de Datos de Aprobación de Préstamos**
Este conjunto de datos contiene información financiera utilizada para predecir la aprobación de préstamos en función de características como el puntaje CIBIL, ingresos, estado de empleo, monto del préstamo, entre otros.

**Fuente:** [UCI Machine Learning Repository: Loan Approval Dataset](https://archive.ics.uci.edu/ml/datasets/Loan+Approval)

**Columnas principales:**
- `loan_id`, número de dependientes, nivel educativo, estado de empleo, ingresos anuales, monto del préstamo, puntaje CIBIL, etc.

**Problema seleccionado:** Clasificación binaria de aprobación/rechazo de préstamos.

**Hallazgos iniciales:**
- El puntaje CIBIL tiene la mayor correlación con el estado del préstamo, indicando que es un factor importante para predecir la aprobación.
- La distribución de `loan_status` muestra un sesgo hacia las aprobaciones, lo que podría afectar la precisión del modelo.

---

### 4. **Conjunto de Datos de Clientes**
Este conjunto de datos contiene información sobre los clientes y su comportamiento de compra, lo que permite predecir el churn (abandono de clientes).

**Fuente:** [Kaggle: Customer Churn Dataset](https://www.kaggle.com/datasets)

**Columnas principales:**
- `CustomerID`, género, edad, región, productos adquiridos, valor de compra, etc.

**Problema seleccionado:** Predicción del abandono de clientes (churn).

---

## Resumen del EDA Inicial
A través de los análisis exploratorios realizados, se identificaron patrones en las relaciones entre las características y las variables objetivo en los distintos conjuntos de datos. Esto permitió seleccionar el problema de predicción más relevante y viable para un análisis más profundo.

## Problema Seleccionado
Después de analizar los distintos conjuntos de datos, se seleccionó el **problema de predicción de los costos del seguro de salud**. Este problema es relevante tanto desde el punto de vista práctico como académico, ya que permite explorar cómo diferentes factores, como la edad, el índice de masa corporal (IMC) y el hábito de fumar, pueden influir en los costos de la salud.

**Objetivos específicos:**
1. Realizar un análisis exploratorio detallado para entender las relaciones entre las características y los costos médicos.
2. Construir un modelo predictivo para estimar los costos de salud en función de estas variables.
3. Evaluar el desempeño del modelo y ajustar parámetros para mejorar su precisión.

## Instrucciones para Ejecutar

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone <url_del_repositorio>
Navega al directorio del proyecto:


# Autor
Delcy - Análisis de datos y modelado de regresión.