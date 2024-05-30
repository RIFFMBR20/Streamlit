import streamlit as st
import pandas as pd

def main():
    st.title("Data Analysis with Streamlit")
    
    st.sidebar.title("Upload Your CSV")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            st.write("Data Preview:")
            st.write(data.head())
            
            if st.sidebar.checkbox("Show data summary"):
                st.write(data.describe())
            
            if st.sidebar.checkbox("Show column data types"):
                st.write(data.dtypes)
            
            visualize_data(data)
        except pd.errors.EmptyDataError:
            st.error("Error: The uploaded file is empty.")
        except pd.errors.ParserError:
            st.error("Error: The uploaded file is not a valid CSV.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.write("Please upload a CSV file to proceed.")
        
def visualize_data(data):
    st.sidebar.title("Data Visualization")
    st.sidebar.subheader("Select Chart Type")
    
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Histogram", "Scatter Plot"])
    
    if chart_type == "Bar Chart":
        st.sidebar.subheader("Bar Chart Settings")
        x_axis = st.sidebar.selectbox("Select X-axis", data.columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", data.columns)
        st.write(f"Bar Chart: {x_axis} vs {y_axis}")
        st.bar_chart(data[[x_axis, y_axis]])
    
    elif chart_type == "Line Chart":
        st.sidebar.subheader("Line Chart Settings")
        x_axis = st.sidebar.selectbox("Select X-axis", data.columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", data.columns)
        st.write(f"Line Chart: {x_axis} vs {y_axis}")
        st.line_chart(data[[x_axis, y_axis]])
    
    elif chart_type == "Histogram":
        st.sidebar.subheader("Histogram Settings")
        column = st.sidebar.selectbox("Select Column", data.columns)
        st.write(f"Histogram: {column}")
        st.hist_chart(data[column])
    
    elif chart_type == "Scatter Plot":
        st.sidebar.subheader("Scatter Plot Settings")
        x_axis = st.sidebar.selectbox("Select X-axis", data.columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", data.columns)
        st.write(f"Scatter Plot: {x_axis} vs {y_axis}")
        st.scatter_chart(data[[x_axis, y_axis]])

if __name__ == "__main__":
    main()
