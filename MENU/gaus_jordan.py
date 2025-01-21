import tkinter as tk
from tkinter import messagebox

def format_number(num):
    """Formatea el número: si es entero, lo muestra como entero; si tiene decimales, lo muestra con 2 decimales."""
    if num.is_integer():
        return str(int(num))  
    else:
        return f"{num:.2f}"  

def gauss_jordan(A, B):
    n = len(A)
    m = len(A[0])
    steps = []  

    AugmentedMatrix = [A[i] + [B[i]] for i in range(n)]
    steps.append(f"Inicial:\n{format_matrix(AugmentedMatrix)}")
    
    for i in range(min(n, m)): 
        max_row = max(range(i, n), key=lambda r: abs(AugmentedMatrix[r][i]))
        AugmentedMatrix[i], AugmentedMatrix[max_row] = AugmentedMatrix[max_row], AugmentedMatrix[i]
        steps.append(f"Intercambio fila {i} con fila {max_row}:\n{format_matrix(AugmentedMatrix)}")
        
        div = AugmentedMatrix[i][i]
        if div == 0:
            return None, steps  
        for j in range(i, m + 1):
            AugmentedMatrix[i][j] /= div
        
        steps.append(f"Normalización fila {i}:\n{format_matrix(AugmentedMatrix)}")
        
        for j in range(n):
            if j != i:
                factor = AugmentedMatrix[j][i]
                for k in range(i, m + 1):
                    AugmentedMatrix[j][k] -= factor * AugmentedMatrix[i][k]
                
                steps.append(f"Fila {j} - ({factor}) * Fila {i}:\n{format_matrix(AugmentedMatrix)}")
    
    solution = [AugmentedMatrix[i][m] for i in range(n)]
    return solution, steps

def format_matrix(matrix):
    """Formatea la matriz para mostrarla de manera adecuada, con los números enteros sin decimales innecesarios."""
    return "\n".join(["\t".join(map(lambda x: format_number(x), row)) for row in matrix])

def generate_inputs():
    try:
        rows = int(entry_rows.get())
        columns = int(entry_columns.get())
        
        if rows <= 0 or columns <= 0:
            messagebox.showerror("Error", "Las filas y columnas deben ser números positivos.")
            return

        for widget in frame_inputs.winfo_children():
            widget.destroy()

        global entry_A
        entry_A = []
        for i in range(rows):
            row_entries = []
            for j in range(columns):
                entry = tk.Entry(frame_inputs, width=10)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            entry_A.append(row_entries)

        global entry_B
        entry_B = []
        tk.Label(frame_inputs, text="Matriz B (resultados):", fg="white", bg="#001f3d").grid(row=rows, column=0, columnspan=columns, pady=10)
        for i in range(rows):
            entry_val = tk.Entry(frame_inputs, width=10)
            entry_val.grid(row=i, column=columns, padx=5, pady=5)
            entry_B.append(entry_val)

        tk.Button(root, text="Resolver", command=solve_system, font=("Arial", 12), bg="#2196F3", fg="white").grid(row=2, column=0, columnspan=4, pady=10)
        
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos para las filas y columnas.")

def solve_system():
    try:
        A = [[float(entry_A[i][j].get()) for j in range(len(entry_A[i]))] for i in range(len(entry_A))]
        
        B = [float(entry_B[i].get()) for i in range(len(entry_B))]

        solution, steps = gauss_jordan(A, B)
        
        if solution is None:
            messagebox.showerror("Error", "El sistema no tiene solución única.")
        else:
            result_var.set(f"Solución: {', '.join(map(format_number, solution))}")
            steps_var.set("\n\n".join(steps))
            
            frame_inside_canvas.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en los datos ingresados: {e}")

root = tk.Tk()
root.title("Método de Gauss-Jordan paso a paso")
root.geometry("900x600")
root.config(bg="#001f3d")  

window_width = 900
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

main_frame = tk.Frame(root, bg="#001f3d")
main_frame.grid(row=0, column=0, sticky="nsew")

header_label = tk.Label(main_frame, text="Método de Gauss-Jordan", font=("Arial", 20, "bold"), bg="#001f3d", fg="#fff")
header_label.grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(main_frame, text="Número de filas:", font=("Arial", 12), bg="#001f3d", fg="white").grid(row=1, column=0, padx=5, pady=5)
entry_rows = tk.Entry(main_frame, font=("Arial", 12))
entry_rows.grid(row=1, column=1, padx=5, pady=5)

tk.Label(main_frame, text="Número de columnas:", font=("Arial", 12), bg="#001f3d", fg="white").grid(row=1, column=2, padx=5, pady=5)
entry_columns = tk.Entry(main_frame, font=("Arial", 12))
entry_columns.grid(row=1, column=3, padx=5, pady=5)

tk.Button(main_frame, text="Generar Entradas", command=generate_inputs, font=("Arial", 12), bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=4, pady=10)

frame_inputs = tk.Frame(main_frame, bg="#001f3d")
frame_inputs.grid(row=3, column=0, columnspan=4)

frame_output = tk.Frame(main_frame, bg="#001f3d")
frame_output.grid(row=4, column=0, columnspan=4, pady=10)

canvas = tk.Canvas(frame_output, bg="#001f3d")
canvas.grid(row=0, column=0, columnspan=4, sticky="nsew")

scrollbar = tk.Scrollbar(frame_output, orient="vertical", command=canvas.yview)
scrollbar.grid(row=0, column=5, sticky="ns")
canvas.config(yscrollcommand=scrollbar.set)

frame_inside_canvas = tk.Frame(canvas, bg="#001f3d")
canvas.create_window((0, 0), window=frame_inside_canvas, anchor="nw")

steps_var = tk.StringVar()
steps_label = tk.Label(frame_inside_canvas, textvariable=steps_var, font=("Arial", 12), bg="#001f3d", fg="white", justify="left")
steps_label.grid(row=0, column=0)

result_var = tk.StringVar()
result_label = tk.Label(frame_inside_canvas, textvariable=result_var, font=("Arial", 12), bg="#001f3d", fg="green")
result_label.grid(row=1, column=0)

root.mainloop()
