import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, exp, sin, sympify, lambdify

# Solicitar al usuario que ingrese la función y el intervalo
input_function = input("Ingresa la función en términos de x (por ejemplo, x**2, x**3 - 4*x): ")
start = float(input("Ingresa el valor de inicio del intervalo: "))
end = float(input("Ingresa el valor de fin del intervalo: "))

# Definir la variable simbólica
x = symbols('x')

# Convertir la entrada del usuario en una expresión simbólica
f = sympify(input_function)

# Calcular la segunda derivada
f_prime2 = diff(f, x, 2)

# Convertir la segunda derivada a una función numérica
f_prime2_func = lambdify(x, f_prime2, "numpy")

# Evaluar la segunda derivada en un rango de valores
x_vals = np.linspace(start, end, 400)  # Dominio especificado por el usuario
f_prime2_vals = f_prime2_func(x_vals)

# Verificar si la segunda derivada es positiva en todo el dominio
is_convex = np.all(f_prime2_vals > 0)

# Imprimir el resultado
if is_convex:
    print("La función es convexa en el dominio.")
else:
    print("La función no es convexa en el dominio.")

# Convertir la función original a una función numérica
# Usar numpy para funciones como exp, sin, etc.
f_func = lambdify(x, f, "numpy")

# Evaluar la función original en el dominio
f_vals = f_func(x_vals)

# Graficar la función original y su segunda derivada
plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label=f"f(x) = {input_function}", color='blue')
plt.plot(x_vals, f_prime2_vals, label="f''(x)", color='red', linestyle='--')
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.legend()
plt.title(f"Demostración de Convexidad de {input_function}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
