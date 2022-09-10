import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

# New section to display Fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

def get_fruityvice_data(this_fruit_choice):
  # streamlit.write('The user entered ', fruit_choice)
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  # streamlit.text(fruityvice_response.json())

  # Normalize json object
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

try:
  # Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  
  if not fruit_choice:
    streamlit.error("Please select a fruit to get the information")
  else:
    
    # Display normalized json
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

# Stop steramlit for debugging
# streamlit.stop()

# Snowflake connector

# Snowflake related fucntions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

# Allow the user to add a fruit to th elist
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write("Thanks for adding ", add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
