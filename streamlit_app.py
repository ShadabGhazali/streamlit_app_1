import streamlit
import pandas as pd
import requests

streamlit.title("Purani Dilli Healthy Diner")

streamlit.header("Naashta Paani")
streamlit.text("🍲Nihaari & 🫓Tandoori Roti")
streamlit.text("🍖Kabab & 🫓Paratha")
streamlit.text("🍳Half-Fried Free-Range Egg")
streamlit.text("🫖Chai, ☕️Coffee, 🥤Fruit Juice")

streamlit.header("🍒🍎🍇Build your own smoothie🍅🍌🥝")
fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Set fruit name column as index
fruit_list = fruit_list.set_index("Fruit")

# Add a user interactive widget called a Multi-select that will allow users to pick the fruits they want in their smoothies.
fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruit_list.index), ['Banana', 'Grapes', 'Watermelon'])
fruits_to_show = fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


streamlit.header("Fruityvice Fruit Advice!")
# Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?, 'kiwi')
streamlit.write('The user entered ', fruit_choice)                                    

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json())

# Normalize json object
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Display normalized json
streamlit.dataframe(fruityvice_normalized)
