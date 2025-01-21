import tkinter as tk
from tkinter import messagebox
import numpy as np
import re

def resolver():
    try:
        # Getting the number of equations
        n = int(entry_num_ecuaciones.get())
        
        if n <= 0:
            raise ValueError("El número de ecuaciones debe ser mayor que cero.")
        
        # Parsing the system of equations
        ecuaciones = text_ecuaciones.get("1.0", tk.END).strip().split('\n')
        
        if len(ecuaciones) != n:
            raise ValueError(f"Debes ingresar exactamente {n} ecuaciones.")
        
        coeficientes = []
        resultados = []
        
        # Regular expression to find terms like '3x', '-y', 'x', etc.
        patron = r"([+-]?\d*\.?\d*)\s?([a-zA-Z]+)"

        for ecuacion in ecuaciones:
            partes = ecuacion.split('=')
            if len(partes) != 2:
                raise ValueError("Ecuación mal formateada. Debe tener la forma 'ax + by = c'.")
            
            izquierda = partes[0].strip()
            resultado = float(partes[1].strip())
            resultados.append(resultado)
            
            coef = [0] * n  # Initialize coefficients list
            
            # Handle implicit coefficients for x and y, e.g., 3x or -y
            terms = re.findall(patron, izquierda)
            for coef_var, var in terms:
                # If coef_var is empty (e.g., just 'x' or '-y'), set it to +1 or -1
                coef_value = float(coef_var) if coef_var not in ["", "+", "-"] else float(coef_var + "1")
                
                # Identify the position of the variable (e.g., x is the first variable)
                var_index = ord(var.lower()) - ord('x')  # Assuming variables are 'x', 'y', 'z', etc.
                coef[var_index] = coef_value
            
            coeficientes.append(coef)
        
        # Convert lists to NumPy arrays
        coeficientes = np.array(coeficientes)
        resultados = np.array(resultados)
        
        # Solve the system using NumPy
        soluciones = np.linalg.solve(coeficientes, resultados)
        
        # Display the results
        result_text = "\nLas soluciones del sistema son:\n"
        for i, sol in enumerate(soluciones):
            result_text += f"x{i+1} = {sol:.4f}\n"
        
        label_resultado.config(text=result_text)
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
ventana = tk.Tk()
ventana.title("Sistema de Ecuaciones Lineales")

# Instructions Label
label_instrucciones = tk.Label(ventana, text="Ingresa el número de ecuaciones y luego las ecuaciones.", font=("Arial", 12))
label_instrucciones.pack(pady=10)

# Entry for number of equations
label_num_ecuaciones = tk.Label(ventana, text="Número de ecuaciones:", font=("Arial", 12))
label_num_ecuaciones.pack(pady=5)
entry_num_ecuaciones = tk.Entry(ventana, font=("Arial", 12))
entry_num_ecuaciones.pack(pady=5)

# Label for input format
label_formato = tk.Label(ventana, text="Formato: ax + by = c", font=("Arial", 12))
label_formato.pack(pady=5)

# Text box for equations
text_ecuaciones = tk.Text(ventana, height=6, width=30, font=("Arial", 12))
text_ecuaciones.pack(pady=10)

# Button to trigger the solver
boton_resolver = tk.Button(ventana, text="Resolver", command=resolver, font=("Arial", 12))
boton_resolver.pack(pady=10)

# Label to display results
label_resultado = tk.Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=10)

# Start the GUI loop
ventana.mainloop()
