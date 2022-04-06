import streamlit as st
import time


def perfumes_fragrances_main():

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

    sub = col1.radio('Choose Sub Category :', ["Arabic Perfumes", "Men's Perfume", "Women's Perfume", "Unisex Perfumes", "Fragrance Sets"])



    if sub == "Arabic Perfumes": ######

        root_cat = ["Unisex Arabic Perfumes", "Women's Eau de Parfum", "Men's Eau de Parfum", "Oudh", "Perfume Oils", "Bakhoor", "Athar"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Men's Perfume": ######

        root_cat = ["Eau de Toilette", "Eau de Parfum", "Eau de Cologne", "Aftershaves"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Women's Perfume": ######

        root_cat = ["Eau de Parfum", "Eau de Toilette", "Eau de Cologne", "Perfume Oils"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Unisex Perfumes": ######

        root_cat = ["Eau de Parfum", "Eau de Toilette", "Eau de Cologne", "Perfume Oils"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Fragrance Sets": ######

        root_cat = ["Women Fragrance Gift Set", "Men Fragrance Gift Set"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])