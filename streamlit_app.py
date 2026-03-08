import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp

st.title("Bisection Method App")

# User inputs
function_text = st.text_input("Enter f(x)", "x**3 - x - 2")
a = st.number_input("Left endpoint a", value=1.0)
b = st.number_input("Right endpoint b", value=2.0)
n_iter = st.number_input("Iterations", min_value=1, max_value=50, value=12)

if st.button("Run"):

    x = sp.symbols("x")
    expr = sp.sympify(function_text)
    f = sp.lambdify(x, expr, "numpy")

    data = []

    for i in range(n_iter):
        c = (a + b) / 2
        data.append([i+1, a, b, c, f(c)])

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(data, columns=["Iteration", "a", "b", "c", "f(c)"])

    st.subheader("Approximate Root")
    st.write(c)

    st.subheader("Iterations Table")
    st.dataframe(df)

    xs = np.linspace(a-1, b+1, 400)
    ys = f(xs)

    fig, ax = plt.subplots()
    ax.plot(xs, ys)
    ax.axhline(0)
    ax.scatter(df["c"], f(df["c"]))
    ax.set_title("Bisection Method Visualization")

    st.pyplot(fig)
