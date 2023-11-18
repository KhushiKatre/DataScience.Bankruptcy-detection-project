# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:26:06 2023

@author: katre
"""


import pickle
import streamlit as st

file = open('svm2_linear.pkl','rb')
model = pickle.load(file)


def predict(ir,mr,ff,cr,co,opr):
    prediction = model.predict([[ir,mr,ff,cr,co,opr]])
    return prediction

def main():
    st.title('BANK DATA')
    st.title(':red[(BANKRUPTCY DETECTION SYSTEM)]')
    
    ir = st.number_input('Industry_risk: ')
    mr = st.number_input('Management_risk: ')    
    ff = st.number_input('Financial_Flexibility: ')
    cr = st.number_input('Credibility: ')
    co = st.number_input('Competitiveness: ')
    opr = st.number_input('Operating_risk: ')
  
    
    
    
    if st.button('Predict'):
     result = predict(ir,mr,ff,cr,co,opr)
     if result==0:
         st.success("BANKRUPT")
     else:
         st.success("NOT A BANKRUPT")
         
         
         
if __name__ == '__main__':
    main()        
    