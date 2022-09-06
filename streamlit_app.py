import streamlit
import pandas as pd

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
