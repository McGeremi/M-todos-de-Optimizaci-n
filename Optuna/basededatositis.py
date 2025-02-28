from sklearn.datasets import load_iris
import pandas as pd

# Cargar el dataset Iris
iris = load_iris()

# Convertir a un DataFrame de pandas para facilitar la visualización
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Agregar la columna de especies (etiquetas)
df['species'] = iris.target

# Mapear los números de las clases a nombres de especies
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Mostrar las primeras filas del DataFrame
print(df.head())