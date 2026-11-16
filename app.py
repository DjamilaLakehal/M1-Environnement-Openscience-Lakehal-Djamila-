import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Tableau de bord interactif : Donnees biologiques")

df = sns.load_dataset("iris")

espece = st.selectbox(
"Choisir une espece :",
df["species"].unique()
)

data_filtre = df[df["species"] == espece]

st.write("Donnees filtrees :", data_filtre)

st.bar_chart(data_filtre[["sepal_length", "sepal_width"]])
