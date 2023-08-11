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
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice=streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered fruit_choice')
import requests
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


fruityvice_normalized  = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector 
#my_cur=my_cnx.cursor()
#my_cur.execute("SELECT current_user()current_account()current_region()")
#my_data_row=my_cur.fetchone()
#streamlit.text("Hello from snowflake:")
#streamlit.text(my_data_row)
