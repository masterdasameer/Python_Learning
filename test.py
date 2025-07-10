import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('My First Streamlit App')

# Add some text
st.write('Hello, Samirone Goswami! This is your initial Streamlit application.')

# Display a data table
st.subheader('Random Data Table')
data = pd.DataFrame({
    'col1': np.random.randn(10),
    'col2': np.random.randn(10),
    'col3': np.random.randn(10)
})
st.dataframe(data)

# Add a slider
st.subheader('Interactive Slider')
x = st.slider('Select a value for x', 0, 100, 25) # min, max, default
st.write(f'You selected: {x}')

# Add a button
if st.button('Click me!'):
    st.write('Button clicked!')
