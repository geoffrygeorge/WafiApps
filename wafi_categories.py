import streamlit as st
import pandas as pd
# import numpy as np

# INITIAL PAGE LAYOUT SETTINGS
st.set_page_config(
        page_title = "WafiApps Categories",
        initial_sidebar_state = "auto",
        layout = "centered"
        )

st.markdown("""

<style>
.big-font {
    text-align: center;
    padding-top: 5px;
    font-size: calc(0.65em + 5vmin);
    font-family: Arial, sans-serif;
}
</style>
""", unsafe_allow_html = True)


st.markdown('<p class="big-font">WAFIAPPS CATEGORY VIEWER</p>', unsafe_allow_html = True)


main = st.sidebar.radio('CHOOSE MAIN CATEGORY :', ['Supermarket', 'Watches', 'Appliances', 'Kitchen & Dining', 'Health & Beauty', 'Electronics', 'Computers & IT', 'Tools & DIY', 'Office Supplies', 'Mobiles & Tablets', 'Toys & Games', 'Perfumes & Fragrances', 'Fashion', 'Luggage & Travel Gear', 'Pharmacy', 'Baby Care', 'Cakes & Flowers', 'Home Decor & Furnishing', 'Musical Instruments', 'Gaming & Consoles', 'Diet & Nutrition', 'Furniture & Storage', 'Automotive', 'Home Improvement & Lighting', 'School Essential', 'Telecom', 'Pet Supplies'])

st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)


