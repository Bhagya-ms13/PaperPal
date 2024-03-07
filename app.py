import streamlit as st
import pickle
import pandas as pd
def recommend(res):
    res_index = research[research['titles']==res].index[0]
    distances = similarity[res_index]
    research_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    recommended_research = []
    for i in research_list:
        recommended_research.append(research.iloc[i[0]].titles)
    return recommended_research
research_dict = pickle.load(open('research_dict.pkl','rb'))
research = pd.DataFrame(research_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Reasearch Paper Recommender')

selected_research_name = st.selectbox('Enter the name of the research paper',research['titles'].values)
if st.button('Recommend'):
    recommendations = recommend(selected_research_name)
    for i in recommendations:
         st.write(i)
