import streamlit as st
from requests import get
import datetime
import pandas as pd
import plotly.express as px
import json

key = st.secrets["API_KEY"]
st.title("Hello")
today_date = datetime.datetime.now()

stocksTicker = "AAPL"
multiplier = 1
timespan = "week"
from_date = "2024-01-01"
to_date = str(today_date.strftime('%Y-%m-%d'))

json_data = get(f"https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?apiKey={key}").json()
st.write(json_data)

df = pd.DataFrame(json_data['results'])

# Convert timestamps to readable dates
df['date'] = pd.to_datetime(df['t'], unit='ms')

# Plot using Plotly
fig = px.line(df, x='date', y='c', title=f"Closing Prices Over Time for {json_data['ticker']}")

# Display the chart in Streamlit
st.plotly_chart(fig)