import streamlit as st
import time


def tools_diy_main():

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

    sub = col1.radio('Choose Sub Category :', ['Hand Tools', 'Power Tools', 'Safety & Security', 'Professional Cleaning Products', 'Garden Tools', 'Hardware', 'Painting Supplies & Wall Treatment', 'Power Solutions'])



    if sub == 'Hand Tools': ######

        root_cat = ['Tool Sets', 'Screw Drivers', 'Measure & Layout Tools', 'Multi Tools', 'Pliers', 'Hammers', 'Tool Boxes', 'Cutting Tools', 'Chisels', 'Wrenchs', 'Saws', 'Ratchets & Sockets', 'Crimping Tools', 'Clamp & Vizes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])


        
    if sub == 'Power Tools': ######

        root_cat = ['Tool Sets', 'Sawing Tools', 'Jig Saws & Blades', 'Cordless Drill', 'Drilling', 'Sanding Tools', 'Planers', 'Cutting Tools', 'Pneumatic Tools', 'Routers', 'Staplers', 'Saws', 'Grinding Tools', 'Rotary Hammers', 'Heatguns', 'Nibblers', 'Shears', 'Distance Measurer', 'Demolition Tools']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Safety & Security': ######

        root_cat = ['Eye Protection', 'Safety Shoes', 'Head Protection', 'Hand & Arm Protection', 'Ear Protection', 'Masks & Respirators', 'Traffic Cones', 'Doctor/Lab Coats', 'Fall Protection']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Professional Cleaning Products': ######

        root_cat = ['Pressure Washers', 'Pro Vacuum Cleaners', 'Air Blowers', 'Steam Cleaners', 'Floor Polishers', 'Electric Brooms']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Garden Tools': ######

        root_cat = ['Lawn Movers', 'Hoses', 'Nozzles', 'Sprinklers', 'Hand Tools', 'Hedge Trimmers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Hardware': ######

        root_cat = ['Adhesives & Sealers', 'Nails Screws & Fasteners', 'Bathroom Hardware', 'Cabinet Hardware', 'Furniture Hardware', 'Door Hardware & Locks', 'Tarps & Tie-Downs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Painting Supplies & Wall Treatment': ######

        root_cat = ['Paint Sprayers', 'Polishers', 'Paint & Primer', 'Wall Stickers', 'Wallpaper & Supplies', 'Finishes Sealers & Stains']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Power Solutions': ######

        root_cat = ['Power Detectors', 'Cable Reels', 'Portable Generators']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])