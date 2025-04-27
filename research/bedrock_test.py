from langchain_community.llms.bedrock import Bedrock
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import boto3
import streamlit as st


#Bedrock client
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1',

)
model_id = "amazon.titan-text-lite-v1"



# Initialize the Bedrock LLM
llm = Bedrock(
    model_id=model_id,
    client=bedrock_client,
    model_kwargs={"temperature": 0.9},
)

def my_cahtbot(language,user_text):
    
    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["language", "user_text"],
        template="You are a helpful assistant. You are a {language} expert. {user_text}",

    )
    bedrock_chain = LLMChain(llm=llm, prompt=prompt)
    response = bedrock_chain({'language':language, 'user_text':user_text})
    return response

st.title("Bedrock LLM Chatbot")

language = st.sidebar.selectbox("Lanuage",["english","Spanish","French","German"])

if language:
    user_text = st.sidebar.text_area(label="What is your question?", max_chars=100)

if user_text:
    response = my_cahtbot(language,user_text)
    st.write("Response:", response['text'])