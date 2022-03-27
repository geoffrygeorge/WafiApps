import streamlit as st
import time
# import pandas as pd
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
    padding-top: 0.5px;
    font-size: calc(0.70em + 4.5vmin);
    font-family: sans-serif;
}
</style>
""", unsafe_allow_html = True)


st.markdown('<p class="big-font">WAFIAPPS CATEGORY VIEWER</p>', unsafe_allow_html = True)

#st.sidebar.image("wafi_logo.png", width = 100)

main = st.sidebar.radio('CHOOSE MAIN CATEGORY :', ['Supermarket', 'Watches', 'Appliances', 'Kitchen & Dining', 'Health & Beauty', 'Electronics', 'Computers & IT', 'Tools & DIY', 'Office Supplies', 'Mobiles & Tablets', 'Toys & Games', 'Perfumes & Fragrances', 'Fashion', 'Luggage & Travel Gear', 'Pharmacy', 'Baby Care', 'Cakes & Flowers', 'Home Decor & Furnishing', 'Musical Instruments', 'Gaming & Consoles', 'Diet & Nutrition', 'Furniture & Storage', 'Automotive', 'Home Improvement & Lighting', 'School Essential', 'Telecom', 'Pet Supplies'])

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
col1, col2, col3, col4 = st.columns([7,1,1,5])


def root_cat_text():

    col4.subheader('ROOT CATEGORIES')

    with col4:

        with st.spinner(text = "Please Wait"):

            time.sleep(0.5)


if main == 'Supermarket': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Frozen Items', 'Beverages', 'Dairy & Eggs', 'Tea & Coffee', 'Cooking Ingredients', 'Organic', 'Tins Jars & Packets', 'Fresh Fruits & Vegetables', 'Chocolate & Confectionery','Fish & Meat', 'Rice Pasta & Pulses', 'Nuts Dates & Dried Fruits', 'Biscuits Crackers & Cakes', 'Chips Dips & Snacks', 'Breakfast Cereals', 'Condiments-Dressings & Marinades', 'Bakery', 'Household Cleaners', 'Jams Honey & Spreads', 'Salt & Sugar', 'Laundry', 'Home Baking & Desserts', 'Disposable Kitchenware', 'Tissues & Toilet Paper', 'Air Fresheners & Deodorizers', 'Shoe Care & Polish', 'Dishwashing Supplies', 'Papers Foils & Wraps', 'Protein', 'Barbecue', 'Insecticides'])



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

        root_cat = ['Whole Grains & Beans', 'Cooking & Baking', 'Oils & Vinegar', 'Spices & Powders', 'Tea Coffee & Drinks']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tins Jars & Packets': ######

        root_cat = ['Soup & Instant Noodles', 'Canned Vegetables', 'Tuna & Seafood', 'Canned Fruits', 'Powdered Milk', 'Pickles & Olives', 'Coconut Milk & Cream', 'Canned Milk', 'Canned Vegetable']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Fresh Fruits & Vegetables': ######

        root_cat = ['Fresh Fruits', 'Fresh Vegetables']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Chocolate & Confectionery': ######

        root_cat = ['Chocolates', 'Indian Sweets & Snacks', 'Candy', 'Gums & Mints', 'Chocolate']

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

        root_cat = ['Cereals & Bars', 'Oats', 'Granola & Bars']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Condiments-Dressings & Marinades': ######

        root_cat = ['Sauces & Condiments', 'Salad Dressings & Vinaigrettes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bakery': ######

        root_cat = ['Sweets & Pastries', 'Croissant', 'Bread & Rolls', 'Wraps Pittas Naan & Thins', 'Cookies & Muffin', 'Pastries']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Household Cleaners': ######

        root_cat = ['Scrubs & Sponges', 'Mops & Bucket Sets', 'Bathroom Cleaners & Fresheners', 'Bleach & Disinfectants', 'Cleaning Gloves', 'Kitchen Cleaner', 'Kitchen Cloth & Cleaning Wipes', 'Multipurpose Cleaner', 'Sink & Drain Unblocker', 'Wood & Metal Polish', 'Window Cleaners']

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

        root_cat = ['Washing Powder', 'Washing Liquid & Gel', 'Stain Remover & Color Care']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Home Baking & Desserts': ######

        root_cat = ['Baking Ingredients', 'Desserts', 'Flour & Bread Mixes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Disposable Kitchenware': ######

        root_cat = ['Bin Liners & Garbage Bags', 'Disposable Bowl & Tray', 'Disposable Cups & Glasses', 'Disposable Cutlery']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tissues & Toilet Paper': ######

        root_cat = ['Facial Tissues', 'Maxi Roll & Kitchen Roll', 'Toilet Paper']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Air Fresheners & Deodorizers': ######

        root_cat = ['Aerosols & Room Sprays', 'Car Air Freshener', 'Gels & Blocks Air Freshener']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Shoe Care & Polish': ######

        root_cat = ['Shoe Cleaners', 'Shoe Polish']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dishwashing Supplies': ######

        root_cat = ['Dishwashing Liquid', 'Dishwashing Powder & Paste']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Papers Foils & Wraps': ######

        root_cat = ['Cling Film', 'Kitchen Aluminium Foil']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Protein': ######

        root_cat = ['Protein Drinks']

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

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Mens Wrist Watch', 'Womens Wrist Watch', 'Boys Watches', 'Girls Watches'])

    if sub == 'Mens Wrist Watch' or sub == 'Womens Wrist Watch' or sub == 'Boys Watches' or sub == 'Girls Watches': ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



if main == 'Appliances': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Kitchen Appliances', 'Home Appliances', 'Washing Machines & Dryers', 'Cooktops & Ranges', 'Refrigerators & Freezers', 'Microwave Ovens', 'Air Conditioners', 'Heating Cooling & Air Quality'])



    if sub == 'Kitchen Appliances': ######

        root_cat = ['Coffee Machines & Grinders', 'Hand Blenders & Mixers', 'Electric Kettles', 'Fryers', 'Juicers', 'Rice Cookers', 'Food Processors', 'Toasters', 'Oven & Toaster Grills', 'Mixer Grinders', 'Induction Cooktops', 'Snack Maker', 'Sandwich Makers', 'Bread Maker', 'Electric Steamers', 'Microwave Ovens', 'Meat Grinders & Mincers', 'Choppers & Chippers', 'Milk Frothers', 'Waffle & Dessert Makers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Home Appliances': ######

        root_cat = ['Irons & Steamers', 'Vacuum Cleaners', 'Water Dispensers & Purifiers', 'Dishwashers']

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

        root_cat = ['Single Door', 'Chest Freezer & Chiller', 'Double Door', 'Side by Side']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Microwave Ovens': ######

        root_cat = ['Solo', 'Grill']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Air Conditioners': ######

        root_cat = ['Split ACs', 'Window ACs']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Heating Cooling & Air Quality': ######

        root_cat = ['Air Purifiers', 'Fans', 'Humidifiers', 'Air Coolers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Kitchen & Dining': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Cookware', 'Kitchen Tools', 'Serveware', 'Bakeware', 'Kitchen Storage & Containers', 'Dinner Sets'])


    if sub == 'Cookware': ######

        root_cat = ['Frying Pans & Saucepans', 'Cookpots & Casseroles', 'Cookware Sets', 'Pressure Cookers', 'Kadhais & Woks', 'Tawas', 'Cooking Spoons', 'Tadka Pans']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Kitchen Tools': ######

        root_cat = ['Knives', 'Utensils & Gadgets', 'Measures & Scales', 'Choppers & Chippers', 'Graters & Slicers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Serveware': ######

        root_cat = ['Hotpots', 'Cups & Mugs', 'Serving Bowls', 'Cutlery', 'Serving Trays', 'Glassware & Drinkware']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bakeware': ######

        root_cat = ['Baking Tools', 'Cake & Muffin Moulds', 'Mixing Bowls', 'Serving Bowls']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Kitchen Storage & Containers': ######

        root_cat = ['Water Bottles & Flasks', 'Jars & Containers', 'Food Savers', 'Countertop & Wall Organization', 'Lunch Boxes & Bags', 'Cooler']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])   



    if sub == 'Dinner Sets': ######

        root_cat = ['Opalware & Glass', 'Plates']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i]) 



if main == 'Health & Beauty': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Face', 'Facial Skincare', 'Skin Care', 'Lips', 'Eyes', 'Hair Care', 'Bath & Body', 'Oral Hygiene', 'Makeup Tools & Accessories', 'Medicine & Treatment', 'Womens Toiletries', 'Suncare & Travel', 'Nail & Nail Polish', 'Mens Grooming'])



    if sub == 'Face': ######

        root_cat = ['Foundation & Contour', 'Concealer & Corrector', 'Primer Makeup', 'Facial Serum', 'Blushes & Bronzers', 'Powder', 'Makeup Sets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Facial Skincare': ######

        root_cat = ['Face Cream & Moisturizer', 'Cleanser Toner & Face Mask', 'Anti Wrinkle Skin Care', 'Cotton Wool', 'Face Wash & Scrub', 'Face Wipes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Skin Care': ######

        root_cat = ['Oil & Petroleum Jelly', 'Footcare & Handcare', 'Hand Sanitizers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])       



    if sub == 'Lips': ######

        root_cat = ['Lipstick', 'Lip Liner']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])  



    if sub == 'Eyes': ######

        root_cat = ['Eyeliner & Mascara', 'Eye Pencil & Brow Liner', 'Eyelash Treatment', 'Eye Shadow & Eye Makeup Kit']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])  



    if sub == 'Hair Care': ######

        root_cat = ['Hair Styling Accessories', 'Hair Treatment Serum & Oil', 'Shampoo', 'Conditioner', 'Hair Colourants', 'Hair Styling Creams & Lotions']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])  



    if sub == 'Bath & Body': ######

        root_cat = ['Body Wash & Shower Gel', 'Bath Accessories', 'Hand Wash & Soap', 'Talcum Powder']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i]) 



    if sub == 'Oral Hygiene': ######

        root_cat = ['Power Toothbrushes & Accessories', 'Tooth Brush & Floss', 'Toothpaste', 'Mouthwash']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])      


            
    if sub == 'Makeup Tools & Accessories': ######

        root_cat = ['Brush Set']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])   



    if sub == 'Medicine & Treatment': ######

        root_cat = ['First Aid', 'Pain Relief', 'Heartburn & Indigestion', 'Sore Throat & Cough Medicine']

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

        root_cat = ['Nail Treatment', 'Nail Polish Remover', 'Manicure Kits']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i]) 



    if sub == 'Mens Grooming': ######

        root_cat = ['Mens Deodorants & Antiperspirants', 'Shaving Cream Foams & Gels', 'Mens Razor & Blade']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i]) 



if main == 'Electronics': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Personal Care for Women', 'Headphones & Earphones', 'Personal Care for Men', 'Speakers', 'Wearable Technology', 'Cameras & Accessories', 'Health Care Appliances', 'Smart Home & Office', 'Televisions', 'Telephones', 'Audio & Video'])



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

        root_cat = ['Smart Watch', 'Activity Trackers', 'Arm & Wristbands', 'Apple Watch']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cameras & Accessories': ######

        root_cat = ['Instant Film Cameras', 'Lenses & Accessories', 'DSLR Cameras', 'Action Cameras']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Health Care Appliances': ######

        root_cat = ['Health Massagers', 'Weighing Scales', 'BP Monitors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Smart Home & Office': ######

        root_cat = ['CCTV Cameras & Accessories', 'Intercom Systems']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Televisions': ######

        root_cat = ['Cables & Accessories', 'Smart TV', 'Ultra HD TV']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Telephones': ######

        root_cat = ['Landphones', 'Telephone Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Audio & Video': ######

        root_cat = ['Audio & Video Accessories', 'Projectors', 'Hi-Fi & Home Audio', 'Home Theatre Systems', 'Set-Top Boxes']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Computers & IT': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Computer Cables & Connectors', 'Networking Devices', 'Mouses & Keyboards', 'Laptops', 'Storage Devices', 'Computer AV Accessories', 'Monitors', 'Printers & Scanners', 'Toners & Cartridges', 'Softwares', 'Components & Parts'])



    if sub == 'Computer Cables & Connectors': ######

        root_cat = ['HDMI Cables', 'USB Cables', 'USB Hubs', 'Adapters', 'Ethernet Cables', 'SATA Cables']

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

        root_cat = ['Laptop', 'Business Laptops', 'MS Surface']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Storage Devices': ######

        root_cat = ['External Data Storage', 'Internal Data Storage', 'Flash Drives']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Computer AV Accessories': ######

        root_cat = ['Webcams & Voip', 'Computer Headsets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Monitors': ######

        root_cat = ['Monitor Accessories', 'Projectors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Printers & Scanners': ######

        root_cat = ['Ink Tank Printers', 'Inkjet Printers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Toners & Cartridges': ######

        root_cat = ['Ink Cartridges']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Softwares': ######

        root_cat = ['Operating Systems']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Components & Parts': ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



if main == 'Tools & DIY': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Hand Tools', 'Power Tools', 'Safety & Security', 'Professional Cleaning Products', 'Garden Tools', 'Hardware', 'Painting Supplies & Wall Treatment', 'Power Solutions'])



    if sub == 'Hand Tools': ######

        root_cat = ['Tool Sets', 'Screw Drivers', 'Measure & Layout Tools', 'Multi Tools', 'Pliers', 'Hammers', 'Tool Boxes', 'Cutting Tools', 'Chisels', 'Wrenchs', 'Saws']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])


        
    if sub == 'Power Tools': ######

        root_cat = ['Tool Sets', 'Sawing Tools', 'Jig Saws & Blades', 'Cordless Drill', 'Drilling', 'Sanding Tools', 'Planers', 'Cutting Tools', 'Pneumatic Tools', 'Routers', 'Staplers', 'Grinding Tools', 'Rotary Hammers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Safety & Security': ######

        root_cat = ['Eye Protection', 'Safety Shoes', 'Head Protection', 'Hand & Arm Protection', 'Ear Protection']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Professional Cleaning Products': ######

        root_cat = ['Pressure Washers', 'Pro Vacuum Cleaners', 'Air Blowers', 'Steam Cleaners']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Garden Tools': ######

        root_cat = ['Lawn Movers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Hardware': ######

        root_cat = ['Adhesives & Sealers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Painting Supplies & Wall Treatment': ######

        root_cat = ['Paint Sprayers', 'Polishers']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Power Solutions': ######

        root_cat = ['Power Detectors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Office Supplies': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Office Pantry', 'Office Cleaning', 'Office Basics', 'Paper'])



    if sub == 'Office Pantry': ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



    if sub == 'Office Cleaning': ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



    if sub == 'Office Basics': ######

        root_cat = ['Battery', 'Scissors']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Paper': ######

        root_cat = ['Copy Paper', 'Other Paper']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Mobiles & Tablets': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Mobile Accessories', 'Mobile Phones', 'Tablets & iPad'])



    if sub == 'Mobile Accessories': ######

        root_cat = ['Mobile Cables', 'Mobile Chargers', 'Mobile Cases & Covers', 'Power Banks', 'Mobile Holders', 'Mobile Screen Protectors', 'SD Cards', 'Selfie Stick']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Mobile Phones': ######

        root_cat = ['Nokia', 'Samsung', 'Huawei', 'iPhone', 'OnePlus']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tablets & iPad': ######

        root_cat = ['Huawei', 'Alcatel', 'Lenovo']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Toys & Games': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Toy Figures & Playsets', 'Dolls & Accessories', 'Games & Accessories', 'Hobbies', 'Sports & Outdoor Play', 'Play Vehicles', 'Dress Up & Pretend Play', 'Learning & Education', 'Stuffed Animals & Plush Toys', 'Puzzles', 'Tricycles & Scooters', 'Arts & Crafts', 'Baby & Toddler Toys', 'Building Toys', 'Party Supplies'])



    if sub == 'Toy Figures & Playsets': ######

        root_cat = ['Action Figures']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dolls & Accessories': ######

        root_cat = ['Dolls', 'Doll Accessories', 'Doll House Accessories', 'Playsets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Games & Accessories': ######

        root_cat = ['Board Games', 'Card Games', 'Floor Games', 'Stacking Games', 'Arcade & Table Games', 'Tile Games']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Hobbies': ######

        root_cat = ['Collecting', 'Pre-built Display Models', 'Robotics']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Sports & Outdoor Play': ######

        root_cat = ['Blasters & Foam Play', 'Trampoline & Accessories', 'Play Sets & Playground Equipments']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Play Vehicles': ######

        root_cat = ['Toy Vehicles']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Dress Up & Pretend Play': ######

        root_cat = ['Pretend Play']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Learning & Education': ######

        root_cat = ['Science Kits & Toys']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Stuffed Animals & Plush Toys': ######

        root_cat = ['Plush Figures', 'Teddy Bears & Stuffed Animals']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Puzzles': ######

        root_cat = ['Jigsaw Puzzles']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Tricycles & Scooters': ######

        root_cat = ['Scooters & Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Arts & Crafts': ######

        root_cat = ['Craft Kits']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Baby & Toddler Toys': ######

        root_cat = ['Musical Toys', 'Sorting & Stacking Toys']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Building Toys': ######

        root_cat = ['Building Sets']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Party Supplies': ######

        root_cat = ['Balloons']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Perfumes & Fragrances': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ["Arabic Perfumes", "Men's Perfume", "Women's Perfume", "Unisex Perfumes", "Fragrance Sets"])



    if sub == "Arabic Perfumes": ######

        root_cat = ["Unisex Arabic Perfumes", "Women's Eau de Parfum", "Men's Eau de Parfum", "Oudh", "Perfume Oils", "Bakhoor", "Athar"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Men's Perfume": ######

        root_cat = ["Eau de Toilette", "Eau de Parfum"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Women's Perfume": ######

        root_cat = ["Eau de Parfum", "Eau de Toilette"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Unisex Perfumes": ######

        root_cat = ["Eau de Parfum", "Eau de Toilette"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == "Fragrance Sets": ######

        root_cat = ["Women Fragrance Gift Set", "Men Fragrance Gift Set"]

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Fashion': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Womens Fashion', 'Mens Fashion', 'Kids & Baby Fashion'])



    if sub == 'Womens Fashion': ######

        root_cat = ['Clothing', 'Eyewear', 'Accessories', 'Bags & Wallets']

        root_cat_text()

        for i in range(len(root_cat)):
            if root_cat[i] == 'Clothing':
                with col4.expander('Clothing'):
                    st.write('Traditional Arabian ▶ Abayas')
                    st.write('Dresses')
                    st.write('Tops Tees & Blouses')
                    st.write('Hoodies')

            elif root_cat[i] == 'Eyewear':
                    with col4.expander('Eyewear'):
                        st.write('Sunglasses')


            elif root_cat[i] == 'Bags & Wallets':
                    with col4.expander('Bags & Wallets'):
                        st.write('Handbags')

            else:
                col4.write(root_cat[i])



    if sub == 'Mens Fashion': ######

        root_cat = ['Mens Hats & Caps', 'Clothing', 'Accessories']

        root_cat_text()

        for i in range(len(root_cat)):
            if root_cat[i] == 'Mens Hats & Caps':
                with col4.expander('Mens Hats & Caps'):
                    st.write('Mens Baseball Cap')
                    st.write('Snap Back Cap')

       
            elif root_cat[i] == 'Clothing':
                with col4.expander('Clothing'):
                    st.write('Top Tees & Shirts')
                    st.write('Jackets')
                    st.write('Hoodies')

            else:
                col4.write(root_cat[i])



    if sub == 'Kids & Baby Fashion': ######

        root_cat = ['Boys']

        root_cat_text()

        for i in range(len(root_cat)):
            if root_cat[i] == 'Boys':
                with col4.expander('Boys'):
                    st.write('Tops & Tees')
                    st.write('Boys Cap')

            else:
                col4.write(root_cat[i])



if main == 'Luggage & Travel Gear': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Backpacks', 'Soft Trolley Bags', 'Hard Trolley Bags', 'Business & Laptop Bags', 'Duffel Bags', 'Cabin Baggage', 'Kids Bags', 'Luggage Accessories', 'Messenger Bags', 'Travel Plugs & Adapters'])
    


    if sub == 'Backpacks' or sub == 'Soft Trolley Bags' or sub == 'Hard Trolley Bags' or sub == 'Business & Laptop Bags' or sub == 'Duffel Bags' or sub == 'Cabin Baggage' or sub == 'Kids Bags' or sub == 'Luggage Accessories' or sub == 'Messenger Bags' or sub == 'Travel Plugs & Adapters': ######

        col4.info('CURRENTLY, THERE ARE NO ROOT-CATEGORIES FOR THE SELECTED SUB-CATEGORY')



if main == 'Pharmacy': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Braces Splints & Supports', 'Bed Pillows & Positioners', 'Face Mask', 'Pain Relief Medications & Treatments', 'Walkers Rollators & Accessories', 'Home Tests'])



    if sub == 'Braces Splints & Supports': ######

        root_cat = ['Leg & Foot Supports', 'Arm Hand & Finger Supports', 'Back Neck & Shoulder Supports', 'Hip & Waist Supports', 'Athletic Tapes & Wraps', 'Chest Supports']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Bed Pillows & Positioners': ######

        root_cat = ['Neck & Cervical Pillows', 'Contoured Support Pillows', 'Bed Pillows']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Face Mask': ######

        root_cat = ['Surgical Face Mask']

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

        root_cat = ['Pregnancy Tests']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



if main == 'Baby Care': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Infant Milk & Food', 'Bottle Feeding', 'Baby Medical & Health Care', 'Bathing', 'Weaning & Toddler Feeding', 'Diapering', 'Baby Oral Care'])



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



if main == 'Cakes & Flowers': ######

    sub = col1.radio('CHOOSE SUB CATEGORY :', ['Fresh Flower Arrangement', 'Cakes', 'Flowers', 'Combos', 'Plants'])



    if sub == 'Fresh Flower Arrangement': ######

        root_cat = ['Flower Bouquet', 'Vase Arrangement', 'Flowers in Sleeve']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Cakes': ######

        root_cat = ['Cup Cakes', 'Frosting Cakes', 'Any Occassion', 'Cake Slices', 'Cake Shake', 'Designer Cakes', 'Donut']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Flowers': ######

        root_cat = ['Roses']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Combos': ######

        root_cat = ['Flowers & Chocolate']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])



    if sub == 'Plants': ######

        root_cat = ['Flowering Plants', 'Money Plants']

        root_cat_text()

        for i in range(len(root_cat)):
            col4.write(root_cat[i])