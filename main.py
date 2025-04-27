import os
import boto3
import streamlit as st
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.llms import Bedrock
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# ------------------ Bedrock Client Setup ------------------

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
)

# ------------------ Model and Embedding Setup ------------------

bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v1",
    client=bedrock_client,
)

def get_llm():
    return Bedrock(
        model_id="amazon.titan-text-lite-v1",
        client=bedrock_client,
        model_kwargs={"temperature": 0.7},
    )

# ------------------ Prompt Template ------------------

prompt_template = """
Human: Use the following pieces of context to provide a detailed answer to the question at the end.
Summarize with at least 200 words and avoid making up information.
<context>
{context}
</context>
Question: {question}
Assistant:
"""

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

# ------------------ Document Handling ------------------

def load_documents():
    if not os.path.exists("pdf-data") or not os.listdir("pdf-data"):
        raise ValueError("No documents found in the 'pdf-data/' folder. Please add PDFs first.")

    loader = PyPDFDirectoryLoader("pdf-data")
    documents = loader.load()

    if not documents:
        raise ValueError("No documents loaded. Check your PDF files.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)

    if not docs:
        raise ValueError("Document splitting failed. No text found.")

    return docs

# ------------------ Vectorstore Handling ------------------

def create_vector_store(docs):
    if not docs:
        raise ValueError("No documents to create vector store.")
    
    vectorstore = FAISS.from_documents(docs, bedrock_embeddings)
    vectorstore.save_local("faiss_index")

def load_vector_store():
    if not os.path.exists("faiss_index/index.faiss"):
        raise FileNotFoundError("Vector store not found. Please store vectors first.")
    
    return FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)

# ------------------ QA Chain ------------------

def ask_question(llm, vectorstore, query):
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    result = qa({"query": query})
    return result["result"]

# ------------------ Streamlit Frontend ------------------

def main():
    st.set_page_config(page_title="End to End RAG Demo", layout="centered")
    st.title("📚 End-to-End Bedrock RAG Application")

    with st.sidebar:
        st.header("🔧 Manage Vector Store")
        if st.button("Store Vector"):
            try:
                with st.spinner("Processing PDFs and creating vector store..."):
                    docs = load_documents()
                    create_vector_store(docs)
                    st.success("✅ Vector store created successfully!")
            except Exception as e:
                st.error(f"Error: {str(e)}")

    user_question = st.text_input("Ask a question about your documents:")

    if user_question:
        if not os.path.exists("faiss_index/index.faiss"):
            st.warning("⚠️ Please click 'Store Vector' first to create vector index.")
        else:
            if st.button("Send"):
                try:
                    with st.spinner("Searching best answers..."):
                        vectorstore = load_vector_store()
                        llm = get_llm()
                        response = ask_question(llm, vectorstore, user_question)
                        st.success("✅ Response generated successfully!")
                        st.markdown(response)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
