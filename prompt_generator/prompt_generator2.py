from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from prompts import PROMPT_IMPROVER_PROMPT
from  initialization import initialize_llm


initial_prompt = "Generate a workout schedule"

llm = initialize_llm("landing-zone-demo-341118","us-central1","text-bison-32k","8192","0.1","0.8","40")


# Initialize LLMChain
prompt_improver_chain = LLMChain(llm=llm, prompt=PROMPT_IMPROVER_PROMPT)

# Run LLMChain
improved_prompt = prompt_improver_chain.run(initial_prompt)
print(improved_prompt)