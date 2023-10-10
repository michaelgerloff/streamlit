import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!")
st.write("What do you mean?")
st.write("Are you talking to me?")
st.write("Are you bored? Choose a number")


a = st.sidebar.radio("Select one:", [1, 2])
if a == 1:
    st.video("https://www.youtube.com/watch?v=xSp2I0ObdW4")
else:
    st.write("WRONG!")


col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

st.checkbox("I agree")

st.multiselect("Buy", ["milk", "butter", "bread"])
st.slider("pick a number", 0, 100)
st.time_input("Meeting Time")


DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)
nrows = 1000


@st.cache_data
def load_data(DATA_URL_, nrows_):
    data = pd.read_csv(DATA_URL_, nrows=nrows_)
    data = data.rename(columns={"Lat": "LAT", "Lon": "LON"})
    return data


data = load_data(DATA_URL, nrows)
st.dataframe(data)
st.map(data.loc[:, ["LAT", "LON"]])

times = pd.to_datetime(data.loc[:, "Date/Time"])
data_summary = data.groupby([times.dt.day, times.dt.hour])["Base"].value_counts()
# st.bar_chart(data_summary)
