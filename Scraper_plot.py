# imports
import streamlit as st
import pandas as pd
import plotly.express as px
import csv

# Streamlit and pandas to write display various headers and information texts
st.set_page_config(page_title="Verge.com-Plots")
st.title("12th Septemper 2022, Verge.com-Plots 📈")

container = st.container()
container.write("Page information: This analysis project of Verge.com is based on their old site till 12th September, 2022. They have changed their format after that.")
container.write("Analysis Report: Shows that they are creating and updating lot of good technology articles on products from major brands, especially Apple products. They have updated team of technology content authors.")
st.write("You can see 1 chart with Article ids, Article links, Article headlines, Article Authors, Article Dates.")
st.subheader("Choose one csv file to upload")

uploaded_file = st.file_uploader('Choose a CSV file', type=['csv'])
if uploaded_file:
    st.markdown("----")
    df2 = pd.read_csv(uploaded_file)
    st.dataframe(df2)

# copyright information and social media links as footer display using streamlit and pandas
st.write("Social Media & Support Link:")
st.write("https://www.theverge.com/")

#----End of Scraper_plot.py file----------------------------------------------------------------
# Coder: Swati Mishra
