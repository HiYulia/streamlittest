import streamlit as st
import pandas as pd
import numpy as np

st.title("My App")

st.write("Hello, World!")

# Create sample data instead of reading from file
df = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10)
})

st.line_chart(df)