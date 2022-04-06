import streamlit as st
import time


def supermarket_main():

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

    sub = col1.radio('Choose Sub Category :', ['Frozen Items', 'Beverages', 'Dairy & Eggs', 'Tea & Coffee', 'Cooking Ingredients', 'Organic', 'Tins Jars & Packets', 'Fresh Fruits & Vegetables', 'Chocolate & Confectionery','Fish & Meat', 'Rice Pasta & Pulses', 'Nuts Dates & Dried Fruits', 'Biscuits Crackers & Cakes', 'Chips Dips & Snacks', 'Breakfast Cereals', 'Condiments-Dressings & Marinades', 'Bakery', 'Household Cleaners', 'Jams Honey & Spreads', 'Salt & Sugar', 'Laundry', 'Home Baking & Desserts', 'Disposable Kitchenware', 'Tissues & Toilet Paper', 'Air Fresheners & Deodorizers', 'Shoe Care & Polish', 'Dishwashing Supplies', 'Papers Foils & Wraps', 'Barbecue', 'Insecticides'])



    if sub == 'Frozen Items': ######

        root_cat = ['Frozen Chicken', 'Snacks & Meals', 'Ice Cream', 'Patties & Burger', 'Fries', 'Frozen Vegetables', 'Frozen Meat', 'Sausages', 'Frozen Fish & Seafood', 'Frozen Pizza', 'Chilled Desserts', 'Frozen Fruits']

        root_cat_text()
        
        for i in range(len(root_cat)):
            
            col4.write(root_cat[i])



    if sub == 'Beverages': ######

        root_cat = ['Juices', 'Soft Drinks', 'Bottled Water', 'Energy Drinks', 'Chocolate & Malted Drinks', 'Cordials & Syrups', 'Herbal Water']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dairy & Eggs': ######
        root_cat = ['Cheese & Labneh', 'Milk & Milk Products', 'Laban', 'Butter & Margarine', 'Egg', 'Yoghurt & Cream']
        
        root_cat_text()

        for i in range(len(root_cat)):
            if root_cat[i] == 'Milk & Milk Products':
                with col4.expander('Milk & Milk Products'):
                    st.write('Fresh Milk')
                    st.write('Almond Milk')
                    st.write('Flavored Milk')
                    st.write('Flavoured Milk')
                    st.write('Soya Milk')
            else:
                col4.write(root_cat[i])



    if sub == 'Tea & Coffee': ######

        root_cat = ['Coffee', 'Tea', 'Coffee & Drinks']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cooking Ingredients': ######

        root_cat = ['Oil & Ghee', 'Herbs Spices & Seasoning', 'Cooking Sauce & Paste', 'Gravy & Stock', 'Bread Crumbs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Organic': ######

        root_cat = ['Whole Grains & Beans', 'Cooking & Baking', 'Oils & Vinegar', 'Spices & Powders', 'Tea Coffee & Drinks', 'Snacks & Crackers', 'Jams & Spread', 'Breakfast & Cereals', 'Dry Fruit & Seeds', 'Protein Bars', 'Fresh Dairy']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tins Jars & Packets': ######

        root_cat = ['Soup & Instant Noodles', 'Canned Vegetables', 'Tuna & Seafood', 'Canned Fruits', 'Powdered Milk', 'Pickles & Olives', 'Coconut Milk & Cream', 'Canned Milk', 'Canned Vegetable', 'Canned Food', 'Canned Meat']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Fresh Fruits & Vegetables': ######

        root_cat = ['Fresh Fruits', 'Fresh Vegetables', 'Herbs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Chocolate & Confectionery': ######

        root_cat = ['Chocolates', 'Indian Sweets & Snacks', 'Candy', 'Gums & Mints', 'Chocolate', 'Seasonal']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Fish & Meat': ######

        root_cat = ['Mutton & Lamb', 'Fish & Seafood', 'Beef', 'Chicken']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Rice Pasta & Pulses': ######

        root_cat = ['Rice', 'Flour', 'Pasta', 'Noodles', 'Pulses & Grams', 'Couscous']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Nuts Dates & Dried Fruits': ######

        root_cat = ['Dates', 'Nuts & Seeds', 'Dried Fruits']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])


    
    if sub == 'Biscuits Crackers & Cakes': ######

        root_cat = ['Crackers & Crispbread', 'Digestives & Assorted Biscuits', 'Coated Biscuits & Wafers', 'Filled Biscuits', 'Cakes Cupcakes & Muffins', 'Rusk']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Chips Dips & Snacks': ######

        root_cat = ['Chips', 'Canister & Puffs', 'Tortilla & Nacho', 'Pop Corn']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Breakfast Cereals': ######

        root_cat = ['Cereals & Bars', 'Oats', 'Granola & Bars', 'Muesli']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Condiments-Dressings & Marinades': ######

        root_cat = ['Sauces & Condiments', 'Salad Dressings & Vinaigrettes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bakery': ######

        root_cat = ['Sweets & Pastries', 'Croissant', 'Bread & Rolls', 'Wraps Pittas Naan & Thins', 'Cookies & Muffin', 'Pastries', 'Tea Cake & Fruit Loaves']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Household Cleaners': ######

        root_cat = ['Scrubs & Sponges', 'Mops & Bucket Sets', 'Bathroom Cleaners & Fresheners', 'Bleach & Disinfectants', 'Cleaning Gloves', 'Kitchen Cleaner', 'Kitchen Cloth & Cleaning Wipes', 'Multipurpose Cleaner', 'Sink & Drain Unblocker', 'Wood & Metal Polish', 'Window Cleaners', 'Sweeping Parts & Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Jams Honey & Spreads': ######

        root_cat = ['Spreadables', 'Honey', 'Jam']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Salt & Sugar': ######

        root_cat = ['Sugar', 'Sweeteners', 'Salt']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Laundry': ######

        root_cat = ['Washing Powder', 'Washing Liquid & Gel', 'Stain Remover & Color Care', 'Fabric Conditioner', 'Ironing Spray & Board Cover', 'Peg & Cloth Care', 'Sewing & Cloth Care']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Home Baking & Desserts': ######

        root_cat = ['Baking Ingredients', 'Desserts', 'Flour & Bread Mixes', 'Color Mixes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Disposable Kitchenware': ######

        root_cat = ['Bin Liners & Garbage Bags', 'Disposable Bowl & Tray', 'Disposable Cups & Glasses', 'Disposable Cutlery', 'Disposable Plates', 'Disposable Straws & Stirrer', 'Disposable Table Mats & Covers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tissues & Toilet Paper': ######

        root_cat = ['Facial Tissues', 'Maxi Roll & Kitchen Roll', 'Toilet Paper', 'Hand Paper Towel', 'Pocket Tissue', 'Paper Napkin']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Air Fresheners & Deodorizers': ######

        root_cat = ['Aerosols & Room Sprays', 'Car Air Freshener', 'Gels & Blocks Air Freshener', 'Automatic Units & Refills', 'Scented Candles', 'Fabric Refreshers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Shoe Care & Polish': ######

        root_cat = ['Shoe Cleaners', 'Shoe Polish']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dishwashing Supplies': ######

        root_cat = ['Dishwashing Liquid', 'Dishwashing Powder & Paste', 'Dishwasher Tablet & Gel']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Papers Foils & Wraps': ######

        root_cat = ['Cling Film', 'Kitchen Aluminium Foil', 'Cooking & Baking Paper', 'Aluminium Foil Food Container']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Barbecue': ######

        root_cat = ['Box Matches']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Insecticides': ######

        root_cat = ['Insect Killer']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])