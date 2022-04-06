import streamlit as st
import time


def office_supplies_main():

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

    sub = col1.radio('Choose Sub Category :', ['Office Pantry', 'Office Cleaning', 'Office Basics', 'Paper', 'Desk Organizers & Accessories', 'Shredder & Office Machines', 'Writing Pads & Notebook', 'Writing Supplies', 'Folders & Filing', 'Tape & Adhesives', 'Boards & Easels', 'Stamp & Embossers', 'Time Card Label & Label Makers', 'Paper Rolls', 'Planners & Calendars'])



    if sub in ('Office Pantry', 'Office Cleaning'): ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



    if sub == 'Office Basics': ######

        root_cat = ['Battery', 'Scissors', 'Staplers & Staples', 'Paper & Binder Clips', 'Punches', 'Envelopes', 'Ruler', 'Rubber Band', 'Clipboards', 'Safety Signs & Stickers', 'Name Badges & Lanyards', 'Key Box & Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Paper': ######

        root_cat = ['Copy Paper', 'Other Paper', 'Color Paper']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Desk Organizers & Accessories': ######

        root_cat = ['Desk Organizers', 'Business Card Organizers', 'Magazine Rack']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Shredder & Office Machines': ######

        root_cat = ['Laminator', 'Calculator', 'Paper Trimmer & Cutter', 'Shredder', 'Price Labeller', 'Binders & Binder Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Writing Pads & Notebook': ######

        root_cat = ['Sticky Notes', 'Writing Pads', 'Note Cards', 'Executive Notebook', 'Wirebound Notebook', 'Legal Pads', 'Accounting Books', 'Diaries & Journals']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Writing Supplies': ######

        root_cat = ['Pen', 'Pencil', 'Correction Pen & Fluid', 'Markers & Highlighters', 'Sharpener', 'Eraser']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Folders & Filing': ######

        root_cat = ['Lever Arch & Box Files', 'Square Cut Folder', 'L Shape Folder', 'Index Dividers', 'Hanging & Expanding Files', 'Ring Binder & View Binder', 'Report File', 'Display Book']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tape & Adhesives': ######

        root_cat = ['Transparent Tape', 'Masking Tape', 'Packing Tape', 'Duct Tape', 'Speciality Tape', 'Decorative Fashion Tape', 'Tape Dispenser', 'Glue Sticks & Pen', 'Adhesives & Removers', 'Hooks & Hanging Strips']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Boards & Easels': ######

        root_cat = ['Whiteboard', 'Bulletin Board', 'Easel & Easel Pad', 'Board Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Stamp & Embossers': ######

        root_cat = ['Stamp Pad & Ink', 'Rubber Stamp']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Time Card Label & Label Makers': ######

        root_cat = ['Address Label', 'Barcode Label', 'Shipping Label', 'Label Maker', 'Label Tape', 'Time Card']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Paper Rolls': ######

        root_cat = ['Thermal Rolls', 'Plotter Rolls', 'Cash Rolls']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Planners & Calendars': ######

        root_cat = ['Daily Planner', 'Weekly Planner', 'Monthly Planner']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])