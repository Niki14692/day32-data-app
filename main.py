import pandas
import streamlit as st
import plotly.express as px
# add title
st.title("In Search for Happiness")

# add selectbox
option_x =st.selectbox("Select the data for the X-axis",("GDP", "Happiness", "Generosity"))
option_y =st.selectbox("Select the data for the Y-axis",("GDP", "Happiness", "Generosity"))

# Load the dataframe
df = pandas.read_csv("happy.csv")

# match the value of the first option
match option_x:
    case "GDP":
        x_array = df["gdp"]
    case "Happiness":
        x_array = df["happiness"]
    case "Generosity":
        x_array = df["generosity"]
# match the value of the second option
match option_y:
    case "GDP":
        y_array = df["gdp"]
    case "Happiness":
        y_array = df["happiness"]
    case "Generosity":
        y_array = df["generosity"]

# add chart
st.subheader(f"{option_x} and {option_y}")
figure =px.scatter(x=x_array, y=y_array, labels={"x":f"{option_x}", "y":f"{option_y}"})
st.plotly_chart(figure)
