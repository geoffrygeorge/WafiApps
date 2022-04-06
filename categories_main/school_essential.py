import streamlit as st
import time


def school_essential_main():

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

    sub = col1.radio('Choose Sub Category :', ['Backpack & Storages', 'Calculator', 'Writing Instruments', 'Cutting & Measuring', 'Art & Crafts'])



    if sub == 'Backpack & Storages': ######

        root_cat = ['School Backpack', 'Pencil Case & Pouch', 'Lunch Box & Bag']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Calculator': ######

        root_cat = ['Scientific Calculator', 'Basic Calculator', 'Graphing Calculator']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Writing Instruments': ######

        root_cat = ['Ballpoint Pen', 'Gel Pen', 'Fountain Pen', 'Markers', 'Highlighters', 'Mechanical Pencil', 'Wooden Pencil', 'Sharpener', 'Eraser']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cutting & Measuring': ######

        root_cat = ['Mathematical Instruments', 'Rulers & Protractors', 'Scissors', 'Paper Trimmers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Art & Crafts': ######

        root_cat = ['Colored Pencil & Sketch Pens', 'Crayons', 'Paint & Paint Brushes', 'Glue Sticks', 'Art Paper & Books', 'Canvas & Art Boards', 'Colored Paper & Cardboard', 'Clay & Craft Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])