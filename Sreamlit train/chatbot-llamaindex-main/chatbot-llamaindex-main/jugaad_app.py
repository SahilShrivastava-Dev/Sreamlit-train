import streamlit as st
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import os
from dotenv import load_dotenv
from haystack.document_store.faiss import FAISSDocumentStore
from haystack.retriever.dense import DensePassageRetriever
from haystack.reader.farm import FARMReader
from haystack.pipeline import ExtractiveQAPipeline

load_dotenv(override=True)

# save keys in .env file
OPENAI_KEY = os.getenv('OPENAI_API_KEY')
ENDPOINT = os.getenv('OPENAI_API_BASE')
OPENAI_VERSION = os.getenv('OPENAI_API_VERSION')

def init_page():
    st.set_page_config(page_title='Personal Chatbot', page_icon='mag_right')
    st.header('Knowledge Query Assistant')
    st.write("I'm here to help you get information from your file.")
    st.sidebar.title('Option')

def init_messages():
    clear_button = st.sidebar.button('Clear Conversation', key='clear')
    if clear_button or 'messages' not in st.session_state:
        st.session_state.messages = [
            SystemMessage(
                content='You are a helpful AI assistant. Reply your answer in markdown format.'
            )
        ]

def main():
    init_page()
    file = st.file_uploader('Upload file: ', type=['pdf', 'txt', 'docx'])
    if file is not None:
        with open(os.path.join('data', file.name), 'wb') as f: 
            f.write(file.getbuffer())        
        st.success('Saved file!')
        documents = [
            {"text": file.getvalue().decode("utf-8"), "meta": {"file_name": file.name}}
        ]

        # Initialize document store
        document_store = FAISSDocumentStore(
            faiss_index_factory_str="Flat",
            similarity="dot_product"
        )
        document_store.write_documents(documents)

        # Initialize retriever and reader
        retriever = DensePassageRetriever(
            document_store=document_store,
            query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
            passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
            use_gpu=True,
            embed_title=True
        )

        reader = FARMReader(model_name_or_path="deepset/roberta-base-squad2", use_gpu=True)

        # Initialize pipeline
        pipe = ExtractiveQAPipeline(reader, retriever)

        init_messages()

        # Get user input -> Generate the answer
        if user_input := st.text_input('Input your question!'):
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner('Bot is typing ...'):
                prediction = pipe.run(query=user_input, top_k_retriever=5, top_k_reader=1)
                answer = prediction['answers'][0]['answer'] if prediction['answers'] else 'No answer found.'

            st.session_state.messages.append(AIMessage(content=f"**Source**: {documents[0]['meta']['file_name']}  \n**Answer**: {answer}"))

        # Show all the messages of the conversation
        messages = st.session_state.get('messages', [])
        for message in messages:
            if isinstance(message, AIMessage):
                with st.chat_message('assistant'):
                    st.markdown(message.content)
            elif isinstance(message, HumanMessage):
                with st.chat_message('user'):
                    st.markdown(message.content)
    else:
        if not os.listdir('./data'):
            st.write('No file is saved yet.')
    
if __name__ == '__main__':
    main()
