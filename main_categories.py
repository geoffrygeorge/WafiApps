"""importing pandas framework"""
import pandas as pd

def main_categories():
 
    """defining function for main categories"""

    cat_list = [
        'Electronics',
        'Computers & IT',
        'Mobiles & Tablets',
        'Perfumes & Fragrances',
        'Appliances',
        'Toys & Games',
        'Fashion',
        'Health & Beauty',
        'Luggage & Travel',
        'Baby Care',
        'Tools & DIY',
        'Supermarket',
        'Pet Supplies',
        'Telecom',
        'Cakes & Flowers',
        'Office Supplies',
        'Diet & Nutrition',
        'Pharmacy',
        'Automotive',
        'Musical Instruments',
        'Gaming & Consoles',
        'Watches',
        'School Essential',
        'Kitchen & Dining',
        'Home Decor & Furnishing',
        'Home Improvement & Lighting',
        'Furniture & Storage'
        ]

    list_df = pd.DataFrame(cat_list, columns = ['category_list'])

    return list_df