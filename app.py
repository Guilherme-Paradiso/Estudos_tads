import streamlit as st
from ds.plot import plot_price

st.title('Stock Price History')
st.write('View the quotation history of companies.')

ticker = st.sidebar.text_input(
    'Choose the ticker:',
    value = 'AAPL'
    )
fig = plot_price(ticker)
st.plotly_chart(fig)