import streamlit as st
import time
from PIL import Image
from streamlit_lottie import st_lottie
import json
import requests
import pandas as pd
# import numpy as np



# INITIAL PAGE LAYOUT SETTINGS
favicon_img = Image.open("images/wafi_favicon.ico")
st.set_page_config(
        page_title = "WafiApps Categories",
        initial_sidebar_state = "auto",
        page_icon = favicon_img,
        layout = "centered"
        )



st.sidebar.title("NAVIGATION")

# defining various pages in the application
main_menu = ['INTRO', 'CATEGORY VIEWER', 'VENDOR LIST']

with st.container():

    menu = st.sidebar.selectbox('Go to', main_menu) 


#### INTRO ####
if menu == "INTRO":

    sidebar_img = Image.open("images/wafi_logo_text.png")

    st.image(sidebar_img, use_column_width = True, output_format = 'PNG')


    if False:
        def intro_lottie(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)


    @st.cache(show_spinner = False)
    def intro_lottie(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None

        return r.json()

    lottie_url = "https://assets3.lottiefiles.com/packages/lf20_57TxAX.json"
    #lottie_local_path = "lottie_files/shopping_lottie.json"
    lottie_sidebar = intro_lottie(lottie_url)
    st_lottie(lottie_sidebar, height = 375, renderer = "svg")




#### CATEGORY VIEWER ####
if menu == "CATEGORY VIEWER":

    st.markdown("""

    <style>
    .big-font {
        text-align: center;
        padding-top: 0.5px;
        font-size: calc(0.70em + 4.5vmin);
        font-family: sans-serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html = True)


    st.markdown('<p class="big-font">WAFIAPPS CATEGORY VIEWER</p>', unsafe_allow_html = True)


    st.sidebar.title('MAIN CATEGORIES')

    main = st.sidebar.radio('Choose Main Category :', ['Supermarket', 'Watches', 'Appliances', 'Kitchen & Dining', 'Health & Beauty', 'Electronics', 'Computers & IT', 'Tools & DIY', 'Office Supplies', 'Mobiles & Tablets', 'Toys & Games', 'Perfumes & Fragrances', 'Fashion', 'Luggage & Travel Gear', 'Pharmacy', 'Baby Care', 'Cakes & Flowers', 'Home Decor & Furnishing', 'Musical Instruments', 'Gaming & Consoles', 'Diet & Nutrition', 'Furniture & Storage', 'Automotive', 'Home Improvement & Lighting', 'School Essential', 'Telecom', 'Pet Supplies'])

    st.markdown('<p></p>', unsafe_allow_html = True)


    # function to display root categories text

    if False:
        def root_cat_text():
            col4.markdown("""

            <style>
            .small-font {
                text-align: left;
                font-size: 20px;
                font-family: sans-serif;
                font-weight: 500;
            }
            </style>
            """, unsafe_allow_html = True)


            col4.markdown('<p class="small-font">ROOT CATEGORIES</p>', unsafe_allow_html = True)

    # defining columns for structure
    col1, col2, col3, col4 = st.columns([7.5,1,1,5])

    # functions
    def root_cat_text():

        col4.subheader('ROOT CATEGORIES')

        with col4:

            with st.spinner(text = "Please Wait"):

                time.sleep(0.5)


    def sub_cat_text():

        col1.subheader('SUB CATEGORIES')


    def root_cat_df(data):
        df = pd.DataFrame(data)
        df.index += 1
        st.table(df)

    # defining categories
    if main == 'Supermarket': ######

        sub_cat_text()

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



    if main == 'Watches': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Mens Wrist Watch', 'Womens Wrist Watch', 'Boys Watches', 'Girls Watches', 'Couple Watches'])

        if sub == 'Mens Wrist Watch' or sub == 'Womens Wrist Watch' or sub == 'Boys Watches' or sub == 'Girls Watches': ######

            col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')

        elif sub == 'Couple Watches': ######

            col4.warning('CURRENTLY, THIS SUB-CATEGORY IS DISABLED & THERE ARE NO ROOT-CATEGORIES')



    if main == 'Appliances': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Kitchen Appliances', 'Home Appliances', 'Washing Machines & Dryers', 'Cooktops & Ranges', 'Refrigerators & Freezers', 'Microwave Ovens', 'Air Conditioners', 'Heating Cooling & Air Quality'])



        if sub == 'Kitchen Appliances': ######

            root_cat = ['Coffee Machines & Grinders', 'Hand Blenders & Mixers', 'Electric Kettles', 'Fryers', 'Juicers', 'Rice Cookers', 'Food Processors', 'Toasters', 'Oven & Toaster Grills', 'Mixer Grinders', 'Induction Cooktops', 'Snack Maker', 'Sandwich Makers', 'Bread Maker', 'Electric Steamers', 'Microwave Ovens', 'Meat Grinders & Mincers', 'Choppers & Chippers', 'Milk Frothers', 'Waffle & Dessert Makers', 'Wet Grinders']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Home Appliances': ######

            root_cat = ['Irons & Steamers', 'Vacuum Cleaners', 'Water Dispensers & Purifiers', 'Dishwashers', 'Sewing Machine & Accessories', 'Inverters']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Washing Machines & Dryers': ######

            root_cat = ['Dryers', 'Fully Automatic Front Load', 'Semi Automatic Top Load', 'Fully Automatic Top Load']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Cooktops & Ranges': ######

            root_cat = ['Cooking Range', 'Cooktop', 'Cooker Hood']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Refrigerators & Freezers': ######

            root_cat = ['Single Door', 'Chest Freezer & Chiller', 'Double Door', 'Side by Side', 'Triple Door']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Microwave Ovens': ######

            root_cat = ['Solo', 'Grill', 'Convection']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Air Conditioners': ######

            root_cat = ['Split ACs', 'Window ACs']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Heating Cooling & Air Quality': ######

            root_cat = ['Air Purifiers', 'Fans', 'Humidifiers', 'Air Coolers', 'Heaters', 'Water Heater']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Kitchen & Dining': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Cookware', 'Kitchen Tools', 'Serveware', 'Bakeware', 'Kitchen Storage & Containers', 'Dinner Sets'])


        if sub == 'Cookware': ######

            root_cat = ['Frying Pans & Saucepans', 'Cookpots & Casseroles', 'Cookware Sets', 'Pressure Cookers', 'Kadhais & Woks', 'Tawas', 'Cooking Spoons', 'Tadka Pans']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Kitchen Tools': ######

            root_cat = ['Knives', 'Utensils & Gadgets', 'Measures & Scales', 'Choppers & Chippers', 'Graters & Slicers', 'Kichen Ladels']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Serveware': ######

            root_cat = ['Hotpots', 'Cups & Mugs', 'Serving Bowls', 'Cutlery', 'Serving Trays', 'Glassware & Drinkware', 'Cookpots & Casseroles']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bakeware': ######

            root_cat = ['Baking Tools', 'Cake & Muffin Moulds', 'Mixing Bowls', 'Decorative Tools', 'Cookie Cutters']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Kitchen Storage & Containers': ######

            root_cat = ['Water Bottles & Flasks', 'Jars & Containers', 'Food Savers', 'Countertop & Wall Organization', 'Lunch Boxes & Bags', 'Cooler', 'Trash & Recycling']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])   



        if sub == 'Dinner Sets': ######

            root_cat = ['Opalware & Glass', 'Plates', 'Bone China & Porcelain', 'Melamine', 'Metalware']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i]) 



    if main == 'Health & Beauty': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Face', 'Facial Skincare', 'Skin Care', 'Lips', 'Eyes', 'Hair Care', 'Bath & Body', 'Oral Hygiene', 'Makeup Tools & Accessories', 'Medicine & Treatment', 'Womens Toiletries', 'Suncare & Travel', 'Nail & Nail Polish', 'Mens Grooming', 'Lifestyle & Wellbeing', 'Hair Styling Accessories'])



        if sub == 'Face': ######

            root_cat = ['Foundation & Contour', 'Concealer & Corrector', 'Primer Makeup', 'Facial Serum', 'Blushes & Bronzers', 'Powder', 'Makeup Sets' , 'BB Cream', 'CC Cream', 'Highlighter & Luminizer', 'Face Makeup Remover', 'Makeup Palettes']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Facial Skincare': ######

            root_cat = ['Face Cream & Moisturizer', 'Cleanser Toner & Face Mask', 'Anti Wrinkle Skin Care', 'Cotton Wool', 'Face Wash & Scrub', 'Face Wipes', 'Lip Balm']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Skin Care': ######

            root_cat = ['Oil & Petroleum Jelly', 'Footcare & Handcare', 'Hand Sanitizers']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])       



        if sub == 'Lips': ######

            root_cat = ['Lipstick', 'Lip Liner', 'Lip Gloss', 'Lip Makup Remover']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])  



        if sub == 'Eyes': ######

            root_cat = ['Eyeliner & Mascara', 'Eye Pencil & Brow Liner', 'Eyelash Treatment', 'Eye Shadow & Eye Makeup Kit', 'Glitter & Shimmer', 'Eye Makeup Remover']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])  



        if sub == 'Hair Care': ######

            root_cat = ['Hair Styling Accessories', 'Hair Treatment Serum & Oil', 'Shampoo', 'Conditioner', 'Hair Colourants', 'Hair Styling Creams & Lotions']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])  



        if sub == 'Bath & Body': ######

            root_cat = ['Body Wash & Shower Gel', 'Bath Accessories', 'Hand Wash & Soap', 'Talcum Powder', 'Body Lotion', 'Bubble Bath Foam & Salts', 'Kids Shower Gel & Handwash']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i]) 



        if sub == 'Oral Hygiene': ######

            root_cat = ['Power Toothbrushes & Accessories', 'Tooth Brush & Floss', 'Toothpaste', 'Mouthwash', 'Kids Oral Care', 'Whitening Oral Care', 'Sensitive Oral Care']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])      


                
        if sub == 'Makeup Tools & Accessories': ######

            root_cat = ['Brush Set', 'Tweezer & Trimmer', 'Makeup Bag']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])   



        if sub == 'Medicine & Treatment': ######

            root_cat = ['First Aid', 'Pain Relief', 'Heartburn & Indigestion', 'Sore Throat & Cough Medicine', 'Eye Care']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])   



        if sub == 'Womens Toiletries': ######

            root_cat = ['Womens Hair Removal', 'Womens Razors & Blades', 'Womens Deodarant & Bodyspray', 'Intimate Wash', 'Sanitary Napkins', 'Tampons & Panty Liners']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])    



        if sub == 'Suncare & Travel': ######

            root_cat = ['Suncare', 'Insect Repellent']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])       



        if sub == 'Nail & Nail Polish': ######

            root_cat = ['Nail Treatment', 'Nail Polish', 'Nail Polish Remover', 'Manicure Kits', 'Nail Tools', 'Top & Base Coat', 'False Nails']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i]) 



        if sub == 'Mens Grooming': ######

            root_cat = ['Mens Deodorants & Antiperspirants', 'Shaving Cream Foams & Gels', 'Mens Razor & Blade', 'Mens Facewash', 'Mens Moisturizer & After Shave', 'Beard Care', 'Mens Skincare', 'Mens Body Wash & Shower Gel', 'Mens Shampoo', 'Mens Hairstyling']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i]) 



        if sub == 'Lifestyle & Wellbeing': ######

            root_cat = ['Condom Lubricants & Gels']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Hair Styling Accessories': ######

            root_cat = ['Hair Spray', 'Cream Gel & Lotion', 'Pomade & Wax', 'Wig & Hair Extension', 'Gloss & Shine', 'Curl Enhancer', 'Volume & Texture', 'Hair Smoothing', 'Heat Protectant']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Electronics': ######

        sub_cat_text()

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



    if main == 'Computers & IT': ######

        sub_cat_text()

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



    if main == 'Tools & DIY': ######

        sub_cat_text()

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



    if main == 'Office Supplies': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Office Pantry', 'Office Cleaning', 'Office Basics', 'Paper', 'Desk Organizers & Accessories', 'Shredder & Office Machines', 'Writing Pads & Notebook', 'Writing Supplies', 'Folders & Filing', 'Tape & Adhesives', 'Boards & Easels', 'Stamp & Embossers', 'Time Card Label & Label Makers', 'Paper Rolls', 'Planners & Calendars'])



        if sub == 'Office Pantry': ######

            col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



        if sub == 'Office Cleaning': ######

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



    if main == 'Mobiles & Tablets': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Mobile Accessories', 'Mobile Phones', 'Tablets & iPad'])



        if sub == 'Mobile Accessories': ######

            root_cat = ['Mobile Cables', 'Mobile Chargers', 'Mobile Cases & Covers', 'Power Banks', 'Mobile Holders', 'Mobile Screen Protectors', 'SD Cards', 'Selfie Stick', 'Bluetooth Devices & Headsets']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Mobile Phones': ######

            root_cat = ['Nokia', 'Samsung', 'Huawei', 'iPhone', 'OnePlus', 'Xiaomi', 'Vivo', 'Alcatel', 'Ravoz', 'Oppo', 'Realme']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Tablets & iPad': ######

            root_cat = ['iPad', 'Samsung', 'Huawei', 'Alcatel', 'Lenovo']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Toys & Games': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Toy Figures & Playsets', 'Dolls & Accessories', 'Games & Accessories', 'Hobbies', 'Sports & Outdoor Play', 'Play Vehicles', 'Dress Up & Pretend Play', 'Learning & Education', 'Stuffed Animals & Plush Toys', 'Puzzles', 'Tricycles & Scooters', 'Arts & Crafts', 'Baby & Toddler Toys', 'Building Toys', 'Party Supplies', 'Kids Electronics', 'Novelty & Gag Toys'])



        if sub == 'Toy Figures & Playsets': ######

            root_cat = ['Action Figures', 'Playsets & Vehicles']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Dolls & Accessories': ######

            root_cat = ['Dolls', 'Doll Accessories', 'Doll House Accessories', 'Playsets', 'Doll Houses']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Games & Accessories': ######

            root_cat = ['Board Games', 'Card Games', 'Floor Games', 'Stacking Games', 'Arcade & Table Games', 'Tile Games', 'Dice Games', 'Handheld Games', 'Game Accessories', 'Marble Games', 'Travel Games', 'Gaming Tops', 'DVD Games', 'Game Collections']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Hobbies': ######

            root_cat = ['Collecting', 'Pre-built Display Models', 'Robotics', 'Model Kits', 'Radio & Remote Control', 'Model Trains', 'Slot Cars', 'Rockets', 'Painting & Surfacing', 'Tools', 'Coins']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Sports & Outdoor Play': ######

            root_cat = ['Blasters & Foam Play', 'Trampoline & Accessories', 'Play Sets & Playground Equipments', 'Bubbles', 'Sandboxes', 'Yo-Yos', 'Pools & Water Toys', 'Sand & Water Tables', 'Play Tents & Tunnels', 'Inflatable Bouncers', 'Ball Pits & Accessories', 'Kites & Wind Spinners', 'Playhouses', 'Toy Sports', 'Flying Toys', 'Gardening Tools', 'Kickball & Playground Balls', 'Pogo Sticks & Hoppers']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Play Vehicles': ######

            root_cat = ['Toy Vehicles', 'Die-Cast Vehicles', 'Vehicle Playsets', 'Play Trains & Railway Sets', 'Pull Back Vehicles']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Dress Up & Pretend Play': ######

            root_cat = ['Pretend Play', 'Beauty & Fashion', 'Costumes', 'Accessories', 'Masks', 'Wigs', 'Hats']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Learning & Education': ######

            root_cat = ['Science Kits & Toys', 'Counting & Math Toys', 'Reading & Writing', 'Marble Runs', 'Musical Instruments', 'Gepgraphic Globes', 'Flash Cards', 'Rock Tumblers', 'Electronic Learning Products', 'Detective & Spy', 'Solar Power Kits', 'Habitats']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Stuffed Animals & Plush Toys': ######

            root_cat = ['Plush Figures', 'Plush Puppets', 'Teddy Bears & Stuffed Animals']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Puzzles': ######

            root_cat = ['Jigsaw Puzzles', 'Brain Teasers', 'Pegged Puzzles', 'Puzzle Play Mats', '3D Puzzles', 'Floor Puzzles', 'Puzzle Accessories', 'Sudoku Puzzles']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Tricycles & Scooters': ######

            root_cat = ['Scooters & Accessories', 'Balance Bikes', 'Bike Accessories', 'Electric Vehicles', 'Kids Bikes', 'Kids Helmets', 'Kids Protective Gear', 'Pedal Cars', 'Pull-Along Wagons', 'Ride On Toys', 'Skateboards', 'Skates', 'Tricycles', 'Unicycles']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Arts & Crafts': ######

            root_cat = ['Craft Kits', 'Clay Dough & Kinetic Sand', 'Drawing & Painting Supplies']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Baby & Toddler Toys': ######

            root_cat = ['Musical Toys', 'Sorting & Stacking Toys', 'Push & Pull Toys', 'Balls', 'Bath Toys', 'Car Seat & Stroller Toys', 'Hammering & Pounding Toys', 'Indoor Climbers & Play', 'Structures', 'Mirrors', 'Rattles & Plush Rings', 'Spinning Tops', 'Stick Horses', 'Teaching Clocks', 'Teethers']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Building Toys': ######

            root_cat = ['Building Sets', 'Stacking Blocks', 'Figures', 'Gear Sets', 'Storage & Accessories']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Party Supplies': ######

            root_cat = ['Balloons', 'Birthday Candles', 'Party Favors', 'Party Hats', 'Table Covers', 'Party Packs', 'Banners', 'Party Tableware', 'Pinatas']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Kids Electronics': ######

            root_cat = ['Remote & App Controlled Figure', 'Electronic Learning Toys', 'Plug & Play Video Games', 'Walkie Talkies', 'Electronic Pets', 'Dance Mats']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Novelty & Gag Toys': ######

            root_cat = ['Gag Toys', 'Magnetic Toys', 'Desk Toys', 'Water Balloons', 'Spy Gadgets', 'Slime & Putty Toys', 'Money Banks', 'Magic Kits & Accessories', 'Prisms & Kaleidoscopes', 'Nesting Dolls', 'Flying Toys']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Perfumes & Fragrances': ######

        sub_cat_text()

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



    if main == 'Fashion': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Womens Fashion', 'Mens Fashion', 'Kids & Baby Fashion'])



        if sub == 'Womens Fashion': ######

            root_cat = ['Clothing', 'Eyewear', 'Accessories', 'Bags & Wallets', 'Womens Hats & Caps', 'Shoes']

            root_cat_text()

            for i in range(len(root_cat)):
                if root_cat[i] == 'Clothing':
                    with col4.expander('Clothing'):

                        data = {'Traditional Arabian Wear':['Abayas', 'Dresses', 'Hijabs']}
                        root_cat_df(data)

                        st.write('Dresses')
                        st.write('Tops Tees & Blouses')
                        st.write('Hoodies')
                        
                        data = {'Tights & Leggings':['Leggings', 'Tights']}
                        root_cat_df(data)

                        st.write('Skirts')
                        st.write('Pants')
                        st.write('Jeans')
                        st.write('Sweatshirts')
                        st.write('Coats')
                        st.write('Jackets')
                        st.write('Shorts')
                        st.write('Socks')
                        
                        data = {'Sports & Gym Wear':['Topwear', 'Bottomwear', 'Tracksuits']}
                        root_cat_df(data)

                        data = {'Lingerie & Sleepwear':['Bras', 'Camisoles & Slips', 'Panties', 'Lingerie Sets', 'Night Dresses', 'Shape-Wear']}
                        root_cat_df(data)

                        data = {'Swim & Beachwear':['Bikinis', 'Shorts', 'Tankinis']}
                        root_cat_df(data)

                        data = {'Maternity':['Dresses', 'Lingerie & Underwear', 'Nursing', 'Tops & Tees']}
                        root_cat_df(data)

                        data = {'Traditional Indian Wear':['Sarees', 'Dress Material', 'Kurtas', 'Dupattas']}
                        root_cat_df(data)

                        st.write('Scarves & Wraps')


                elif root_cat[i] == 'Eyewear':
                    with col4.expander('Eyewear'):
                        st.write('Sunglasses')
                        st.write('Eyewear Frames')


                elif root_cat[i] == 'Bags & Wallets':
                    with col4.expander('Bags & Wallets'):
                        st.write('Handbags')
                        st.write('School Bags')
                        st.write('Wallets')


                elif root_cat[i] == 'Womens Hats & Caps':
                    with col4.expander('Womens Hats & Caps'):
                        st.write('Womens Baseball Caps')
                            

                elif root_cat[i] == 'Shoes':
                    with col4.expander('Bags & Wallets'):
                        st.write('Sandals')
                        st.write('Flats')
                        st.write('Sneakers')
                        st.write('Pumps')
                        st.write('Boots')
                        st.write('Slippers')
                        st.write('Sports Shoes')

                else:
                    col4.write(root_cat[i])



        if sub == 'Mens Fashion': ######

            root_cat = ['Mens Hats & Caps', 'Clothing', 'Accessories', 'Shoes']

            root_cat_text()

            for i in range(len(root_cat)):
                if root_cat[i] == 'Mens Hats & Caps':
                    with col4.expander('Mens Hats & Caps'):

                        st.write('Mens Baseball Cap')
                        st.write('Snap Back Cap')

        
                elif root_cat[i] == 'Clothing':
                    with col4.expander('Clothing'):

                        data = {'Top Tees & Shirts':['T-Shirts', 'Polos', 'Casual Shirts', 'Formal Shirts']}
                        root_cat_df(data)

                        st.write('Jackets')
                        st.write('Hoodies')
                        st.write('Pants')
                        st.write('Jeans')
                        st.write('Sweatshirts')
                        st.write('Coats')
                        st.write('Shorts')
                        
                        data = {'Swimwear':['Briefs', 'Shorts']}
                        root_cat_df(data)

                        data = {'Innerwear & Loungewear':['Briefs', 'Boxers', 'Trunks', 'Vests', 'Thermal', 'Pyjamas & Lounge Pants']}
                        root_cat_df(data)

                        st.write('Ghutras')
                        st.write('Tie')
                        st.write('Socks')


                elif root_cat[i] == 'Shoes':                    
                    col4.warning('CURRENTLY, "Shoes" CATEGORY IS DISABLED & THERE ARE NO ROOT-CATEGORIES')

                else:
                    col4.write(root_cat[i])



        if sub == 'Kids & Baby Fashion': ######

            root_cat = ['Boys', 'Girls', 'Baby Boys', 'Baby Girls']

            root_cat_text()

            for i in range(len(root_cat)):
                if root_cat[i] == 'Boys':
                    with col4.expander('Boys'):

                        st.write('Tops & Tees')
                        st.write('Boys Cap')
                        st.write('Hoodies & Sweatshirts')
                        st.write('Pants')
                        st.write('Jeans')
                        st.write('Shorts')
                        st.write('Suits & Blazers')
                        st.write('Socks')
                        st.write('Sleepwear & Robes')
                        st.write('Underwear')
                        st.write('Swimwear')
                        st.write('Sunglasses')
                        
                        data = {'Shoes':['Sneakers', 'Boots', 'Sport Shoes', 'Slippers']}
                        root_cat_df(data)

                        st.write('Bags & Accessories')


                elif root_cat[i] == 'Girls':                    
                    with col4.expander('Girls'):

                        data = {'Tops Tees & Blouses':['Tanks & Camis', 'T-Shirts']}
                        root_cat_df(data)

                        st.write('Skirts')
                        st.write('Pants & Capris')
                        st.write('Dresses')
                        st.write('Jeans')
                        st.write('Hoodies & Sweatshirts')
                        st.write('Tights & Leggings')
                        st.write('Track & Activewear Jacket')
                        st.write('Shorts')
                        st.write('Socks')
                        st.write('Sleepwear & Robes')
                        st.write('Underwear')
                        st.write('Swimwear')

                        data = {'Shoes':['Sneakers', 'Boots', 'Sport Shoes', 'Slippers']}
                        root_cat_df(data)

                        st.write('Sunglasses')
                        st.write('Bags & Accessories')


                elif root_cat[i] == 'Baby Boys':
                    with col4.expander('Baby Boys'):

                        st.write('Bodysuit')
                        st.write('Bottoms')
                        st.write('Tops')
                        st.write('Sneakers')


                elif root_cat[i] == 'Baby Girls':
                    with col4.expander('Baby Girls'):

                        st.write('Bodysuits')
                        st.write('Bottoms')
                        st.write('Tops')
                        st.write('Sneakers')
                        st.write('Dresses')
                        st.write('Sandals')
                        st.write('Boots')

                else:
                    col4.write(root_cat[i])



    if main == 'Luggage & Travel Gear': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Backpacks', 'Soft Trolley Bags', 'Hard Trolley Bags', 'Business & Laptop Bags', 'Duffel Bags', 'Cabin Baggage', 'Kids Bags', 'Luggage Accessories', 'Messenger Bags', 'Travel Plugs & Adapters', 'Luggage Sets', 'School Bags-Pencil Cases & Sets', 'Handbags & Shoulder Bags', 'Childrens Luggage', 'Suitcases', 'Waist Packs', 'Wallets & Card Cases', 'Money Organizers', 'Travel Garment Bags', 'Shopping Bags & Baskets'])
        


        if sub == 'Backpacks' or sub == 'Soft Trolley Bags' or sub == 'Hard Trolley Bags' or sub == 'Business & Laptop Bags' or sub == 'Duffel Bags' or sub == 'Cabin Baggage' or sub == 'Kids Bags' or sub == 'Luggage Accessories' or sub == 'Messenger Bags' or sub == 'Travel Plugs & Adapters': ######

            col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')

        elif sub == 'School Bags-Pencil Cases & Sets' or sub == 'Handbags & Shoulder Bags' or sub == 'Childrens Luggage' or sub == 'Suitcases' or sub == 'Waist Packs' or sub == 'Wallets & Card Cases' or sub == 'Money Organizers' or sub == 'Travel Garment Bags' or sub == 'Shopping Bags & Baskets': ######

            col4.warning('CURRENTLY, THIS SUB-CATEGORY IS DISABLED & THERE ARE NO ROOT-CATEGORIES')
        


    if main == 'Pharmacy': ######

        sub_cat_text()

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



    if main == 'Baby Care': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Infant Milk & Food', 'Bottle Feeding', 'Baby Medical & Health Care', 'Bathing', 'Weaning & Toddler Feeding', 'Diapering', 'Baby Oral Care', 'Wipes & Accessories', 'Baby Skin Care', 'Bips Pacifiers & Teethers', 'Breast Feed', 'Baby Grooming', 'Travel Gear & High Chairs', 'Safety Equipment'])



        if sub == 'Infant Milk & Food': ######

            root_cat = ['Infant Milk', 'Baby Fruits & Vegetables', 'Baby Cereals', 'Baby Snacks']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bottle Feeding': ######

            root_cat = ['Bottles', 'Bottle Nipples', 'Cleaning Accessories']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Baby Medical & Health Care': ######

            root_cat = ['Baby Thermometer']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bathing': ######

            root_cat = ['Baby Soaps & Cleansers', 'Baby Body Wash', 'Baby Shampoo']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Weaning & Toddler Feeding': ######

            root_cat = ['Forks Knives & Spoons']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Diapering': ######

            root_cat = ['Size 5 (11 to 25kg)', 'Size 6 (16kg +)']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Baby Oral Care': ######

            root_cat = ['Baby Toothbrushes']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Wipes & Accessories': ######

            root_cat = ['Wet Wipes', 'Wipes & Refills']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Baby Skin Care': ######

            root_cat = ['Baby Rash Cream', 'Baby Powder', 'Baby Lotion & Cream', 'Baby Hair Oils', 'Baby Massage Oils', 'Baby Sunscreen']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bips Pacifiers & Teethers': ######

            root_cat = ['Teethers', 'Pacifiers', 'Bips & Burp Towels']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Breast Feed': ######

            root_cat = ['Breast Pumps', 'Breast Pads', 'Breast Care', 'Breast Milk Containers', 'Nursing Pillows & Covers']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Baby Grooming': ######

            root_cat = ['Baby Hair Brush & Comb', 'Baby Nail Clippers', 'Baby Scissors']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Travel Gear & High Chairs': ######

            root_cat = ['Baby Carriers', 'High Chairs & Booster Seat', 'Car Seat & Accessories', 'Strollers Prams & Accessories']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Safety Equipment': ######

            root_cat = ['Baby Monitors']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Cakes & Flowers': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Fresh Flower Arrangement', 'Cakes', 'Flowers', 'Combos', 'Plants'])



        if sub == 'Fresh Flower Arrangement': ######

            root_cat = ['Flower Bouquet', 'Vase Arrangement', 'Flowers in Sleeve', 'Flowers in Box', 'Valentine Boquets']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Cakes': ######

            root_cat = ['Cup Cakes', 'Frosting Cakes', 'Any Occassion', 'Cake Slices', 'Cake Shake', 'Designer Cakes', 'Donut', 'Heart Shaped Cakes', 'Cartoon Cakes', 'Eggless Cakes', 'Photo Cakes', 'Dry Cakes', 'Cake in Jar']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Flowers': ######

            root_cat = ['Roses', 'Orchids', 'Lillies', 'Carnations', 'Anthuriums']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Combos': ######

            root_cat = ['Flowers & Chocolate', 'Cake with Flowers', 'Cake with Chocolates', 'Flowers & Teddy', 'Flowers & Sweets', 'Flowers & Dry Fruits']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Plants': ######

            root_cat = ['Flowering Plants', 'Air Purifying Plants', 'Lucky Bamboo', 'Money Plants', 'Premium Plants']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Home Decor & Furnishing': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Wall Decor', 'Home Decor', 'Kitchen Linen', 'Bathroom Linen', 'Bedroom Linen', 'Carpets & Rugs', 'Artworks', 'Curtains & Accessories'])



        if sub == 'Wall Decor': ######

            root_cat = ['Wall Decor & Hanging', 'Clocks', 'Stickers', 'Mirrors']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Home Decor': ######

            root_cat = ['Alarm Clocks', 'Cushion Covers', 'Home Fragrance']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Kitchen Linen': ######

            root_cat = ['Oven Gloves', 'Aprons', 'Table Cloths', 'Table Runners', 'Place Mats']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bathroom Linen': ######

            root_cat = ['Towel Sets', 'Bath Robe', 'Hand Towels', 'Bath Towel', 'Bath Sheets', 'Face Towels', 'Beach Towels', 'Bath Mats & Rugs', 'Bath Slippers', 'Shower Curtains', 'Washcloths']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bedroom Linen': ######

            root_cat = ['Bed Pillows', 'Kids Bedding', 'Pillow Cases', 'Sheets', 'Comforters', 'Duvets & Covers', 'Bedspreads', 'Blankets & Quilts', 'Mattress Toppers', 'Mattress & Pillow Protectors', 'Throws']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])

        

        if sub == 'Carpets & Rugs': ######

            root_cat = ['Carpets', 'Rugs', 'Door Mats']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])


        
        if sub == 'Artworks': ######

            root_cat = ['Canvas & Framed Paintings', 'Paintings', 'Wall Stickers', 'Posters & Prints']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Curtains & Accessories': ######

            root_cat = ['Curtains', 'Blinds', 'Valances', 'Tiers', 'Swags', 'Accessories']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Musical Instruments': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Guitars', 'DJ Equipments', 'Violin - Ukulele & Oud', 'Pianos & Keyboards'])

        if sub == 'Guitars' or sub == 'DJ Equipments' or sub == 'Violin - Ukulele & Oud' or sub == 'Pianos & Keyboards': ######

            col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



    if main == 'Gaming & Consoles': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Gaming Mice', 'Gaming Components', 'Gaming Headset', 'Gaming Chairs', 'Gaming Keyboard', 'Controllers-Joysticks & Accessories', 'PS4 Games', 'Xbox One Games', 'PS5 Games', 'Gaming Monitors', 'Gaming Consoles', 'Gaming Desktop', 'Gaming Laptop', 'Gaming Cases', 'PC Games'])

        if sub == 'Gaming Mice' or sub == 'Gaming Components' or sub == 'Gaming Headset' or sub == 'Gaming Chairs' or sub == 'Gaming Keyboard' or sub == 'Controllers-Joysticks & Accessories' or sub == 'PS4 Games' or sub == 'Xbox One Games' or sub == 'PS5 Games' or sub == 'Gaming Monitors' or sub == 'Gaming Consoles' or sub == 'Gaming Desktop': ######

            col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')

        elif sub == 'Gaming Laptop' or sub == 'Gaming Cases' or sub == 'PC Games': ######

            col4.warning('CURRENTLY, THIS SUB-CATEGORY IS DISABLED')



    if main == 'Diet & Nutrition': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Vitamins & Supplements', 'Protein', 'Weight Management', 'Herbs & Natural Solutions', 'Performance', 'Digestion', 'Super Foods & Green Foods'])



        if sub == 'Vitamins & Supplements': ######

            root_cat = ['Multivitamins', 'Vitamins A-Z', 'Fish Oil & Omegas', 'Nutritional Supplements', 'Specialty Supplements', 'Antioxidants', 'Joint Support', 'Wellness Essentials', 'Minerals', 'Blended Vitamin & Mineral Supplements']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Protein': ######

            root_cat = ['Protein Drinks', 'Meal Replacements', 'Whey Protein', 'Mass Gainers', 'Protein Bars', 'Protein Blends', 'Casein Proteins', 'Plant Based Protein']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Weight Management': ######

            root_cat = ['Fat Burners & Thermogenics', 'Meal Replacements', 'Appetite Control & Diet Support', 'Ketogenic Friendly']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Herbs & Natural Solutions': ######

            root_cat = ['Natural Solutions', 'Herbs A-E', 'Herbs F-N', 'Herbs O-S', 'Herbs T-Z']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Performance': ######

            root_cat = ['Pre-Workout Supplements', 'Energy & Endurance', 'Muscle Builders', 'Performance Supplements']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Digestion': ######

            root_cat = ['Digestive Support', 'Cleansing & Detox']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Super Foods & Green Foods': ######

            root_cat = ['Super Foods', 'Green Foods']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Furniture & Storage': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Bathroom Storage & Organiser', 'Bedroom', 'Storage & Organisation', 'Living Room', 'Kitchen & Dining', 'Study Room', 'Home Bar', 'Kitchen & Dining', 'Outdoor Furniture'])



        if sub == 'Bathroom Storage & Organiser': ######

            root_cat = ['Soap Dishes', 'Bath Organizers', 'Toothbrush Holders', 'Toilet Brush Holders', 'Toilet Paper Holders', 'Dispensers', 'Bathroom Trash Bins', 'Tumblers', 'Towel Holders', 'Towel Hooks']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bedroom': ######

            root_cat = ['Tv Stand & Media Centers', 'Chest of Drawers', 'Bedside Tables', 'Beds', 'Mattresses', 'Wardrobes', 'Dressing Tables']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Storage & Organisation': ######

            root_cat = ['Ironing Boards', 'Racks Shelves & Drawers', 'Cabinet Organizers & Storage Baskets', 'Laundry Storage', 'Clothing & Closet Storage', 'Storage Containers']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Living Room': ######

            root_cat = ['Center Tables', 'Chairs', 'Side Tables', 'Sofa Beds', 'Sofa Sets', 'L-Shaped Sofas', 'Recliners', 'TV & Entertainment Units', 'Nested Tables', 'Bean Bags', 'Shoe Racks', 'Wall Shelves', 'Magazine Racks', 'Footstools']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Study Room': ######

            root_cat = ['Desks', 'Bookcases', 'Office Chairs']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])


        
        if sub == 'Home Bar': ######

            root_cat = ['Bar Table', 'Bar Cabinets', 'Bar Stools', 'Serving Trolleys']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Kitchen & Dining': ######

            root_cat = ['Dining Table Sets', 'Dining Tables', 'Dining Chairs', 'Dining Bench', 'Kitchen Cabinets']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Outdoor Furniture': ######

            root_cat = ['Swing Chairs', 'Hammocks', 'Patio Umbrella', 'Outdoor Furniture Sets']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Automotive': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Car Mobile Accessories', 'Car Services', 'Tires & Wheels'])

        if sub == 'Car Mobile Accessories' or sub == 'Car Services' or sub == 'Tires & Wheels': ######

            col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



    if main == 'Home Improvement & Lighting': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Functional Lighting', 'Electricals', 'Safes & Security', 'Fixtures', 'Bathroom & Kitchen Fixtures', 'Door Locks & Hardware', 'Patio Lawn & Garden'])



        if sub == 'Functional Lighting': ######

            root_cat = ['Desk Lights & Lamps']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Electricals': ######

            root_cat = ['Cables']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Safes & Security': ######

            root_cat = ['Video Door Phones']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Fixtures': ######

            root_cat = ['Ceiling Lights & Fans', 'Chandeliers', 'Office Ceiling Lights', 'Bathroom Lights', 'Picture & Display Lights', 'Track Rail & Cable Lighting Systems']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Bathroom & Kitchen Fixtures': ######

            root_cat = ['Shower Heads', 'Health Faucets', 'Bathroom Basin Taps', 'Shower & Bath Taps', 'Bathroom Hardware', 'Kitchen Fixtures']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Door Locks & Hardware': ######

            root_cat = ['Hooks', 'Door Locks', 'Door Hardware', 'Cabinet Hardware', 'Furniture Hardware', 'Ladders', 'Painting Supplies & Wall Treatments', 'Building Supplies']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Patio Lawn & Garden': ######

            root_cat = ['Outdoor Lighting', 'Gardening & Lawn Care', 'Farm & Ranch', 'Pest Control']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'School Essential': ######

        sub_cat_text()

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



    if main == 'Telecom': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Batelco'])



        if sub == 'Batelco': ######

            root_cat = ['Mobile & Data', 'Home Broadband', 'Postpaid Plans', 'Mobile Broadband']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



    if main == 'Pet Supplies': ######

        sub_cat_text()

        sub = col1.radio('Choose Sub Category :', ['Cat Food', 'Cat Care & Accessories', 'Dog Care & Accessories', 'Dog Food', 'Fish Food & Accessories'])



        if sub == 'Cat Food': ######

            root_cat = ['Dry Cat Food Adult', 'Wet Cat Food', 'Dry Food Kitten', 'Cat Treats']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Cat Care & Accessories': ######

            root_cat = ['Cat Grooming Supplies', 'Cat Litter & Accessories', 'Cat Vitamins & Supplements', 'Cat Scratcher & Furniture', 'Cat Toys', 'Cat Microchips', 'Cat Odor Removers & Cleaning', 'Cat Collar Leashes & Harness', 'Cat Parasites Control', 'Cat Feeding Accessories & Bowls', 'Cat Carriers & Crates', 'Cat Beds', 'Cat Travel Essentials']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Dog Care & Accessories': ######

            root_cat = ['Dog Feeding Accessories & Bowls', 'Dog Litter Accessories', 'Dog Odor Removers & Cleaning', 'Dog Toys', 'Dog Microchips', 'Dog Collar Leashes & Harness', 'Dog Carriers & Crates', 'Dog Beds', 'Dog Vitamins & Supplies', 'Dog Grooming Supplies', 'Dog Parasites Control', 'Dog Travel Essentials']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Dog Food': ######

            root_cat = ['Dog Treats & Chews', 'Wet Dog Food', 'Dry Food Puppy', 'Dry Food Adult']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])



        if sub == 'Fish Food & Accessories': ######

            root_cat = ['Fish Food', 'Fish Tanks', 'Fish Pumps & Filter', 'Decors & Accessories', 'Equipments', 'Conditioner & Additives']

            root_cat_text()

            for i in range(len(root_cat)):
                col4.write(root_cat[i])




#### CATEGORY VIEWER ####
if menu == "VENDOR LIST":

    st.error("UNDER CONSTRUCTION")