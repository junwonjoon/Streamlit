import streamlit as st
from pages.page1 import page1
from pages.page2 import page2
from pages.page3 import page3

st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Page 1', 'Page 2', 'Page 3'])
pages = {
    'Page 1': page1,
    'Page 2': page2,
    'Page 3': page3,
}
if page:
    pages[page]()
