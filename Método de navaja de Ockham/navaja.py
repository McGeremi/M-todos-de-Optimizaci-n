import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.datasets import fetch_california_housing

# Cargar dataset
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["Price"] = data.target * 100000  # Convertir a dolares
print(df.head())

# Separar variables predictoras y objetivo
X = df.drop(columns=["Price"])
y = df["Price"]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo Completo
modelo_completo = LinearRegression()
modelo_completo.fit(X_train, y_train)
y_pred_completo = modelo_completo.predict(X_test)

# Modelo Simplificado (Lasso - Navaja de Ockham)
modelo_simplificado = Lasso(alpha=50000)
modelo_simplificado.fit(X_train, y_train)
y_pred_simplificado = modelo_simplificado.predict(X_test)

# Evaluación del error en ambos modelos
mse_completo = mean_squared_error(y_test, y_pred_completo)
mse_simplificado = mean_squared_error(y_test, y_pred_simplificado)

print(f"Error del Modelo Completo: {mse_completo}")
print(f"Error del Modelo Simplificado (Lasso - Ockham): {mse_simplificado}")

# Mostrar coeficientes eliminados en Lasso
coef_completo = modelo_completo.coef_
coef_simplificado = modelo_simplificado.coef_

print("Coeficientes del Modelo Completo:", coef_completo)
print("Coeficientes del Modelo Simplificado (Ockham - Lasso):", coef_simplificado)

# Mostrar las variables eliminadas por Lasso
variables = np.array(data.feature_names)
eliminadas = variables[modelo_simplificado.coef_ == 0]
print("Variables eliminadas por Lasso:", eliminadas)

# Visualización
plt.figure(figsize=(8,5))
plt.bar(data.feature_names, coef_completo, alpha=0.5, label="Regresión Lineal")
plt.bar(data.feature_names, coef_simplificado, alpha=0.5, label="Lasso (Ockham)")
plt.legend()
plt.xticks(rotation=45)
plt.ylabel("Importancia del Coeficiente")
plt.title("Comparación de Modelos (Ockham vs Complejo)")
plt.show()
