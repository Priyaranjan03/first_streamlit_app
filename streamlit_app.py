import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('Hello! i just started learning')

streamlit.header('🥣 🥗 Breakfast Menu 🥑🍞')
streamlit.text('🐔 🥑🍞Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 🍞Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('List of Fruits')

my_fruit_list = my_fruit_list.set_index('Fruit')
#Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avacodo','strawberries'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


