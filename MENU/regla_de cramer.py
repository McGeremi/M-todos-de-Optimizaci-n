from tkinter import Tk, Frame, Label, Entry, Button, Text, Scrollbar, messagebox, Toplevel
from fractions import Fraction
from sympy import Matrix
import tkinter.font as tkFont

class CramerSolver:
    def __init__(self):
        self.n = 0
        self.coeff_entries = []
        self.b_entries = []
        self.root = Tk()
        self.root.title("Resolución de Sistema de Ecuaciones por Cramer")
        self.root.geometry("600x500") 
        self.root.config(bg="#1e1e1e")
        
        # Definir fuentes
        self.font_large = tkFont.Font(family="Arial", size=14, weight="bold")
        self.font_medium = tkFont.Font(family="Arial", size=12)

        # Crear el marco principal
        self.coeff_frame = Frame(self.root, bg="#1e1e1e")
        self.coeff_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Etiqueta para la dimensión de la matriz
        self.eq_label = Label(self.coeff_frame, text="Dimensión de la matriz (n):", fg="#f8f8f8", bg="#1e1e1e", font=self.font_medium)
        self.eq_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Entrada para la dimensión de la matriz
        self.eq_entry = Entry(self.coeff_frame, width=6, font=self.font_medium, bd=2, relief="solid")
        self.eq_entry.grid(row=0, column=1, padx=5, pady=5)

        # Botón para crear la matriz
        self.create_button = Button(self.coeff_frame, text="Establecer matriz", command=self.crear_casillas, bg="#007BFF", fg="#ffffff", font=self.font_medium, relief="flat", width=20)
        self.create_button.grid(row=0, column=2, padx=5, pady=5)

        # Botón para resolver el sistema
        self.solve_button = Button(self.coeff_frame, text="Resolver", command=self.resolver_sistema, bg="#28a745", fg="#ffffff", font=self.font_medium, relief="flat", width=20)
        self.solve_button.grid(row=0, column=3, padx=5, pady=5)

        self.centrar_ventana()  
    
    def crear_casillas(self):
        try:
            self.n = int(self.eq_entry.get())
            if self.n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número entero positivo.")
            return
        
        for entry_row in self.coeff_entries:
            for entry in entry_row:
                entry.destroy()
        for entry in self.b_entries:
            entry.destroy()
        self.coeff_entries.clear()
        
        for i in range(self.n):
            row_entries = []
            for j in range(self.n):
                entry = Entry(self.coeff_frame, width=10, font=self.font_medium, bd=2, relief="solid")
                entry.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
                row_entries.append(entry)
            self.coeff_entries.append(row_entries)
        
        self.b_entries.clear()
        for i in range(self.n):
            entry = Entry(self.coeff_frame, width=10, font=self.font_medium, bd=2, relief="solid")
            entry.grid(row=i + 1, column=self.n, padx=5, pady=5, sticky="nsew")
            self.b_entries.append(entry)

        self.root.update()

    def resolver_sistema(self):
        coeficientes = []
        for row_entries in self.coeff_entries:
            fila = []
            for entry in row_entries:
                try:
                    valor = Fraction(entry.get())
                except ValueError:
                    messagebox.showerror("Error", "Ingrese un número válido.")
                    return
                fila.append(valor)
            coeficientes.append(fila)

        b_values = []
        for entry in self.b_entries:
            try:
                valor = Fraction(entry.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido para el vector b.")
                return
            b_values.append(valor)

        try:
            steps, solution = self.cramer(coeficientes, b_values)
            self.mostrar_resultados(steps, solution)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def cramer(self, matrix, b):
        n = len(matrix)
        A = Matrix(matrix)
        B = Matrix(b)
        determinant = A.det()
        if determinant == 0:
            raise ValueError("La matriz es singular, no se puede resolver el sistema.")
        steps = []
        solution = []
        for i in range(n):
            A_i = A.copy()
            A_i[:, i] = B
            step = f"Paso {i + 1}:\n\n"
            step += f"Matriz A:\n{A_i}\n\n"
            step += f"Vector b:\n{B}\n\n"
            step += f"Determinante de A: {determinant}\n\n"
            determinant_i = A_i.det()
            step += f"Determinante de A{i + 1}: {Fraction(determinant_i).limit_denominator()}\n\n"
            solution_i = determinant_i / determinant
            step += f"Solución x{i + 1}: {Fraction(solution_i).limit_denominator()}\n\n"
            steps.append(step)
            solution.append(solution_i)
        return steps, solution

    def mostrar_resultados(self, steps, solution):
        results_window = Toplevel(self.root)
        results_window.title("Resultados")
        results_window.geometry("700x500")
        results_window.config(bg="#f8f8f8")
        self.centrar_ventana(results_window)

        results_frame = Frame(results_window, bg="#f8f8f8")
        results_frame.pack(fill="both", expand=True)

        output_text = Text(results_frame, font=self.font_medium, bg="#f8f8f8", fg="#000000", wrap="word", bd=2, relief="solid")
        output_text.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = Scrollbar(output_text)
        scrollbar.pack(side="right", fill="y")
        output_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=output_text.yview)

        output_text.insert("end", "Pasos:\n\n")
        for step in steps:
            output_text.insert("end", step)
        output_text.insert("end", "Solución:\n\n")
        for i, sol in enumerate(solution):
            output_text.insert("end", f"x{i + 1} = {Fraction(sol).limit_denominator()}\n")
        output_text.config(state="disabled")

    def centrar_ventana(self, ventana=None):
        if not ventana:
            ventana = self.root
        ventana.update_idletasks()
        ventana_width = ventana.winfo_width()
        ventana_height = ventana.winfo_height()
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()
        x = (screen_width // 2) - (ventana_width // 2)
        y = (screen_height // 2) - (ventana_height // 2)
        ventana.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

solver = CramerSolver()
solver.root.mainloop()
