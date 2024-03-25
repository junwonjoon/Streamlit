import streamlit as st
from requests import get
import datetime


st.title("Stock Price!")
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
genre = st.radio(
    "What stock price do you want to see?",
    [key for key in dict_stocksTicker.keys()])

start_date_select = st.date_input("When should be the start date?", datetime.date(2024, 1, 1))
st.write("The start date is", start_date_select)

end_date_select = st.date_input("When should be the end date?", datetime.datetime.now() - datetime.timedelta(days=1))
st.write("The end date is", end_date_select)

timespan_select = st.select_slider(
    'Select the timespan',
    options=['second', 'minute', 'hour', 'day', 'week', 'month', 'quarter', 'year'],
    value=('day'))
st.write('You selected timespan as ', timespan_select)


timespan_multiplier_select = st.number_input('Enter the timespan multiplier', 1, step = 1)
st.write('Timespan multiplier is:', timespan_multiplier_select)

if st.button("Continue", type="primary"):
    stocksTicker = dict_stocksTicker[genre]
    multiplier = 1
    timespan = timespan_select
    from_date = start_date_select
    to_date = end_date_select

    json_data = get(f"https://api.polygon.io/v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?apiKey={key}").json()
    if json_data["status"] is "ERROR":
        st.write("Too many request were created, maximum request is 5 per minute, try again a minute later")
    elif json_data["status"] is "NOT_AUTHORIZED":
        st.write("Sorry this feature is not availiable to use")
    else:
        st.write(json_data)




