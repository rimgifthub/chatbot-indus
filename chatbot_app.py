
import streamlit as st 

from chatbot_core import build_db, generate_answer
import tempfile 
import os 

st.set_page_config(page_title="INDUSTRY 4.0 Lab Chatbot ", page_icon="🤖")
st.title("Industry 4.0 Lab Chatbot")
st.write("Ask me anything about Industry 4.0 based on the lab documents")

st.markdown("### Try questions like:")
st.markdown("- what is Industry  4.0 ?")
st.markdown("what are the key components of Industry 4.0 ?")

uploaded_file = st.file_uploader("upload your Industry 4.0 file", type=["pdf"])




if uploaded_file :
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp :
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name
else:
    pdf_path = "industry-4-0.pdf"  


try: 
    with st.spinner("Processing Industry 4.0 documents ..."):
      db, chunks = build_db(pdf_path)



except Exception as e:
    st.error(f"Error loading documents: {e}")
    st.stop()



query = st.text_input("💬 Ask q question about industry 4.0")
if query:
    with st.spinner("Generating answer"):
        response = generate_answer(query)
    
    st.markdown("### Answer :")
    st.write(response)
    



    st.markdown("### Total chunks created")
    total_words = sum(len(chunk.page_content.split())for chunk in chunks)
    avg_words = total_words / len(chunks)
    st.write(f"Average words per chunk: {avg_words:.1f}")
    







