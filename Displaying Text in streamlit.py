import streamlit as st
import pandas as pd
import numpy as np


#Text/title
st.title('Welcome Collobrative learning team')

#Header/Subheader
st.header('Hello everyone is this our first app using streamlit')

#Sub-header
st.subheader("this is sub-header")


#Text
st.text("Hello, Streamlit")

#markdown
st.markdown("#This is a markdown")
st.markdown("##This is a markdown")
st.markdown("##This is a markdown")

#Caption
#st.caption('This is a string that explains something above.')

#Display code in app
code = '''def hello():
...     print("Hello, Streamlit!")'''
st.code(code, language='python')

#Error / Colorful text 
# success
st.success("Success")
# success
st.info("Information")
# success
st.warning("Warning")
# success
st.error("Error")


#Display mathematical expressions formatted as LaTeX.
st.latex(r'''
...     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

#How to create a file selector
#import streamlit as st
#import os

#def file_selector(folder_path='.'):
#    filenames = os.listdir(folder_path)
#    selected_filename = st.selectbox('Select a file', filenames)
#    return os.path.join(folder_path, selected_filename)

#filename = file_selector()
#st.write('You selected `%s`' % filename)




