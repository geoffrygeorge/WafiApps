import streamlit as st
import time


def pharmacy_main():

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

    sub = col1.radio('Choose Sub Category :', ['Braces Splints & Supports', 'Bed Pillows & Positioners', 'Face Mask', 'Pain Relief Medications & Treatments', 'Walkers Rollators & Accessories', 'Home Tests'])



    if sub == 'Braces Splints & Supports': ######

        root_cat = ['Leg & Foot Supports', 'Arm Hand & Finger Supports', 'Back Neck & Shoulder Supports', 'Hip & Waist Supports', 'Athletic Tapes & Wraps', 'Chest Supports', 'Arthritis Gloves', 'Braces', 'Kinesiology Recovery Tapes', 'Compression Socks']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bed Pillows & Positioners': ######

        root_cat = ['Neck & Cervical Pillows', 'Contoured Support Pillows', 'Bed Pillows']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Face Mask': ######

        root_cat = ['Surgical Face Mask', 'Cloth Face Mask']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Pain Relief Medications & Treatments': ######

        root_cat = ['Hot & Cold Therapies']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Walkers Rollators & Accessories': ######

        root_cat = ['Standard Walkers', 'Rolling Walkers', 'Wheelchairs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Home Tests': ######

        root_cat = ['Pregnancy Tests', 'Family Planning Tests']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])