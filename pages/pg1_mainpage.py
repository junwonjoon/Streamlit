import streamlit as st
from requests import get


# secret_value = os.getenv('MY_SECRET')

# print(secret_value)
key =  st.secrets["API_KEY"]

st.title("Hello")

forecast = get(
    f"https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey={key}").json()

# Hello'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=c4NLm5QgWNWDBWp530A_Ypnxc6PHmmtD
# aggs = []
# for a in client.list_aggs(
#     "AAPL",
#     1,
#     "minute",
#     "2022-01-01",
#     "2023-02-03",
#     limit=50000,
# ):
#     aggs.append(a)

# print(aggs)