#PaperPal
#Stack Used:

  Language: Python
  Libraries:
	Streamlit for the web app interface.<br />
	Tkinter for the desktop app interface.<br />
	Pandas for data manipulation.<br />
	PyMuPDF for PDF text extraction.<br />
	Sumy for text summarization.<br />
  Datasets used:
	https://www.kaggle.com/datasets/spsayakpaul/arxiv-paper-abstracts/data<br />

#Description:
This project is a tool that serves as both a research paper recommendation system and a text summarization tool. It offers a streamlined interface for users to interact with. The research paper recommendation<br />feature allows users to input a research paper's name and receive recommendations for similar papers. This is achieved using a precomputed similarity matrix and a straightforward recommendation algorithm.<br />

Additionally, the tool offers a text summarization feature for PDF files. Users can upload a PDF file, and the tool will extract text from the PDF, split it into sections based on headings, and summarize each <br />section using the LsaSummarizer algorithm. This feature is useful for quickly getting an overview of the content of a lengthy document.<br />

Overall, this project provides a convenient and efficient way for users to explore research papers and summarize text, making it a valuable tool for researchers, students, and anyone dealing with large amounts of<br /> textual data.
