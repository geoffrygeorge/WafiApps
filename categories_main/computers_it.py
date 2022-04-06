import streamlit as st
import time


def computers_it_main():

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

    sub = col1.radio('Choose Sub Category :', ['Computer Cables & Connectors', 'Networking Devices', 'Mouses & Keyboards', 'Laptops', 'Desktops', 'Mac', 'Storage Devices', 'Computer AV Accessories', 'Monitors', 'Printers & Scanners', 'Toners & Cartridges', 'Softwares', 'Components & Parts'])



    if sub == 'Computer Cables & Connectors': ######

        root_cat = ['HDMI Cables', 'USB Cables', 'USB Hubs', 'Adapters', 'Ethernet Cables', 'SATA Cables', 'Lightning Cables']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Networking Devices': ######

        root_cat = ['Routers', 'Network Adapters']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Mouses & Keyboards': ######

        root_cat = ['Mice', 'Keyboard & Mice Combos', 'Keyboards', 'Mouse Pads & Wrist Rests']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Laptops': ######

        root_cat = ['Laptop', 'Business Laptops', 'MS Surface', 'Gaming Laptops', 'Convertible 2in1']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Desktops': ######

        root_cat = ['Computer Towers', 'All in One PCs', 'iMac', 'Gaming Desktops']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Mac': ######

        root_cat = ['Macbook Air', 'Macbook Pro', 'iMac', 'iMac Pro']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Storage Devices': ######

        root_cat = ['External Data Storage', 'Internal Data Storage', 'Flash Drives', 'Network Attached Storage']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Computer AV Accessories': ######

        root_cat = ['Webcams & Voip', 'Computer Headsets', 'Computer Speakers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Monitors': ######

        root_cat = ['Samsung Monitors', 'Dell Monitors', 'HP Monitors', 'Monitor Accessories', 'Projectors', 'LG Monitors', 'BenQ Monitors', 'Viewsonic Monitors', 'MSI Monitors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Printers & Scanners': ######

        root_cat = ['Ink Tank Printers', 'Inkjet Printers', 'Laser Printers', 'Photo Printers', 'Thermal Printers', 'Sacnners']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Toners & Cartridges': ######

        root_cat = ['Ink Cartridges', 'Ink Bottles', 'Toners', 'Compatible Catridges']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Softwares': ######

        root_cat = ['Operating Systems', 'Antivirus & Security', 'Business & Office']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Components & Parts': ######

        root_cat = ['External Components', 'Internal Components']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])