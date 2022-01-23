import streamlit as st
import pickle
import numpy as np
import pandas as pd

m=pickle.load(open('model.pkl','rb'))
path = r'C:\\Users\\AIDEN SAMUEL\\Desktop\\Data\\AIML_Dataset.csv'
df = pd.read_csv(path)

st.dataframe(df)

def predict_fraud():
    # prediction=model.predict_proba(input)
    # pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return st.dataframe(df.head())

def main():
    st.title("Financial Management System by Runtime Terror")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Fraud Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    txn_id = st.text_input("Transaction_id","Type Here")

    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Transaction is not a Fraud</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Transaction is a fraud</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_fraud()
        # st.success('The probability of fraud taking place is {}'.format(output))
        # if output > 0.5:
        #     st.markdown(danger_html,unsafe_allow_html=True)
        # else:
        #     st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()