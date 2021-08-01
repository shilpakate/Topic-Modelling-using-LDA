#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st 
import pandas as pd
from pickle import dump
from pickle import load
from PIL import Image
import sklearn
import base64
from sklearn.feature_extraction.text import CountVectorizer
import pickle

CV = CountVectorizer(stop_words="english")

from load_css import local_css

local_css("D:/Project 3/style.css")

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        padding-top: 0rem;
    }}
   
</style>
""",
        unsafe_allow_html=True,
    )

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    width: auto;
    height: auto;
    }
  }
    
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
                                      
set_background('D:/Project 3/pic2.jpeg')                          


col1, col2 = st.beta_columns(2)

names = "<div><span class='blue_heading'>Topic Modelling</span></div>"
col1.markdown(names, unsafe_allow_html=True)

image = Image.open('D:/Project 3/excelr.png')
col2.image(image, caption=None, width=200, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

names = "<div><span class='blue'>Group5 </span></div>"
st.markdown(names, unsafe_allow_html=True)
st.header("Topic Modelling Definition:")
st.markdown(''' Topic modeling is an unsupervised machine learning technique that's capable of scanning a set of documents, detecting word and phrase patterns within them, and automatically clustering word groups and similar expressions that best characterize a set of documents.''')
st.header("Importance of Topic Modelling:")
st.markdown('''Topic modelling provides us with methods to organize, understand and summarize large collections of textual information. It helps in: Discovering hidden topical patterns that are present across the collection. Annotating documents according to these topics.''')
st.header("LDA-Latent Dirichlet Allocation:")
st.markdown('''It is one of the most popular topic modeling methods. Each document is made up of various words, and each topic also has various words belonging to it. The aim of LDA is to find topics a document belongs to, based on the words in it.''')

sentence = st.text_area("Input your sentence here:")
#sentence = st.text_input('Input your sentence here:')
sentence1 = [sentence]
#loaded_model = load(open("model.pickle", 'rb'))
loaded_model = load(open('D:/Project 3/mo.pkl', 'rb'))




if(len(sentence)!=0):
    prediction = loaded_model.predict(sentence1)
    if(prediction==0): col1.markdown("<div><span class='purple'>TOPIC - Religion</span></div>",unsafe_allow_html=True)
    if(prediction==1): col1.markdown("<div><span class='purple'>TOPIC - Sport-Hockey</span></div>",unsafe_allow_html=True)
    if(prediction==2): col1.markdown("<div><span class='purple'>TOPIC - Motarcycle-Bike</span></div>",unsafe_allow_html=True)

