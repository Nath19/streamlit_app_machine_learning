import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as gost

df = pd.read_csv("https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv")
if st.checkbox('Show dataframe'): 
     st.write(df)
     st.write(df.shape)

def info_dataset():
    st.write('Shape :' ,df.shape)
    st.write('Types :' ,df.dtypes)

info_dataset()


species = st.multiselect('Show iris per variety?', df['variety'].unique())
col1 = st.selectbox('Which feature on x?', df.columns[0:4])
col2 = st.selectbox('Which feature on y?', df.columns[0:4])
new_df = df[(df['variety'].isin(species))]
st.write(new_df)
fig = px.scatter(new_df, x =col1,y=col2, color='variety')
st.plotly_chart(fig)



feature = st.selectbox('Which feature?', df.columns[0:4])
# Filter dataframe
new_df2 = df[(df['variety'].isin(species))][feature]
fig2 = px.histogram(new_df, x=feature, color="variety", marginal="rug")
st.plotly_chart(fig2)


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.svm import SVC

features = df[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].values
labels = df['variety'].values
X_train,X_test, y_train, y_test = train_test_split(features, labels, train_size=0.7, random_state=1)
alg = ['Decision Tree', 'Support Vector Machine']
classifier = st.selectbox('Which algorithm?', alg)

if classifier=='Decision Tree':
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    acc = dtc.score(X_test, y_test)
    st.write('Accuracy: ', acc)
    pred_dtc = dtc.predict(X_test)
    cm_dtc=confusion_matrix(y_test,pred_dtc)
    st.write('Confusion matrix: ', cm_dtc)
elif classifier == 'Support Vector Machine':
    svm=SVC()
    svm.fit(X_train, y_train)
    acc = svm.score(X_test, y_test)
    st.write('Accuracy: ', acc)
    pred_svm = svm.predict(X_test)
    cm=confusion_matrix(y_test,pred_svm)
    st.write('Confusion matrix: ', cm)