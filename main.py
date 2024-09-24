import os
from dotenv import load_dotenv

import langchain
from langchain_openai import ChatOpenAI

# import langsmith
# import langserve

load_dotenv()

input_phrase = 'Cest quoi la fromage?'

model = ChatOpenAI(model='gpt-4o-mini', temperature=0)

