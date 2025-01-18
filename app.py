import streamlit as st
from dotenv import load_dotenv
from modules.get_pdf_text import get_pdf_text 
from modules.get_text_chunks import get_text_chunks 
from modules.get_vector_store import get_vector_store
from modules.get_conversation_chain import get_conversation_chain



def main():
    load_dotenv()
    
    st.set_page_config(page_title="Chat with your PDFs" , page_icon = ':books:')
    
    st.header('Chat with your PDFs :books:')
    st.text_input('Ask a question about your PDF')
    
    
    with st.sidebar:
        st.subheader('Your PDFs')
        pdf_docs =  st.file_uploader('Upload your PDFs here and click on process' , accept_multiple_files=True)
        if st.button('process'):
            with st.spinner('processing'):
                # get the pdf text 
                
                raw_text = get_pdf_text(pdf_docs)
                # st.write(raw_text)
                
                
                # get the text chunks
                text_chunks =  get_text_chunks(raw_text)
                st.write(text_chunks)
                
                # create vector store  
                vector_store = get_vector_store(raw_text)       
                
                # Conversation Chain
                conversation = get_conversation_chain(vectors_store)


if __name__ == '__main__':
    main()