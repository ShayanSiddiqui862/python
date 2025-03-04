import streamlit as st
import pandas as pd
import numpy as np
import pdfplumber
from io import BytesIO

st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")
st.title("Growth Mindset Challenge")
st.write("Upload CSV, XLSX, or PDF files to analyze and clean data.")

# File uploader
uploaded_files = st.file_uploader("Upload your data", type=['csv', 'xlsx', 'pdf'], accept_multiple_files=True)

def read_pdf(file):
    with pdfplumber.open(file) as pdf:
        tables = []
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                tables.extend(table)
    return pd.DataFrame(tables[1:], columns=tables[0]) if tables else pd.DataFrame()

if uploaded_files:
    for file in uploaded_files:
        st.subheader(f"Processing: {file.name}")
        
        # Read file
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        elif file.name.endswith('.pdf'):
            df = read_pdf(file)
        else:
            st.error("Unsupported file format.")
            continue
        
        # Display data preview
        if not df.empty:
            st.write("Data Preview:")
            st.dataframe(df.head())
        else:
            st.warning("No data extracted from the PDF. It might not contain tabular data.")
            continue
        
        # Data Cleaning Options
        st.subheader("Data Cleaning:")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button(f"Remove Duplicates from {file.name}"):
                df.drop_duplicates(inplace=True)
                st.success("Duplicates removed.")
                st.dataframe(df.head())
        
        with col2:
            if st.button(f"Fill Missing Values in {file.name}"):
                numeric_cols = df.select_dtypes(include=[np.number]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.success("Missing values filled with column mean.")
                st.dataframe(df.head())
        
        # Data Transformation
        st.subheader("Data Transformation:")
        selected_cols = st.multiselect("Select columns to keep", df.columns, default=df.columns)
        df = df[selected_cols]
        st.subheader("Data Visualization options:")
    if st.checkbox("Show Visualization"):
        st.write("Select the columns to visualize")
        col1 , col2 = st.columns(2)
        with col1:
            x_axis = st.selectbox("X-axis", df.columns)
        with col2:
            y_axis = st.selectbox("Y-axis", df.columns)
        st.write(f"Selected columns for visualization: {x_axis} and {y_axis}")
        st.line_chart(df[[x_axis, y_axis]])
        
        # File Conversion
        st.subheader("Download Cleaned Data:")
        conv_type = st.radio("Select format", ["csv", "xlsx"], key=file.name)
        buffer = BytesIO()
        
        if conv_type == "csv":
            df.to_csv(buffer, index=False)
            file_name = file.name.replace(".xlsx", ".csv").replace(".pdf", ".csv")
            mime_type = "text/csv"
        else:
            df.to_excel(buffer, index=False)
            file_name = file.name.replace(".csv", ".xlsx").replace(".pdf", ".xlsx")
            mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        
        buffer.seek(0)
        st.download_button(
            label=f"Download {file.name} as {conv_type}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )

st.success("Thank you for using the app!")
