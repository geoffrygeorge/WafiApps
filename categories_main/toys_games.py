import streamlit as st
import time


def toys_games_main():

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