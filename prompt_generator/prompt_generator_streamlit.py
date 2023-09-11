from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
import streamlit as st
from prompts import PROMPT_IMPROVER_PROMPT
from  initialization import initialize_llm



# This Python Script is a Streamlit App that allows you to generate a prompt using the Prompt Improver Template
# You can run this file by running the following command in your terminal:
# streamlit run prompt_generator_streamlit.py

# Set up Streamlit Interface

with st.container():
    st.markdown("""
                ## Enter initial prompt here:
                """)
initial_prompt = st.text_area(label="Prompt Input", label_visibility='collapsed', placeholder="Generate a workout schedule", key="prompt_input")

if initial_prompt:
    # Initialize LLM
    # openai_api_key = "YOUR_OPENAI_API_KEY"
    # llm = initialize_llm(project_id,region,model_name,max_tokens,temperature,top_p,top_k)
    llm = initialize_llm("landing-zone-demo-341118","us-central1","text-bison-32k","8192","0.1","0.8","40")
    
    # Initialize LLMChain
    prompt_improver_chain = LLMChain(llm=llm, prompt=PROMPT_IMPROVER_PROMPT)

    # Run LLMChain
    with st.spinner("Generating..."):
        improved_prompt = prompt_improver_chain.run(initial_prompt)
        st.markdown("""
                    ## Improved Prompt:
                    """)
        st.code(improved_prompt)