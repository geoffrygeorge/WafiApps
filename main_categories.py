"""importing pandas framework"""
import pandas as pd

def main_categories():
  
    """defining function for main categories"""

    cat_list = [
        'Supermarket',
        'Watches',
        'Appliances',
        'Kitchen & Dining',
        'Health & Beauty',
        'Electronics',
        'Computers & IT',
        'Tools & DIY',
        'Office Supplies',
        'Mobiles & Tablets',
        'Toys & Games',
        'Perfumes & Fragrances',
        'Fashion',
        'Luggage & Travel Gear',
        'Pharmacy',
        'Baby Care',
        'Cakes & Flowers',
        'Home Decor & Furnishing',
        'Musical Instruments',
        'Gaming & Consoles',
        'Diet & Nutrition',
        'Furniture & Storage',
        'Automotive',
        'Home Improvement & Lighting',
        'School Essential',
        'Telecom',
        'Pet Supplies'
        ]

    list_df = pd.DataFrame(cat_list, columns = ['category_list'])

    return list_df