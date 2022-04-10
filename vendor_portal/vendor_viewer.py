import streamlit as st
import pandas as pd
import time

def vendor_viewer_main():

    def break_loop():
        i = 0
        while i < 5:
            st.markdown('<p></p>', unsafe_allow_html = True)
            i += 1
    
    # data transformation
    vendor_df = pd.read_csv('data/vendors.csv')
    vendor_df = vendor_df.sort_values(by = ['Vendor Name'])
    vendor_df = vendor_df.reset_index(drop=True)
    vendor_df = vendor_df.drop('Disapproval Reason', axis = 1)
    vendor_list = vendor_df['Vendor Name'].unique().tolist()

    with st.sidebar.expander('VENDOR LIST', expanded = True):
        vendor = st.radio('Choose Vendor :', vendor_list)

    st.title('VENDOR IMFORMATION :')

    with st.spinner(text = "Please Wait"):

                time.sleep(0.5)

    # to get name
    vendor_name = vendor_df['Vendor Name'].loc[vendor_df['Vendor Name'] == vendor]
    vendor_name = vendor_name.tolist()

    # to get email id
    vendor_email = vendor_df['Vendor Email'].loc[vendor_df['Vendor Name'] == vendor]
    vendor_email = vendor_email.tolist()

    # to get vendor status
    vendor_status = vendor_df['Vendor Status'].loc[vendor_df['Vendor Name'] == vendor]
    vendor_status = vendor_status.tolist()

    # to get vendor shop status
    vendor_shop_status = vendor_df['Vendor Shop Status'].loc[vendor_df['Vendor Name'] == vendor]
    vendor_shop_status = vendor_shop_status.tolist()

    # with st.expander('Dataframe'):
    #    st.dataframe(vendor_df)

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
        st.subheader('Vendor Status:')
        st.text(' '.join(vendor_status))

    with col4:
        st.subheader('Vendor Shop Status:')
        st.text(' '.join(vendor_shop_status))