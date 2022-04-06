import streamlit as st
import time


def telecom_main():

    # defining columns for structure
    col1, col2, col3, col4 = st.columns([7.2,1,1,5])

    col2.empty()
    col3.empty()

    def root_cat_text():

        col4.subheader('ROOT CATEGORIES')

        with col4:

            with st.spinner(text = "Please Wait"):

                time.sleep(0.5)

    col1.subheader('SUB CATEGORIES')

    sub = col1.radio('Choose Sub Category :', ['Batelco'])



    if sub == 'Batelco': ######

        root_cat = ['Mobile & Data', 'Home Broadband', 'Postpaid Plans', 'Mobile Broadband']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])