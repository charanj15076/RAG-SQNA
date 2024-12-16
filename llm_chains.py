# from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import LLMChain 
# from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_chroma import Chroma
from prompt_template import memory_prompt_template, pdf_chat_prompt
from langchain.llms.bedrock import Bedrock
from langchain_community.embeddings import BedrockEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import boto3
import chromadb
import yaml
import streamlit as st




with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)


#connection to aws bedrock (ivoking bedrock-runtime client)
bedrock_client = boto3.client(service_name="bedrock-runtime")


#Normal chain loads mistral7b
def create_llm(model_path = config["model_path"]["large"], model_type = config["model_type"], model_config = config["model_config"]):
    llm = CTransformers(model = model_path,model_type = model_type, config = model_config)
    return llm

#pdf chain loads LLAMA3 from aws bedrock
def get_rag_llm():
    llm = Bedrock(model_id = "meta.llama3-8b-instruct-v1:0", client = bedrock_client,
                  model_kwargs = {'max_gen_len':512})
    return llm

#converts user query to embeddings
def create_embeddings(embeddings_path = config["embeddings_path"]):
    return HuggingFaceEmbeddings(model_name=embeddings_path)

#chat history for context
def create_chat_memory(chat_history):
    return ConversationBufferWindowMemory(memory_key = "history", chat_memory = chat_history, k = 1)

def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)

def create_prompt_from_template_rag(template):
    return PromptTemplate.from_template(template)

def create_llm_chain(llm, chat_prompt, memory):
    return LLMChain(llm = llm, prompt = chat_prompt, memory = memory)


def load_normal_chain(chat_history):
    return chatChain(chat_history)

# function to create chroma db

def load_vectordb(embeddings):
    persistent_client = chromadb.PersistentClient("chroma_db")
    langchain_chroma = Chroma(
        client = persistent_client,
        collection_name = 'pdfs',
        embedding_function = embeddings,
    )
    return langchain_chroma

def load_pdf_chat_chain(chat_history):
    return pdfChatChain(chat_history)


def get_response(llm,vectorstore):
    ## create prompt / template
    prompt_template = """

    Human: Please use the given context to provide concise answer to the question
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    <context>
    {context}
    </context>

    Question: {question}

    Assistant:"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "human_input"]
    )

    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 5}
    ),
    chain_type_kwargs={"prompt": PROMPT} 
    )
    return qa



class chatChain:

    def __init__(self,chat_history):
        self.memory = create_chat_memory(chat_history)
        llm = create_llm()
        chat_prompt = create_prompt_from_template(memory_prompt_template)
        self.llm_chain = create_llm_chain(llm,chat_prompt,self.memory)
    
    def run(self,user_input):
        return self.llm_chain.run(human_input = user_input,history = self.memory.chat_memory.messages, stop=["Human:"])
    



class pdfChatChain:
    def __init__(self,chat_history):
        self.memory = create_chat_memory(chat_history)
        self.vector_db = load_vectordb(create_embeddings())
        chat_prompt = create_prompt_from_template(pdf_chat_prompt)
        llm = get_rag_llm()
        # chat_prompt = create_prompt_from_template(memory_prompt_template)
        self.llm_chain = get_response(llm = llm , vectorstore=self.vector_db)

    def run(self, user_input):
        print("PDF chat chain is running.....")
        answer=self.llm_chain({"query":user_input})
        print(answer)
        
        return answer['result']