from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_google_genai import  ChatGoogleGenerativeAI
import os

def get_conversation_chain(vectore_store):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro" , 
                                 api_key=os.environ["GEMINI_API_KEY"])
    memory = ConversationBufferMemory(memory_key='Chat_history' , return_messages=True)
    
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm= llm,
        retriever= vectore_store.as_retriever(),
        memory = memory
    )
    
    return conversation_chain