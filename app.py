from tkinter import CENTER, Menu
from turtle import width
from click import style
import streamlit as st
st.title( 'Squence Prediction')

st.image('Seq2.jpeg',width= 800)

st.markdown("""
<h1>Description </hl>
<h3>Sequence prediction is a popular machine learning task, which consists of predicting the next symbol(s) based on the previously observed sequence of symbols. These symbols could be a number, an alphabet, a word, an event, or an object like a webpage or product. For example: A sequence of words or characters in a text. </h3>
<h3>Sequence-to-sequence prediction involves predicting an output sequence given an input sequence. For example: Given: 1, 2, 3, 4, 5. Predict: 6, 7, 8, 9, 10.</h3>
""",     unsafe_allow_html = True)


st.header('What is Sequence Prediction ?')
st.markdown("""
<h3>Sequence prediction is a popular machine learning task, which consists of predicting the next symbol(s) based on the previously observed sequence of symbols. These symbols could be a number, an alphabet, a word, an event, or an object like a webpage or product.</h3>

""",     unsafe_allow_html = True)

st.image('Seq.jpg', width= 300)
st.header('What is CPT?')
st.markdown("""
<h3>Compact Prediction Tree (CPT) is one such algorithm which I found to be more accurate than traditional Machine Learning model.</h3>

""",     unsafe_allow_html = True)
sidebar = st.sidebar
sidebar.header('Menu')
btn = sidebar.button("Home page")
btn1 = sidebar.button("Training")
btn2 = sidebar.button("Prediction")
btn3 = sidebar.button("Search")











