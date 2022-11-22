import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("SreeGaya's New Healthy Diner")

streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍞 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Cage Egg')
streamlit.text('🥑 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected =streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)                    

#New Section to display fruityvice api response
#streamlit.header('Fruityvice Fruit Advice !')
#fruit_choice= streamlit.text_input('What fruit would you like information about?', 'Kiwi')
#streamlit.write('The User Entered', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# Take the json version of the response and normalize it
# streamlit.text(fruityvice_response.json())
# Take the json version of the response and normalise it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
# streamlit.dataframe(fruityvice_normalized)

#New Section to display fruityvice api response
#streamlit.header('Fruityvice Fruit Advice !')
#try:
 #   fruit_choice = streamlit.text_input('What fruit would you like information about?')
 #   if not fruit_choice:
 #      streamlit.error("Please select a fruit to get information")
  #  else:
   #         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
   #         fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   #         streamlit.dataframe(fruityvice_normalized)
#except URLError as e:
 #       streamlit.error()
    
 #Create the repeatable code block (callea a function)
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
   fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice !')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
        
except URLError as e:
   streamlit.error()
      
#streamlit.write('The User Entered', fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
# Take the json version of the response and normalize it
# streamlit.text(fruityvice_response.json())
# Take the json version of the response and normalise it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table
# streamlit.dataframe(fruityvice_normalized)


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchall()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
streamlit.header("The frut load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
   
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
   my_cnx = my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)

#streamlit.dataframe(my_data_row)

#streamlit.header("What fruit would you like to add?:")
#fruit_entered= streamlit.text_input('What fruit would you like to add', 'Kiwi')
#streamlit.write('The User Entered ', fruit_entered)
# streamlit.write("Thanks for adding: " fruit_entered)
#my_cur.execute("insert into fruit_load_list values('from stremlit')")
#
# Allow the end user to add fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values('from stremlit')")
         return "Thanks for adding "+ new_fruit

ass_my_fruit = streamlit.text('What fruit would you like to add?:', 'kiwi')
if streamlit.button('Add a Fruit to the List'):
   My_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)
