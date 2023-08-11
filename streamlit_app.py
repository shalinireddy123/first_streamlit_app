import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard boiled free range egg')
streamlit.text('🥑🍞Avocado toast')
streamlit.header('🍌🥭 Build your own fruit smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_first_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.Fruit),['Avocado','Strawberries'])
#fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_selected)
import requests
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
 
