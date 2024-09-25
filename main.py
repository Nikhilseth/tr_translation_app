from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from chains.response.response_chain import get_combined_response_chain

# import langchain
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers.json import JsonOutputParser
# from langchain_core.prompts.chat import ChatPromptTemplate
# from pydantic import BaseModel, Field

# import langsmith
# import langserve

# add routes here. move model to chain parameter.

load_dotenv()
input_phrase = "Il fait une belle journée dehors ! On va à la plage ?"
output_tone = "formal"

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
combined_chain = get_combined_response_chain(model)

output = combined_chain.invoke({"input_phrase": input_phrase, "output_tone": output_tone})
print(output)