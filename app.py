import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document
from initialization import *



def gcpCliCommandGenerator(user_input):
    # chat = ChatOpenAI(
    #     model="gpt-3.5-turbo-16k",
    #     temperature=0
    # )
    
    llm = initialize_llm()
    
    system_template = """You are a virtual assistant capable of generating the corresponding Google Cloud Platform (GCP) command-line interface (CLI) command based on the user's input."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """The user's input is: '{user_input}'. Please generate the corresponding GCP CLI command."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=llm, prompt=chat_prompt)
    result = chain.run(user_input=user_input)
    return result # returns string   

def display_gcp_command(gcp_command):
    if gcp_command != "":
        st.markdown(f"**Generated GCP CLI Command:** {gcp_command}")
    else:
        st.markdown("No command generated. Please enter a valid GCP operation.")

# Step-3 Get input from the user
user_input = st.text_input("Please enter the desired GCP operation")

# Step-4 Put a submit button with an appropriate title
if st.button('Generate GCP CLI Command'):
    # Step-5 Call functions only if all user inputs are taken and the button is clicked.
    if user_input:
        gcp_command = gcpCliCommandGenerator(user_input)
        display_gcp_command(gcp_command)
    else:
        st.markdown("No command generated. Please enter a valid GCP operation.")