# function to display root categories text
def root_cat_text():
    st.markdown("""

    <style>
    .small-font {
        text-align: center;
        font-size: 20px;
        font-family: Arial, sans-serif;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html = True)


    st.markdown('<p class="small-font">ROOT CATEGORIES</p>', unsafe_allow_html = True)



if main == 'Supermarket': ######

    sub = st.radio('CHOOSE SUB CATEGORY :', ['Frozen Items', 'Beverages', 'Dairy & Eggs', 'Tea & Coffee', 'Cooking Ingredients', 'Organic', 'Tins Jars & Packets', 'Fresh Fruits & Vegetables', 'Chocolate & Confectionery','Fish & Meat', 'Rice Pasta & Pulses', 'Nuts Dates & Dried Fruits', 'Biscuits Crackers & Cakes', 'Chips Dips & Snacks', 'Breakfast Cereals', 'Condiments-Dressings & Marinades', 'Bakery', 'Household Cleaners', 'Jams Honey & Spreads', 'Salt & Sugar', 'Laundry', 'Home Baking & Desserts', 'Disposable Kitchenware', 'Tissues & Toilet Paper', 'Air Fresheners & Deodorizers', 'Shoe Care & Polish', 'Dishwashing Supplies', 'Papers Foils & Wraps', 'Protein', 'Barbecue', 'Insecticides'])



    if sub == 'Frozen Items': ######

        root_cat = ['Frozen Chicken', 'Snacks & Meals', 'Ice Cream', 'Patties & Burger', 'Fries', 'Frozen Vegetables', 'Frozen Meat', 'Sausages', 'Frozen Fish & Seafood', 'Frozen Pizza', 'Chilled Desserts', 'Frozen Fruits']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Beverages': ######

        root_cat = ['Juices', 'Soft Drinks', 'Bottled Water', 'Energy Drinks', 'Chocolate & Malted Drinks', 'Cordials & Syrups', 'Herbal Water']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Dairy & Eggs': ######
        root_cat = ['Cheese & Labneh', 'Milk & Milk Products', 'Laban', 'Butter & Margarine', 'Egg', 'Yoghurt & Cream']
        
        root_cat_text()

        for i in range(len(root_cat)):
            if root_cat[i] == 'Milk & Milk Products':
                with st.expander('Milk & Milk Products'):
                    st.write('Fresh Milk')
                    st.write('Almond Milk')
                    st.write('Flavored Milk')
                    st.write('Flavoured Milk')
                    st.write('Soya Milk')
            else:
                st.write(root_cat[i])



    if sub == 'Tea & Coffee': ######

        root_cat = ['Coffee', 'Tea', 'Coffee & Drinks']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Cooking Ingredients': ######

        root_cat = ['Oil & Ghee', 'Herbs Spices & Seasoning', 'Cooking Sauce & Paste', 'Gravy & Stock', 'Bread Crumbs']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Organic': ######

        root_cat = ['Whole Grains & Beans', 'Cooking & Baking', 'Oils & Vinegar', 'Spices & Powders', 'Tea Coffee & Drinks']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Tins Jars & Packets': ######

        root_cat = ['Soup & Instant Noodles', 'Canned Vegetables', 'Tuna & Seafood', 'Canned Fruits', 'Powdered Milk', 'Pickles & Olives', 'Coconut Milk & Cream', 'Canned Milk', 'Canned Vegetable']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Fresh Fruits & Vegetables': ######

        root_cat = ['Fresh Fruits', 'Fresh Vegetables']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Chocolate & Confectionery': ######

        root_cat = ['Chocolates', 'Indian Sweets & Snacks', 'Candy', 'Gums & Mints', 'Chocolate']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Fish & Meat': ######

        root_cat = ['Mutton & Lamb', 'Fish & Seafood', 'Beef', 'Chicken']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Rice Pasta & Pulses': ######

        root_cat = ['Rice', 'Flour', 'Pasta', 'Noodles', 'Pulses & Grams', 'Couscous']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])


  
    if sub == 'Nuts Dates & Dried Fruits': ######

        root_cat = ['Dates', 'Nuts & Seeds', 'Dried Fruits']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])


    
    if sub == 'Biscuits Crackers & Cakes': ######

        root_cat = ['Crackers & Crispbread', 'Digestives & Assorted Biscuits', 'Coated Biscuits & Wafers', 'Filled Biscuits', 'Cakes Cupcakes & Muffins', 'Rusk']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Chips Dips & Snacks': ######

        root_cat = ['Chips', 'Canister & Puffs', 'Tortilla & Nacho', 'Pop Corn']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Breakfast Cereals': ######

        root_cat = ['Cereals & Bars', 'Oats', 'Granola & Bars']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Condiments-Dressings & Marinades': ######

        root_cat = ['Sauces & Condiments', 'Salad Dressings & Vinaigrettes']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Bakery': ######

        root_cat = ['Sweets & Pastries', 'Croissant', 'Bread & Rolls', 'Wraps Pittas Naan & Thins', 'Cookies & Muffin', 'Pastries']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Household Cleaners': ######

        root_cat = ['Scrubs & Sponges', 'Mops & Bucket Sets', 'Bathroom Cleaners & Fresheners', 'Bleach & Disinfectants', 'Cleaning Gloves', 'Kitchen Cleaner', 'Kitchen Cloth & Cleaning Wipes', 'Multipurpose Cleaner', 'Sink & Drain Unblocker', 'Wood & Metal Polish', 'Window Cleaners']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Jams Honey & Spreads': ######

        root_cat = ['Spreadables', 'Honey', 'Jam']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Salt & Sugar': ######

        root_cat = ['Sugar', 'Sweeteners', 'Salt']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Laundry': ######

        root_cat = ['Washing Powder', 'Washing Liquid & Gel', 'Stain Remover & Color Care']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Home Baking & Desserts': ######

        root_cat = ['Baking Ingredients', 'Desserts', 'Flour & Bread Mixes']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Disposable Kitchenware': ######

        root_cat = ['Bin Liners & Garbage Bags', 'Disposable Bowl & Tray', 'Disposable Cups & Glasses', 'Disposable Cutlery']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Tissues & Toilet Paper': ######

        root_cat = ['Facial Tissues', 'Maxi Roll & Kitchen Roll', 'Toilet Paper']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Air Fresheners & Deodorizers': ######

        root_cat = ['Aerosols & Room Sprays', 'Car Air Freshener', 'Gels & Blocks Air Freshener']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Shoe Care & Polish': ######

        root_cat = ['Shoe Cleaners', 'Shoe Polish']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Dishwashing Supplies': ######

        root_cat = ['Dishwashing Liquid', 'Dishwashing Powder & Paste']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Papers Foils & Wraps': ######

        root_cat = ['Cling Film', 'Kitchen Aluminium Foil']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Protein': ######

        root_cat = ['Protein Drinks']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Barbecue': ######

        root_cat = ['Box Matches']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Insecticides': ######

        root_cat = ['Insect Killer']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



if main == 'Watches': ######

    sub = st.radio('CHOOSE SUB CATEGORY :', ['Mens Wrist Watch', 'Womens Wrist Watch', 'Boys Watches', 'Girls Watches'])

    if sub == 'Mens Wrist Watch' or sub == 'Womens Wrist Watch' or sub == 'Boys Watches' or sub == 'Girls Watches': ######

        st.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



if main == 'Appliances': ######

    sub = st.radio('CHOOSE SUB CATEGORY :', ['Kitchen Appliances', 'Home Appliances', 'Washing Machines & Dryers', 'Cooktops & Ranges', 'Refrigerators & Freezers', 'Microwave Ovens', 'Air Conditioners', 'Heating Cooling & Air Quality'])


    if sub == 'Kitchen Appliances': ######

        root_cat = ['Coffee Machines & Grinders', 'Hand Blenders & Mixers', 'Electric Kettles', 'Fryers', 'Juicers', 'Rice Cookers', 'Food Processors', 'Toasters', 'Oven & Toaster Grills', 'Mixer Grinders', 'Induction Cooktops', 'Snack Maker', 'Sandwich Makers', 'Bread Maker', 'Electric Steamers', 'Microwave Ovens', 'Meat Grinders & Mincers', 'Choppers & Chippers', 'Milk Frothers', 'Waffle & Dessert Makers']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Home Appliances': ######

        root_cat = ['Irons & Steamers', 'Vacuum Cleaners', 'Water Dispensers & Purifiers', 'Dishwashers']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Washing Machines & Dryers': ######

        root_cat = ['Dryers', 'Fully Automatic Front Load', 'Semi Automatic Top Load', 'Fully Automatic Top Load']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Cooktops & Ranges': ######

        root_cat = ['Cooking Range', 'Cooktop', 'Cooker Hood']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Refrigerators & Freezers': ######

        root_cat = ['Single Door', 'Chest Freezer & Chiller', 'Double Door', 'Side by Side']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Microwave Ovens': ######

        root_cat = ['Solo', 'Grill']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Air Conditioners': ######

        root_cat = ['Split ACs', 'Window ACs']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])



    if sub == 'Heating Cooling & Air Quality': ######

        root_cat = ['Air Purifiers', 'Fans', 'Humidifiers', 'Air Coolers']

        root_cat_text()

        for i in range(len(root_cat)):
            st.write(root_cat[i])