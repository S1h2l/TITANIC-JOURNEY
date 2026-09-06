import streamlit as st
import pandas as pd

st.title("PASSENGER SURVIVAL CHANCE IN THE TITANIC JOUNRNEY")

pclass =st.slider("ENTER THE PASSENGER CLASS FOR THE USER ",1,3)
sex =st.selectbox("ENTER THE PASSENGER GENDER ",['MALE','FEMALE'])
sibsp=st.slider("ENTER THE PASSENGER SIBLING AND SPOUSE",1,8)
parch = st.slider("ENTER THE PASSENGER TOTAL NUMBER OF PARENTS AND CHILD ",0,6)
fare =st.number_input("ENTER THE FARE OF THE PASSENGER ")
st.number_input("ENTER THE FARE OF THE PASSENGERS")
embarked = st.selectbox(
    "ENTER THE PASSENGER STATION FROM WHERE THEY STARTED THE JOURNEY",
    ["C", "Q", "S"]
)

data = pd.DataFrame([{'Pclass':pclass,'sex':sex,'Sibsp':sibsp,'Parch':parch,'Fare':fare,'Embarked':embarked}])

if st.button('data'):

    st.write(data)