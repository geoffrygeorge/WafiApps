import streamlit as st
import utils
from vendor_portal import vendor_viewer

def authenticate():
    def is_authenticated(password):
        return password == "WD2qj&VAUTJ9f%m"


    def generate_login_block():
        block1 = st.empty()
        block2 = st.empty()

        return block1, block2


    def clean_blocks(blocks):
        for block in blocks:
            block.empty()


    def login(blocks):
        blocks[0].markdown("""
                <style>
                    input {
                        -webkit-text-security: disc;
                    }
                </style>
            """, unsafe_allow_html=True)

        return blocks[1].text_input('Password :')


    login_blocks = generate_login_block()
    password = login(login_blocks)

    if is_authenticated(password):

        clean_blocks(login_blocks)

        utils.main_heading_text_vendor()

        utils.break_loop_vendor_viewer()
       
        vendor_viewer.vendor_viewer_main()

    elif password:
        st.error("Please enter a valid password")