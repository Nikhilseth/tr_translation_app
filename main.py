from dotenv import load_dotenv
from chains.response.response_chain import get_combined_response_chain

# import langchain
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers.json import JsonOutputParser
# from langchain_core.prompts.chat import ChatPromptTemplate
# from pydantic import BaseModel, Field

# import langsmith
# import langserve

# detect tone. Have tone as input. Translate from detected tone to output tone.

load_dotenv()
input_phrase = "parles-tu français?"

combined_chain = get_combined_response_chain()

output = combined_chain.invoke({"input_phrase": input_phrase})
print(output)