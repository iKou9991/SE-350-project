import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# Title
st.title('Streamlit Demo')

# Header
st.header('This is a header')

# Subheader
st.subheader('This is a subheader')

# Text
st.write('This is some text.')

# Markdown
st.markdown('## This is a Markdown title')

# Dataframes
st.write('A DataFrame:')
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write(df)

# Line chart
st.write('Line Chart:')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.write(chart_data)
st.line_chart(chart_data)

# Map
st.write('Map:')
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.write(map_data)
st.map(map_data)

# Checkbox
st.write('Checkbox:')
if st.checkbox('Show dataframe'):
    st.write(df)

# Selectbox
st.write('Selectbox:')
option = st.selectbox(
    'Which number do you like best?',
    df['Column 1']
)
'You selected:', option

# Multiselect
st.write('Multiselect:')
options = st.multiselect(
    'What are your favorite numbers?',
    df['Column 1']
)
'You selected:', options

# Slider
st.write('Slider:')
x = st.slider('Select a value', 0, 100, 50)
'You selected:', x

# File upload
st.write('File Upload:')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# Image
st.write('Display Image:')
img = Image.open('kitty.jpg')
st.image(img, caption='Sunset', use_column_width=True)

# Progress bar
st.write('Progress Bar:')
import time
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)
