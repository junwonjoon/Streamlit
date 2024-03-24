import streamlit as st
from requests import get
import datetime

key = st.secrets["API_KEY"]
st.title("Hello")
today_date = datetime.datetime.now()
genre = st.radio(
    "What stock price do you want to see?",
    ["Google", "Apple", "Microsoft", "NVIDIA"])



st.write("You selected:", genre)

stocksTicker = "AAPL"
multiplier = 1
timespan = "week"
from_date = "2024-01-01"
to_date = str(today_date.strftime('%Y-%m-%d'))

json_data = get(f"https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?apiKey={key}").json()
if json_data["status"] is not "ERROR":
    st.write(json_data["status"])
else:
    st.write("Error Occured")



