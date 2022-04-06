"""importing libraries"""
import streamlit as st
from PIL import Image

# INITIAL PAGE LAYOUT SETTINGS
favicon_img = Image.open("images/wafi_favicon.ico")
st.set_page_config(
        page_title = "WafiApps",
        initial_sidebar_state = "auto",
        page_icon = favicon_img,
        layout = "centered"
        )

from streamlit_lottie import st_lottie
import main_categories
import utils
from categories_main import supermarket, watches, appliances, kitchen_dining, health_beauty, electronics, computers_it, tools_diy, office_supplies, mobiles_tablets, toys_games, perfumes_fragrances, fashion, luggage_travelgear, pharmacy, baby_care, cakes_flowers, home_decor, musical_instruments, gaming_consoles, diet_nutrition, furniture_storage, automotive, home_improvement, school_essential, telecom, pet_supplies




st.sidebar.title("NAVIGATION")

# defining various pages in the application
main_menu = ['INTRO', 'CATEGORY VIEWER']

with st.container():

    menu = st.sidebar.selectbox('Go to', main_menu)



#### INTRO ####
if menu == "INTRO":

    sidebar_img = Image.open("images/wafi_logo_text.png")

    st.image(sidebar_img, use_column_width = True, output_format = 'PNG')

    #LOTTIE_LOCAL_PATH = "lottie_files/shopping_lottie.json"
    LOTTIE_URL = "https://assets3.lottiefiles.com/packages/lf20_57TxAX.json"
    lottie_sidebar = utils.intro_lottie(LOTTIE_URL)
    st_lottie(lottie_sidebar, height = 375, renderer = "svg")




#### CATEGORY VIEWER ####
if menu == "CATEGORY VIEWER":

    utils.main_heading_text()

    st.sidebar.title('MAIN CATEGORIES')

    main_list = main_categories.main_categories()

    cat_list = main_list['category_list'].unique().tolist()

    main = st.sidebar.radio('Choose Main Category :', cat_list)

    st.markdown('<p></p>', unsafe_allow_html = True)



    if main == 'Supermarket': ######

        supermarket.supermarket_main()


    if main == 'Watches': ######

        watches.watches_main()


    if main == 'Appliances': ######

        appliances.appliances_main()

        
    if main == 'Kitchen & Dining': ######

        kitchen_dining.kitchen_dining_main()


    if main == 'Health & Beauty': ######

        health_beauty.health_beauty_main()


    if main == 'Electronics': ######

        electronics.electronics_main()


    if main == 'Computers & IT': ######

        computers_it.computers_it_main()


    if main == 'Tools & DIY': ######

        tools_diy.tools_diy_main()


    if main == 'Office Supplies': ######

        office_supplies.office_supplies_main()


    if main == 'Mobiles & Tablets': ######

        mobiles_tablets.mobiles_tablets_main()


    if main == 'Toys & Games': ######

        toys_games.toys_games_main()


    if main == 'Perfumes & Fragrances': ######

        perfumes_fragrances.perfumes_fragrances_main()


    if main == 'Fashion': ######

        fashion.fashion_main()


    if main == 'Luggage & Travel Gear': ######

        luggage_travelgear.luggage_travelgear_main()


    if main == 'Pharmacy': ######

        pharmacy.pharmacy_main()


    if main == 'Baby Care': ######

        baby_care.baby_care_main()


    if main == 'Cakes & Flowers': ######

        cakes_flowers.cakes_flowers_main()


    if main == 'Home Decor & Furnishing': ######

        home_decor.home_decor_main()


    if main == 'Musical Instruments': ######

        musical_instruments.musical_instruments_main()


    if main == 'Gaming & Consoles': ######

        gaming_consoles.gaming_consoles_main()


    if main == 'Diet & Nutrition': ######

        diet_nutrition.diet_nutrition_main()


    if main == 'Furniture & Storage': ######

        furniture_storage.furniture_storage_main()


    if main == 'Automotive': ######

        automotive.automotive_main()


    if main == 'Home Improvement & Lighting': ######

        home_improvement.home_improvement_main()


    if main == 'School Essential': ######

        school_essential.school_essential_main()


    if main == 'Telecom': ######

        telecom.telecom_main()


    if main == 'Pet Supplies': ######

        pet_supplies.petsupplies_main()




#### CATEGORY VIEWER ####
if menu == "VENDOR LIST":

    st.error("UNDER CONSTRUCTION")