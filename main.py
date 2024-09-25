from dotenv import load_dotenv
from chains.detect_language.detect_language import get_detect_language_chain

# import langchain
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers.json import JsonOutputParser
# from langchain_core.prompts.chat import ChatPromptTemplate
# from pydantic import BaseModel, Field

# import langsmith
# import langserve

load_dotenv()
input_phrase = 'parles-tu français?'
chain = get_detect_language_chain()

output = chain.invoke({"input": input_phrase})
print(output)