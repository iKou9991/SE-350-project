import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Assignment using streamlit')

st.header('Tasks:')

st.subheader('1. Reading the Data:')
st.write('- Read the csv file.')
st.write('- Remove any unnecessary columns (e.g., columns with IDs or columns that you won’t use in this assignment).')
st.write('- Show the data in a table.')

#Read the csv file.
df = pd.read_csv("museum_data.csv")

st.title("Read the csv file.")  # add a title
st.write(df)

#Remove any unnecessary columns
st.title("Drop colum of the data frame and then show the data")  # add a title
df.drop(columns=['Museum ID', 'Legal Name', 'Alternate Name', 'Institution Name',
                'Street Address (Administrative Location)', 'Street Address (Physical Location)',
                'City (Physical Location)', 'State (Physical Location)','Zip Code (Physical Location)',
                'Phone Number','Employer ID Number', 'Tax Period'], axis=1, inplace=True)

st.write(df)


#----------------------------------------------------------------------------------------------------------------------

st.subheader('2. Data Summarization and Statistics:')
st.write('- Calculate the total number of museums in the dataset.')
st.write('- Calculate the average income per museum type.')
st.write('- Show the above information in a clear way with a header and formatted numbers below.')

# Read the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("museum_data.csv")
    return df

df = load_data()

# Calculate the total number of museums
total_museums = len(df)

# Display the total number of museums
st.write("# Total number of museums:", total_museums)

# Calculate the average income per museum type
average_income_per_type = df.groupby('Museum Type')['Income'].mean()

# Display the information
st.write("# Average Income per Museum Type")
for museum_type, avg_income in average_income_per_type.items():
    st.write(f"- {museum_type}: ${avg_income:.2f}")

#----------------------------------------------------------------------------------------------------------------------

st.subheader('3. Data Visualization:')
st.write('- Create a pie chart to visualize the distribution of museums by type.')
st.write('- Create visualizations to explore the relationship between income and revenue.')
st.write('- Show museums on the map as markers, where the marker color depends on the type of the museum. You can choose any colors you like.')

def load_data():
    df = pd.read_csv("museum_data.csv")
    return df

df = load_data()

# Task 1: Pie chart to visualize museum distribution by type
st.write("# Museum Distribution by Type")
museum_type_counts = df['Museum Type'].value_counts()
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(museum_type_counts, labels=museum_type_counts.index, autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

# Task 2: Visualizations to explore the relationship between income and revenue
st.write("# Relationship Between Income and Revenue")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=df, x='Income', y='Revenue', ax=ax)
st.pyplot(fig)

# Task 3: Show museums on the map with marker color based on museum type
# Map
df = pd.read_csv("museum_data.csv")
df = df.dropna(subset=['Latitude', 'Longitude'])
# Rename the columns to 'lat' and 'lon' for compatibility with st.map()
df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}, inplace=True)

# Define color mapping for different museum types
color_mapping = {
    'ARBORETUM, BOTANICAL GARDEN, OR NATURE CENTER': '#33FF39',
    'ART MUSEUM': '#33FCFF',
    "CHILDREN'S MUSEUM": '#6133FF',
    'GENERAL MUSEUM': '#FF9933',
    'HISTORIC PRESERVATION': '#FF3333',
    'HISTORY MUSEUM': '#F0FF33',
    'NATURAL HISTORY MUSEUM': '#C27D0C',
    'SCIENCE & TECHNOLOGY MUSEUM OR PLANETARIUM': '#F31AE9',
    'ZOO, AQUARIUM, OR WILDLIFE CONSERVATION': '#2A1AF3'
}

# Map museum types to marker colors
df['marker_color'] = df['Museum Type'].map(color_mapping)

# Select only the first 100 rows of the DataFrame
df_first_100 = df.head(100)

# Write only the Latitude and Longitude data for the first 100 rows
st.write("Latitude and Longitude Data (First 100 Rows):")
st.write(df_first_100[['lat', 'lon']])

# Display the map with markers colored by museum type for the first 100 rows
st.map(df_first_100)