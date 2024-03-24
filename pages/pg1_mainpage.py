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

# Preparing the data for visualization
# dates = [datetime.fromtimestamp(item["t"] / 1000).date() for item in json_data["results"]]
# closing_prices = [item["c"] for item in json_data["results"]]
# # Creating a dictionary for Streamlit chart
# chart_data = {'Date': dates, 'Closing Price': closing_prices}

# # Converting dictionary to Streamlit compatible format (columns with same length)
# df_for_chart = st.dataframe(chart_data)

# # Displaying the line chart in Streamlit
# st.line_chart(df_for_chart)