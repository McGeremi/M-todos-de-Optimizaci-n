import optuna
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from collections import Counter

# Cargar los datos
data = pd.read_csv("trama_UO_usuarios_202410.csv", encoding="latin-1")

# Calcular la moda y frecuencia de los apellidos
primer_apellidos = data["PRIMER_APELLIDO"].dropna().tolist()
segundo_apellidos = data["SEGUNDO_APELLIDO"].dropna().tolist()

contador_primer_apellido = Counter(primer_apellidos)
contador_segundo_apellido = Counter(segundo_apellidos)

moda_primer_apellido, freq_primer = contador_primer_apellido.most_common(1)[0]
moda_segundo_apellido, freq_segundo = contador_segundo_apellido.most_common(1)[0]

print(f"Moda Primer Apellido: {moda_primer_apellido} ({freq_primer} veces)")
print(f"Moda Segundo Apellido: {moda_segundo_apellido} ({freq_segundo} veces)")

# Preprocesamiento
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Separar características (X) y variable objetivo (y)
X = data.drop(columns=["TIPO_USUARIO"])
y = data["TIPO_USUARIO"]

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Función objetivo para Optuna
def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 2, 200)
    max_depth = trial.suggest_int("max_depth", 2, 32, log=True)
    min_samples_split = trial.suggest_float("min_samples_split", 0.1, 1.0)
    min_samples_leaf = trial.suggest_float("min_samples_leaf", 0.1, 0.5)

    clf = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        random_state=42
    )
    
    score = cross_val_score(clf, X_train, y_train, cv=3, n_jobs=-1).mean()
    return score

# Crear un estudio de Optuna y optimizar
study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=100)

# Obtener los mejores hiperparámetros
trial = study.best_trial
print("Best accuracy: {}".format(trial.value))
print("Best hyperparameters: {}".format(trial.params))