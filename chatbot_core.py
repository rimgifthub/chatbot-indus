from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_db(pdf_path):
    loader=PyPDFLoader(pdf_path)
    docs=loader.load()
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks=splitter.split_documents(docs)
    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db=FAISS.from_documents(chunks,embeddings)

    return db, chunks 
db,chunks=build_db("industry-4-0.pdf")
db.save_local("industry4_index")

from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama

llm = Ollama(model="gemma:2b", temperature=0, num_predict=150) 

qa_chain = RetrievalQA.from_chain_type(llm=llm,chain_type="stuff",retriever=db.as_retriever(search_kwargs={"k": 3}),return_source_documents=False)


def search_function(query, db, k=3):
    if not query.strip():
        return[]
    results=db.similarity_search(query, k)
    return[r.page_content for r in results]



def generate_answer(query,db):
    top_chunks = search_function(query, db, k=3)
    context = " ".join(top_chunks)
    prompt = f"Answer the question using this context:\n{context}\nQuestion: {query}"

    return qa_chain.run(query)