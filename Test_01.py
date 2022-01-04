import streamlit as st
import pandas as pd
import numpy as np
import datetime



#Checkbox
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

  
#Radio Button
genre = st.radio(
"What's your favorite movie genre",
('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")
    

#Selection Box
option = st.selectbox(
'How would you like to be contacted?',
('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)


#Multi-Select box
options = st.multiselect(
'What are your favorite colors',
['Green', 'Yellow', 'Red', 'Blue'],['Yellow', 'Red'])
st.write('You selected:', options)


#Button
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')


#Text Input
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


#Slider
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


#And here's an example of a range slider:
values = st.slider(
'Select a range of values',
0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

#Display a date input widget.
d = st.date_input(
"When's your birthday",
datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

#input_date
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)