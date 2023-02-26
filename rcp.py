import streamlit as st
import random

st.header('Welcome to the game of rock,paper, scissors')
st.write("##")
st.subheader('choose 1 for rock, choose 2 for paper, choose 3 for scissors')



use = st.number_input('Insert a number', step = 1, key="sa", min_value=1, max_value=3)
computer = random.randint(1,4)
if(use == computer):
        st.subheader("its a draw")
if(use == 1 and computer == 3):
        st.subheader("computer choose scissors you win")
if(use == 1 and computer == 2):
        st.subheader("computer choose paper you lose")   
if(use == 2 and computer == 1):
        st.subheader("computer choose scissors you win")
if(use  == 2 and computer == 3):
        st.subheader("computer choose paper you lose")  
if(use  == 3 and computer == 1):
        st.subheader("computer choose scissors you lose")
if(use == 3 and computer == 2):
     st.subheader("computer choose paper you win")


