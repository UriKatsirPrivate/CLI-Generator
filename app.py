import streamlit as st
from langchain.chains import LLMChain
from langchain import hub
# from langchain.prompts.chat import (ChatPromptTemplate,
#                                     HumanMessagePromptTemplate,
#                                     SystemMessagePromptTemplate)
from back import get_project_id, initialize_llm

# https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="GCP CLI Generator",
    page_icon="icons/vertexai.png",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get help': 'https://github.com/UriKatsirPrivate/CLI-Generator',
        'About': "#### Created by [Uri Katsir](https://www.linkedin.com/in/uri-katsir/)"
    }
)

# def gcpCliCommandGenerator(user_input):
    
#     llm = initialize_llm(project_id,region,model_name,max_tokens,temperature,top_p,top_k)
    
#     system_template = """You are a virtual assistant capable of generating the corresponding Google Cloud Platform (GCP) command-line interface (CLI) command based on the user's input."""
#     system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
#     human_template = """The user's input is: '{user_input}'. Please generate the corresponding GCP CLI command. Be as elaborate as possible and use as many flags as possible.
#                         For every flag you use, explain its purpose. also, make sure to provide a working sample command.
#                         """
#     human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
#     chat_prompt = ChatPromptTemplate.from_messages(
#         [system_message_prompt, human_message_prompt]
#     )

#     chain = LLMChain(llm=llm, prompt=chat_prompt)
#     result = chain.run(user_input=user_input)
#     return result # returns string   

# Function to generate the GCP CLI command based on a prompt form PromptHub
# https://smith.langchain.com/hub/uri-katsir/generate-gcp-cli-commands
def generate_gcp_command(user_input):
    llm = initialize_llm(project_id,region,model_name,max_tokens,temperature,top_p,top_k)
    prompt =  hub.pull("uri-katsir/generate-gcp-cli-commands")
    runnable = prompt | llm
    # print(
    # prompt.format(
    #     user_input=user_input,
        
    # ))
    result = runnable.invoke({
                        "user_input": user_input
                    })
    return result # returns string

def display_gcp_command(gcp_command):
    if gcp_command != "":
        st.markdown(f"**Generated GCP CLI Command:** {gcp_command}")
    else:
        st.markdown("No command generated. Please enter a valid GCP operation.")

# Step-1 Get input from the user
REGIONS=["europe-west4","us-central1","us-west4","us-west1","us-east4"]
MODEL_NAMES=['gemini-1.0-pro-001','text-bison-32k','code-bison-32k']

PROJECT_ID=st.sidebar.text_input(label="Project ID",value="Your Project ID")
if PROJECT_ID=="" or PROJECT_ID=="Your Project ID":
    # print("getting project id")
    PROJECT_ID=get_project_id()

project_id=PROJECT_ID    
st.sidebar.write("Project ID: ",f"{PROJECT_ID}")
user_input = st.text_input("Please enter the desired GCP operation")
region=st.sidebar.selectbox("Please enter the region",REGIONS)
model_name = st.sidebar.selectbox('Enter model name',MODEL_NAMES)
max_tokens = st.sidebar.slider('Enter max token output',min_value=1,max_value=8192,step=100,value=8192)
temperature = st.sidebar.slider('Enter temperature',min_value=0.0,max_value=1.0,step=0.1,value=0.1)
top_p = st.sidebar.slider('Enter top_p',min_value=0.0,max_value=1.0,step=0.1,value=0.8)
top_k = st.sidebar.slider('Enter top_k',min_value=1,max_value=40,step=1,value=40)

if not ('32k' in model_name or 'gemini' in model_name) and max_tokens>1024:
  st.error(f'{max_tokens} output tokens is not a valid value for model {model_name}')

# Step-2 Put a submit button with an appropriate title
if st.button('Generate GCP CLI Command',disabled=not (project_id)):
    # Step-3 Call functions only if all user inputs are taken and the button is clicked.
    if user_input:
        with st.spinner('Generating command...'):
            # gcp_command = gcpCliCommandGenerator(user_input)
            gcp_command = generate_gcp_command(user_input)
        display_gcp_command(gcp_command)
    else:
        st.markdown("No command generated. Please enter a valid GCP operation.")