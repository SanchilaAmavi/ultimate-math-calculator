# ultimate_math_calculator.py
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define symbols
x, y, z = sp.symbols('x y z')


# Evaluate normal expressions
def calculate(expr):
    try:
        return sp.sympify(expr)
    except Exception as e:
        return f"Error: {e}"

# Plot expressions
def plot_expression(expr):
    try:
        sym_expr = sp.sympify(expr)
        f = sp.lambdify(x, sym_expr, "numpy")

        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        plt.plot(x_vals, y_vals)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"y = {expr}")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print("Plot Error:", e)

# Solve equations
def solve_equation(equation_str):
    try:
        eq = sp.sympify(equation_str)
        solutions = sp.solve(eq, x)
        return solutions
    except Exception as e:
        return f"Error: {e}"

# Differentiation
def differentiate(expr_str):
    try:
        expr = sp.sympify(expr_str)
        return sp.diff(expr, x)
    except Exception as e:
        return f"Error: {e}"

# Integration
def integrate_expr(expr_str):
    try:
        expr = sp.sympify(expr_str)
        return sp.integrate(expr, x)
    except Exception as e:
        return f"Error: {e}"

# Matrix operations
def matrix_operations(matrix_input):
    try:
        # matrix_input comes as Python list of lists
        clean_matrix = [[float(cell) for cell in row] for row in matrix_input]
        M = sp.Matrix(clean_matrix)
        det = M.det()
        trans = M.T
        inv = M.inv() if det != 0 else "Matrix not invertible"
        return {"Matrix": M, "Determinant": det, "Transpose": trans, "Inverse": inv}
    except Exception as e:
        return f"Error: {e}"


print("=== Ultimate Math Calculator ===")
print("Commands:")
print("  math expression (2+3*4, sin(pi/2), etc.)")
print("  plot x^2 + 3*x")
print("  solve x^2 + 3*x + 2")
print("  diff x^3 + 5*x")
print("  integrate x^2 + 3*x")
print("  matrix [[1,2],[3,4]]")
print("  exit")
print("===============================")

while True:
    user_input = input(">> ").strip()

    if user_input.lower() == "exit":
        break

    # Matrix handling
    if user_input.startswith("matrix"):
        expr = user_input.replace("matrix", "").strip()
        try:
            # Convert string to Python list
            matrix_list = eval(expr)
        except:
            print("Invalid matrix format. Use [[1,2],[3,4]]")
            continue
        result = matrix_operations(matrix_list)
        print("Matrix operations:")
        for k, v in result.items():
            print(f"{k}: {v}")
        continue

    # Plotting
    if user_input.startswith("plot"):
        expr = user_input.replace("plot", "").strip()
        plot_expression(expr)
        continue

    # Solve
    if user_input.startswith("solve"):
        eq = user_input.replace("solve", "").strip()
        solutions = solve_equation(eq)
        print("Solutions:", solutions)
        continue

    # Differentiate
    if user_input.startswith("diff"):
        expr = user_input.replace("diff", "").strip()
        derivative = differentiate(expr)
        print("Derivative:", derivative)
        continue

    # Integrate
    if user_input.startswith("integrate"):
        expr = user_input.replace("integrate", "").strip()
        integral = integrate_expr(expr)
        print("Integral:", integral)
        continue

    # Otherwise: normal math
    print("=", calculate(user_input))
