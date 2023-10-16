import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Imon International's Bank scoring system",
    page_icon='🏦',
    layout="wide", 
    initial_sidebar_state="expanded", 
)

st.subheader('Imon International Bank scoring')

model_selected = st.radio('What analysis do you want to use', ('LogisticRegression', 'DecisionTreeClassifier', 'RandomForestClassifier(without options)',  'RandomForestClassifier(with options)', 'Default'))



if model_selected == 'DecisionTreeClassifier':
    pickle_in = open("scoring_imon_ModelTree.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['LogisticRegression', 'Default']:
    pickle_in = open("scoring_imon_LogReg.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(with options)':
    pickle_in = open("scoring_imon_Forest(par).pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(without options)':
    pickle_in = open("scoring_imon_Forest.pkl","rb")
    classifier=pickle.load(pickle_in)

                     
                     
def predict_note_authentication(Age, Issue_amount_nominal, Term, Age_full_years, Family_status, Type_of_client, Education, Tupe_of_business):
    prediction=classifier.predict([[Age, Issue_amount_nominal, Term, Age_full_years, Family_status, Type_of_client, Education, Tupe_of_business]])
    print(prediction)
    return prediction
                     
                     
def main():
    st.title("Imon International's Bank scoring system")
    Age = st.radio('Ваш пол?(0 - male, 1 - female)', (0, 1))
    Issue_amount_nominal = st.number_input('Какова сумма выдочи номинала(используйте только цифры)?', step=1, value=0)
    Term = st.number_input('На какой срок вы хотите кредит?(используйте только цифры)?', step=1, value=0) 
    Age_full_years = st.number_input('Сколько вам полных лет?(используйте только цифры)?', step=1, value=0)
    Family_status = st.radio('Каков ваш семеный статус?(0 - Widow/Widower, 1 - Single, 2 - Married, 3 - Divorced)', (0, 1, 2, 3))
    Type_of_client = st.radio('Какой вы клиент?(0 - Старый клиент, 1 - Новый клиент)', (0, 1))    
    Education = st.radio('Какое у вас образование?(0 - Высшее образование, 1 - Сред.спец.образ-ние, 2 - Среднее образование, 3 - Непол Сред.образ, 4 - Начал образование, 5 - Аспирантура)', (0, 1, 2, 3, 4, 5))
    Tupe_of_business = st.radio('Какой у вас вид бизнеса?(0 - 1. Карзи истеъмоли/Потребительский кредит, 1 - 2. Истехсолот/Производство, 2 - 6. Хочагии кишлок / Сельское хозяйство, 3 - 3. Хизматрасони/Услуги, 4 - 4. Савдо / Торговля)', (0, 1, 2, 3, 4)) 
                     
    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(Age, Issue_amount_nominal, Term, Age_full_years, Family_status, Type_of_client, Education, Tupe_of_business)) 
     #st.success('The output is {}'.format(result))
    st.success('Scoring system result is(1 - Длительность самой долгой единовременной просрочки в течение цикла > 20, 0 - Scoring system result is(1 - Длительность самой долгой единовременной просрочки в течение цикла <= 20) {}'.format(result))
                     
    
    if st.button("About program"):
        st.text("Bank scoring is an evaluation system used by banks and financial institutions to determine the viability of a client to receive a loan, credit, mortgage or insurance. It comprises a series of economic, demographic and financial data of the person.")
        st.text("Built by Aziz Rasulov")
              
                  
if __name__=='__main__':
    main()

   