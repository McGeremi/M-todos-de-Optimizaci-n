import streamlit as st
from fractions import Fraction
from sympy import Matrix

# Método de Sustitución
class SustitucionSolverStreamlit:
    def __init__(self):
        self.n = 0
        self.coeff_entries = []
        self.b_entries = []

    def crear_entrada_matriz(self):
        self.n = st.number_input("Dimensión de la matriz (n):", min_value=1, step=1)
        
        if self.n == 2:  # Aseguramos que el sistema tiene dos ecuaciones y dos incógnitas
            self.coeff_entries = []
            self.b_entries = []
            
            st.write("Ingrese los coeficientes de la matriz A:")
            for i in range(self.n):
                row = []
                for j in range(self.n):
                    row.append(st.number_input(f"A[{i+1},{j+1}]", key=f"coeff_{i}_{j}"))
                self.coeff_entries.append(row)

            st.write("Ingrese los valores del vector b:")
            for i in range(self.n):
                self.b_entries.append(st.number_input(f"b[{i+1}]", key=f"b_{i}"))

            if st.button("Resolver"):
                self.resolver_sistema()

    def resolver_sistema(self):
        # Convertir entradas a fracciones para evitar problemas con decimales
        coeficientes = []
        for i in range(self.n):
            coeficientes.append([Fraction(self.coeff_entries[i][j]) for j in range(self.n)])

        b_values = [Fraction(self.b_entries[i]) for i in range(self.n)]

        try:
            solution = self.sustitucion(coeficientes, b_values)
            self.mostrar_resultados(solution)
        except Exception as e:
            st.error(f"Error: {str(e)}")

    def sustitucion(self, matrix, b):
        # Para el sistema con 2 incógnitas
        x = [0] * 2
        # Despejamos x de la segunda ecuación: x = y + 1
        x[0] = b[1] + 1  # x = y + 1

        # Sustituimos en la primera ecuación: 3x + 2y = 16
        # 3(y + 1) + 2y = 16
        # 3y + 3 + 2y = 16
        # 5y = 13
        y = (b[0] - 3 * x[0]) / 5  # y = (16 - 3(y + 1)) / 5

        # Sustituimos y en x = y + 1
        x[0] = y + 1  # x = y + 1
        
        return [x[0], y]

    def mostrar_resultados(self, solution):
        st.subheader("Solución:")
        for i, sol in enumerate(solution):
            st.write(f"x{i + 1} = {Fraction(sol).limit_denominator()}")


# Método de Gauss-Jordan
class GaussJordanSolverStreamlit:
    def __init__(self):
        self.n = 0
        self.coeff_entries = []
        self.b_entries = []

    def crear_entrada_matriz(self):
        self.n = st.number_input("Dimensión de la matriz (n):", min_value=1, step=1)
        
        if self.n > 0:
            self.coeff_entries = []
            self.b_entries = []
            
            st.write("Ingrese los coeficientes de la matriz A:")
            for i in range(self.n):
                row = []
                for j in range(self.n):
                    row.append(st.number_input(f"A[{i+1},{j+1}]", key=f"coeff_{i}_{j}"))
                self.coeff_entries.append(row)

            st.write("Ingrese los valores del vector b:")
            for i in range(self.n):
                self.b_entries.append(st.number_input(f"b[{i+1}]", key=f"b_{i}"))

            if st.button("Resolver"):
                self.resolver_sistema()

    def resolver_sistema(self):
        coeficientes = []
        for i in range(self.n):
            coeficientes.append([Fraction(self.coeff_entries[i][j]) for j in range(self.n)])

        b_values = [Fraction(self.b_entries[i]) for i in range(self.n)]

        try:
            solution = self.gauss_jordan(coeficientes, b_values)
            self.mostrar_resultados(solution)
        except Exception as e:
            st.error(f"Error: {str(e)}")

    def gauss_jordan(self, matrix, b):
        n = len(matrix)
        A = [matrix[i] + [b[i]] for i in range(n)]

        for i in range(n):
            if A[i][i] == 0:
                raise ValueError("La matriz es singular, no se puede resolver el sistema.")
            divisor = A[i][i]
            for j in range(i, n + 1):
                A[i][j] /= divisor
            for k in range(n):
                if k != i:
                    factor = A[k][i]
                    for j in range(i, n + 1):
                        A[k][j] -= factor * A[i][j]

        solution = [A[i][n] for i in range(n)]
        return solution

    def mostrar_resultados(self, solution):
        st.subheader("Solución:")
        for i, sol in enumerate(solution):
            st.write(f"x{i + 1} = {Fraction(sol).limit_denominator()}")


# Método de Cramer
class CramerSolverStreamlit:
    def __init__(self):
        self.n = 0
        self.coeff_entries = []
        self.b_entries = []

    def crear_entrada_matriz(self):
        self.n = st.number_input("Dimensión de la matriz (n):", min_value=1, step=1)
        
        if self.n > 0:
            self.coeff_entries = []
            self.b_entries = []
            
            st.write("Ingrese los coeficientes de la matriz A:")
            for i in range(self.n):
                row = []
                for j in range(self.n):
                    row.append(st.number_input(f"A[{i+1},{j+1}]", key=f"coeff_{i}_{j}"))
                self.coeff_entries.append(row)

            st.write("Ingrese los valores del vector b:")
            for i in range(self.n):
                self.b_entries.append(st.number_input(f"b[{i+1}]", key=f"b_{i}"))

            if st.button("Resolver"):
                self.resolver_sistema()

    def resolver_sistema(self):
        coeficientes = []
        for i in range(self.n):
            coeficientes.append([Fraction(self.coeff_entries[i][j]) for j in range(self.n)])

        b_values = [Fraction(self.b_entries[i]) for i in range(self.n)]

        try:
            steps, solution = self.cramer(coeficientes, b_values)
            self.mostrar_resultados(steps, solution)
        except Exception as e:
            st.error(f"Error: {str(e)}")

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
        st.subheader("Pasos:")
        for step in steps:
            st.write(step)

        st.subheader("Solución:")
        for i, sol in enumerate(solution):
            st.write(f"x{i + 1} = {Fraction(sol).limit_denominator()}")


# Integración al menú
def main():
    st.title("Sistema de Ecuaciones Lineales")
    st.sidebar.title("Menú de Métodos")
    
    metodo = st.sidebar.radio("Selecciona un método:", ["Método de Gauss-Jordan", "Método de Cramer", "Método de Sustitución"])
    
    if metodo == "Método de Sustitución":
        solver = SustitucionSolverStreamlit()
        solver.crear_entrada_matriz()

    elif metodo == "Método de Gauss-Jordan":
        solver = GaussJordanSolverStreamlit()
        solver.crear_entrada_matriz()

    elif metodo == "Método de Cramer":
        solver = CramerSolverStreamlit()
        solver.crear_entrada_matriz()

if __name__ == "__main__":
    main()
