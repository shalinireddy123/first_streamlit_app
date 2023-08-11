import streamlit
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard boiled free range egg')
streamlit.text('🥑🍞Avocado toast')
streamlit.header('🍌🥭 Build your own fruit smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_first_list=my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.Fruit),['Avocado','Strawberries'])
#fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_selected)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response= requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice) 
  fruityvice_normalized  = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choice=streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
            streamlit.error()
                  
streamlit.stop()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
  my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row= get_fruit_load_list()
  streamlit.dataframe(my_data_row)

fruit_add=streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding'+ fruit_add)

my_cur.execute("insert into fruit_load_list values('from streamlist')")
