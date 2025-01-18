import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS 


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004" ,
                                              google_api_key =os.environ["GEMINI_API_KEY"] )
    
    vectors_store = FAISS.from_texts(texts= text_chunks , 
                                   embedding= embeddings
                                   )
    
    # Conversation Chain
    conversation = get_conversation_chain(vectors_store)
    
    
    
    return vectors_store


# get_vector_store('text-embedding-')