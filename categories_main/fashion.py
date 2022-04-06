import streamlit as st
import time
import pandas as pd


def fashion_main():

    # defining columns for structure
    col1, col2, col3, col4 = st.columns([7.2,1,1,5])

    col2.empty()
    col3.empty()

    def root_cat_text():

        col4.subheader('ROOT CATEGORIES')

        with col4:

            with st.spinner(text = "Please Wait"):

                time.sleep(0.5)

    def root_cat_df(data):
        df = pd.DataFrame(data)
        df.index += 1
        st.table(df)

    col1.subheader('SUB CATEGORIES')

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