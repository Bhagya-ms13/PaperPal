import streamlit as st
import fitz  # PyMuPDF
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import pandas as pd
import re
import pickle

def extract_text_from_pdf(pdf_bytes):
    text = ""
    with fitz.open("temp.pdf", stream=pdf_bytes) as pdf_file:
        for page_num in range(len(pdf_file)):
            page = pdf_file.load_page(page_num)
            text += page.get_text()
    return text

def split_text_by_headings(text):
    # Split the text into sections based on headings
    sections = re.split(r'\n[A-Z\s]+\n', text)
    return sections

def summarize_sections(sections, num_sentences=3):
    summarizer = LsaSummarizer()
    summaries = []
    for section in sections:
        parser = PlaintextParser.from_string(section, Tokenizer("english"))
        summary = summarizer(parser.document, num_sentences)
        summary_text = " ".join([str(sentence) for sentence in summary])
        summaries.append(summary_text)
    return summaries

def summarize_pdf(pdf_bytes):
    pdf_text = extract_text_from_pdf(pdf_bytes)
    sections = split_text_by_headings(pdf_text)
    summaries = summarize_sections(sections)
    return summaries

def recommend(res, research, similarity):
    res_index = research[research['titles'] == res].index[0]
    distances = similarity[res_index]
    research_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_research = []
    for i in research_list:
        recommended_research.append(research.iloc[i[0]].titles)
    return recommended_research

# Load research data
research_dict = pickle.load(open('research_dict.pkl', 'rb'), encoding='latin1')
research = pd.DataFrame(research_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'), encoding='latin1')

# Streamlit app
st.set_page_config(page_title="Research Paper Recommender & PDF Summarizer")

# Header
st.title('Research Paper Recommender & PDF Summarizer')

# Sidebar
st.sidebar.title('Choose an Option')
option = st.sidebar.radio('', ('PDF Summarizer', 'Research Paper Recommender'))

if option == 'PDF Summarizer':
    st.subheader('PDF Summarizer')
    st.info('Upload a PDF file to summarize its content.')

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        try:
            summaries = summarize_pdf(uploaded_file.read())
            st.success("PDF Summarized Successfully!")
            st.write("\n\n".join(summaries))
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

elif option == 'Research Paper Recommender':
    st.subheader('Research Paper Recommender')
    selected_research_name = st.selectbox('Enter the name of the research paper', research['titles'].values)
    
    if st.button('Recommend'):
        recommendations = recommend(selected_research_name, research, similarity)
        st.success("Recommended Research Papers:")
        for i in recommendations:
            st.write(i)
