import time
import streamlit as st
import pandas as pd
import utils
import main_categories

def vendor_viewer_main():

    def break_loop():
        i = 0
        while i < 5:
            st.markdown('<p></p>', unsafe_allow_html = True)
            i += 1

    # data transformation
    main_list = main_categories.main_categories()

    cat_list = main_list['category_list'].unique().tolist()

    all_vendor_df = pd.read_csv('data/vendors.csv')
    all_vendor_df = all_vendor_df.sort_values(by = ['Vendor Name'])
    all_vendor_df = all_vendor_df.reset_index(drop=True)
    all_vendor_df = all_vendor_df.drop(['Disapproval Reason', 'Vendor Status'], axis = 1)
    vendor_enabled_df = all_vendor_df[all_vendor_df['Vendor Shop Status'] == 'Enabled']
    vendor_disabled_df = all_vendor_df[all_vendor_df['Vendor Shop Status'] == 'Disabled']

    # creating lists
    all_vendor_list = all_vendor_df['Vendor Name'].unique().tolist()
    vendor_enabled_list = vendor_enabled_df['Vendor Name'].unique().tolist()
    vendor_disabled_list = vendor_disabled_df['Vendor Name'].unique().tolist()

    # vendor shop status filter
    st.sidebar.title('FILTER (BY SHOP STATUS)')
    shop_status_choice = st.sidebar.selectbox('Vendor Shop Status', options = ['Enabled & Disabled', 'Enabled', 'Disabled'])



    if shop_status_choice == 'Enabled & Disabled':

        with st.expander('Dataframe'):
            st.dataframe(all_vendor_df)

        with st.sidebar.expander('VENDOR LIST', expanded = True):
            vendor = st.radio('Choose Vendor :', all_vendor_list)

        # to get name
        vendor_name = all_vendor_df['Vendor Name'].loc[all_vendor_df['Vendor Name'] == vendor]
        vendor_name = vendor_name.tolist()

        # to get email id
        vendor_email = all_vendor_df['Vendor Email'].loc[all_vendor_df['Vendor Name'] == vendor]
        vendor_email = vendor_email.tolist()

        # to get vendor shop status
        vendor_shop_status = all_vendor_df['Vendor Shop Status'].loc[all_vendor_df['Vendor Name'] == vendor]
        vendor_shop_status = vendor_shop_status.tolist()

        # to get vendor commission status
        vendor_commission_status = all_vendor_df['Commission Status'].loc[all_vendor_df['Vendor Name'] == vendor]
        vendor_commission_status = vendor_commission_status.tolist()

        # to get vendor phone number will come soon

        # to get vendor categories
        vendor_categories = all_vendor_df[cat_list].loc[all_vendor_df['Vendor Name'] == vendor]

        vendor_categories = vendor_categories.dropna(axis=1, inplace=False)

        st.header('VENDOR IMFORMATION:')

        with st.spinner(text = "Please Wait"):
            
            time.sleep(0.5)

        col1, col2, col3, col4 = st.columns([8,1,1,4])

        col2.empty()
        col3.empty()

        with col1:
            st.subheader('Vendor Name:')
            st.text(' '.join(vendor_name))
            break_loop()

        with col4:
            st.subheader('Vendor Email:')
            st.text(' '.join(vendor_email))
            break_loop()

        with col1:
            st.subheader('Vendor Shop Status:')
            st.text(' '.join(vendor_shop_status))

        utils.break_loop_vendor_viewer()

        st.header('COMMISSION RATE & CATEGORIES:')

        st.subheader('Commission Status:')
        st.text(' '.join(vendor_commission_status))
        break_loop()
        
        st.subheader('Commission Categories')
        vendor_categories = vendor_categories.reset_index(drop=True)
        st.dataframe(vendor_categories)




    if shop_status_choice == 'Enabled':

        with st.expander('Dataframe'):
            st.dataframe(vendor_enabled_df)

        with st.sidebar.expander('VENDOR LIST', expanded = True):
            vendor = st.radio('Choose Vendor :', vendor_enabled_list)

        # to get name
        vendor_name = vendor_enabled_df['Vendor Name'].loc[vendor_enabled_df['Vendor Name'] == vendor]
        vendor_name = vendor_name.tolist()

        # to get email id
        vendor_email = vendor_enabled_df['Vendor Email'].loc[vendor_enabled_df['Vendor Name'] == vendor]
        vendor_email = vendor_email.tolist()

        # to get vendor shop status
        vendor_shop_status = vendor_enabled_df['Vendor Shop Status'].loc[vendor_enabled_df['Vendor Name'] == vendor]
        vendor_shop_status = vendor_shop_status.tolist()

        # to get vendor commission status
        vendor_commission_status = vendor_enabled_df['Commission Status'].loc[vendor_enabled_df['Vendor Name'] == vendor]
        vendor_commission_status = vendor_commission_status.tolist()

        # to get vendor phone number will come soon

        # to get vendor categories
        vendor_categories = vendor_enabled_df[cat_list].loc[vendor_enabled_df['Vendor Name'] == vendor]

        vendor_categories = vendor_categories.dropna(axis=1, inplace=False)

        st.header('VENDOR IMFORMATION:')

        with st.spinner(text = "Please Wait"):
            
            time.sleep(0.5)

        col1, col2, col3, col4 = st.columns([8,1,1,4])

        col2.empty()
        col3.empty()

        with col1:
            st.subheader('Vendor Name:')
            st.text(' '.join(vendor_name))
            break_loop()

        with col4:
            st.subheader('Vendor Email:')
            st.text(' '.join(vendor_email))
            break_loop()

        with col1:
            st.subheader('Vendor Shop Status:')
            st.text(' '.join(vendor_shop_status))

        utils.break_loop_vendor_viewer()

        st.header('COMMISSION RATE & CATEGORIES:')

        st.subheader('Commission Status:')
        st.text(' '.join(vendor_commission_status))
        break_loop()
        
        st.subheader('Commission Categories')
        vendor_categories = vendor_categories.reset_index(drop=True)
        st.dataframe(vendor_categories)




    if shop_status_choice == 'Disabled':

        with st.expander('Dataframe'):
            st.dataframe(vendor_disabled_df)

        with st.sidebar.expander('VENDOR LIST', expanded = True):
            vendor = st.radio('Choose Vendor :', vendor_disabled_list)

        # to get name
        vendor_name = vendor_disabled_df['Vendor Name'].loc[vendor_disabled_df['Vendor Name'] == vendor]
        vendor_name = vendor_name.tolist()

        # to get email id
        vendor_email = vendor_disabled_df['Vendor Email'].loc[vendor_disabled_df['Vendor Name'] == vendor]
        vendor_email = vendor_email.tolist()

        # to get vendor shop status
        vendor_shop_status = vendor_disabled_df['Vendor Shop Status'].loc[vendor_disabled_df['Vendor Name'] == vendor]
        vendor_shop_status = vendor_shop_status.tolist()

        # to get vendor commission status
        vendor_commission_status = vendor_disabled_df['Commission Status'].loc[vendor_disabled_df['Vendor Name'] == vendor]
        vendor_commission_status = vendor_commission_status.tolist()

        # to get vendor phone number will come soon

        # to get vendor categories
        vendor_categories = vendor_disabled_df[cat_list].loc[vendor_disabled_df['Vendor Name'] == vendor]

        vendor_categories = vendor_categories.dropna(axis=1, inplace=False)

        st.header('VENDOR IMFORMATION:')

        with st.spinner(text = "Please Wait"):
            
            time.sleep(0.5)

        col1, col2, col3, col4 = st.columns([8,1,1,4])

        col2.empty()
        col3.empty()

        with col1:
            st.subheader('Vendor Name:')
            st.text(' '.join(vendor_name))
            break_loop()

        with col4:
            st.subheader('Vendor Email:')
            st.text(' '.join(vendor_email))
            break_loop()

        with col1:
            st.subheader('Vendor Shop Status:')
            st.text(' '.join(vendor_shop_status))

        utils.break_loop_vendor_viewer()

        st.header('COMMISSION RATE & CATEGORIES:')

        st.subheader('Commission Status:')
        st.text(' '.join(vendor_commission_status))
        break_loop()
        
        st.subheader('Commission Categories')
        vendor_categories = vendor_categories.reset_index(drop=True)
        st.dataframe(vendor_categories)