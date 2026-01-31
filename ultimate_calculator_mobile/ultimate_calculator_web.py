# ultimate_calculator_web.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import os

# Symbol for calculations
x = sp.symbols('x')

# Create folder for plots
os.makedirs("Plots", exist_ok=True)

# Function to convert user-friendly symbols to Python/SymPy syntax
def convert_math_symbols(expr):
    expr = expr.replace('×', '*')
    expr = expr.replace('÷', '/')
    expr = expr.replace('^', '**')
    expr = expr.replace('π', 'pi')
    return expr

class CalculatorLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # Input box
        self.expr_input = TextInput(
            hint_text='Enter math expression',
            multiline=False,
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.expr_input)

        # Result label
        self.result_label = Label(
            text='Result will appear here',
            size_hint_y=None,
            height=40
        )
        self.add_widget(self.result_label)

        # Button style
        button_style = {'size_hint_y': None, 'height': 50}

        # Evaluate button
        self.btn_evaluate = Button(text='Evaluate', background_color=(0.4, 0.7, 0.9, 1), **button_style)
        self.btn_evaluate.bind(on_press=self.evaluate)
        self.add_widget(self.btn_evaluate)

        # Derivative button
        self.btn_derivative = Button(text='Derivative', background_color=(0.9, 0.5, 0.2, 1), **button_style)
        self.btn_derivative.bind(on_press=self.derivative)
        self.add_widget(self.btn_derivative)

        # Integral button
        self.btn_integral = Button(text='Integral', background_color=(0.5, 0.9, 0.5, 1), **button_style)
        self.btn_integral.bind(on_press=self.integral)
        self.add_widget(self.btn_integral)

        # Plot button
        self.btn_plot = Button(text='Plot', background_color=(0.8, 0.6, 0.9, 1), **button_style)
        self.btn_plot.bind(on_press=self.plot)
        self.add_widget(self.btn_plot)

    def evaluate(self, instance):
        try:
            expr = convert_math_symbols(self.expr_input.text)
            result = sp.sympify(expr)
            self.result_label.text = f"Result: {result}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def derivative(self, instance):
        try:
            expr = convert_math_symbols(self.expr_input.text)
            deriv = sp.diff(sp.sympify(expr), x)
            self.result_label.text = f"Derivative: {deriv}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def integral(self, instance):
        try:
            expr = convert_math_symbols(self.expr_input.text)
            integ = sp.integrate(sp.sympify(expr), x)
            self.result_label.text = f"Integral: {integ}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

    def plot(self, instance):
        try:
            expr = convert_math_symbols(self.expr_input.text)
            f = sp.lambdify(x, sp.sympify(expr), modules=['numpy'])
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f(x_vals)
            plt.figure(figsize=(5,4))
            plt.plot(x_vals, y_vals, label=f"y={expr}")
            plt.title("Plot of the expression")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)
            plt.legend()
            filename = f"Plots/plot_{len(os.listdir('Plots'))+1}.png"
            plt.savefig(filename)
            plt.close()
            self.result_label.text = f"Plot saved: {filename}"
        except Exception as e:
            self.result_label.text = f"Error: {e}"

class UltimateCalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == "__main__":
    UltimateCalculatorApp().run()
