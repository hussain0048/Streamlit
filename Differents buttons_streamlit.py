import streamlit as st
import pandas as pd
import numpy as np


#Check Box
#Display a checkbox widget.
agree = st.checkbox('I agree')
if agree:
   st.write('Great!')
   

#Radio Button
#Display a radio button widget.

genre = st.radio(
  "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")


#selectbox
#Display a select widget.

option = st.selectbox(
 'How would you like to be contacted?',
 ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)


#Multiselect 
#Display a multiselect widget.
#The multiselect widget starts as empty.

options = st.multiselect(
'What are your favorite colors',
['Green', 'Yellow', 'Red', 'Blue'],
['Yellow', 'Red']
)
st.write('You selected:', options)


#Button
#Display a button widget.

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
     
     
#Input_Text
#Display a single-line text input widget.

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


#Slider
#Display a slider widget.

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')