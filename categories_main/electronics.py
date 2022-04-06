import streamlit as st
import time


def electronics_main():

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

    sub = col1.radio('Choose Sub Category :', ['Personal Care for Women', 'Headphones & Earphones', 'Personal Care for Men', 'Speakers', 'Wearable Technology', 'Cameras & Accessories', 'Health Care Appliances', 'Smart Home & Office', 'Televisions', 'Telephones', 'Audio & Video'])



    if sub == 'Personal Care for Women': ######

        root_cat = ['Epilators', 'Hair Straightener', 'Hair Curlers & Stylers', 'Hair Dryer', 'Sauna & Spa']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Headphones & Earphones': ######

        root_cat = ['Earphones', 'Headphones', 'Headsets with Mic']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Personal Care for Men': ######

        root_cat = ['Trimmers & Clippers', 'Electric Shavers', 'Grooming Kit']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Speakers': ######

        root_cat = ['Bluetooth Speakers', 'Portable Speakers & Docks', 'Sound Bars', 'Subwoofers', 'Smart Speakers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Wearable Technology': ######

        root_cat = ['Smart Watch', 'Activity Trackers', 'Arm & Wristbands', 'Apple Watch', 'Clips', 'VR Headsets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cameras & Accessories': ######

        root_cat = ['Instant Film Cameras', 'Lenses & Accessories', 'DSLR Cameras', 'Action Cameras', 'Digital Cameras', 'Camcorders']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Health Care Appliances': ######

        root_cat = ['Health Massagers', 'Weighing Scales', 'BP Monitors', 'Nebulizers Inhalers & Masks', 'Oral Care']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Smart Home & Office': ######

        root_cat = ['CCTV Cameras & Accessories', 'Intercom Systems', 'Smart Lighting', 'Baby Monitors', 'Safety Lockers', 'Batteries & Chargers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Televisions': ######

        root_cat = ['Smart TV', 'Ultra HD TV', 'QLED TV', 'LED TV', 'Full HD TV', 'Cables & Accessories', 'OLED TV']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Telephones': ######

        root_cat = ['Landphones', 'Telephone Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Audio & Video': ######

        root_cat = ['Audio & Video Accessories', 'Projectors', 'Hi-Fi & Home Audio', 'Home Theatre Systems', 'Set-Top Boxes', 'DVD Players & Recorders', 'Media Streaming Devices']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])