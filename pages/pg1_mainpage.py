import streamlit as st
from requests import get


key =  st.secrets["API_KEY"]

st.title("Hello")

st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

json_data = get(
    f"https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from_date
}/{to_date}?apiKey={key}").json()
st.write(json_data)
