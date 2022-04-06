import streamlit as st
import time


def health_beauty_main():

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