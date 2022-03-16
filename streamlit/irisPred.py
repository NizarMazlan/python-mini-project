import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App

This app will predict the Iris flower type
""")


st.sidebar.header('User Input Parameters')
#ada sidebar punya ni 

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4) #1st
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4) #2nd
    petal_length = st.sidebar.slider('Petal Lenght', 1.0, 6.9, 1.3) #3rd
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2) #4th

    data = {'sepal_lenght': sepal_length,
            'sepal_width': sepal_width,
            'petal_lenght': petal_length,
            'petal_width': petal_width}

    features = pd.DataFrame(data, index = [0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

iris = datasets.load_iris()
#load the iris data

X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)

prediction_clf = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction_clf])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)