import streamlit as st
from requests import get
import datetime

key = st.secrets["API_KEY"]
# key_temp = 'c4NLm5QgWNWDBWp530A_Ypnxc6PHmmtD'
st.title("Hello")
today_date = datetime.datetime.now()

stocksTicker = "AAPL"
multiplier = 1
timespan = "week"
from_date = "2024-01-01"
to_date = str(today_date.strftime('%Y-%m-%d'))

json_data = get(f"https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?apiKey={key}").json()
st.write(json_data)

