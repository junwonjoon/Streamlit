import streamlit as st
from requests import get
import datetime


st.title("Welcome to the stock price displayer")
dict_stocksTicker ={"Apple Inc.": "AAPL",
                    "Microsoft Corporation": "MSFT",
                    "Amazon.com, Inc.": "AMZN",
                    "Google LLC": "GOOGL",
                    "Facebook, Inc.": "FB",
                    "Tesla, Inc.": "TSLA",
                    "Berkshire Hathaway Inc.": "BRK.A",
                    "Johnson & Johnson": "JNJ",
                    "Walmart Inc.": "WMT",
                     "Visa Inc.": "V"}

key = st.secrets["API_KEY"]
today_date = datetime.datetime.now()
genre = st.radio(
    "What stock price do you want to see?",
    [key for key in dict_stocksTicker.keys()])

start_date = st.date_input("When should be the start date?", datetime.date(2019, 7, 6))
st.write("The start date is", start_date)
end_date = st.date_input("When should be the end date?", datetime.datetime.now())
st.write("The end date is", end_date)

st.write("You selected:", genre)
if st.button("Continue", type="primary"):
    stocksTicker = dict_stocksTicker[genre]
    multiplier = 1
    timespan = "week"
    from_date = "2024-01-01"
    to_date = str(today_date.strftime('%Y-%m-%d'))

    json_data = get(f"https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?apiKey={key}").json()
    if json_data["status"] is not "ERROR":
        st.write(json_data)
    else:
        st.write("Error Occured")



