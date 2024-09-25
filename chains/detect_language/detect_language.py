import os
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
from pydantic import BaseModel, Field
from chains.prompt_loader import read_prompt_file


class DetectLanguageOutput(BaseModel):
    detected_language: str = Field(description="Detected Language")
    reasoning: str = Field(description="Detected Language")


def get_detect_language_chain():
    prompt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'detect_language_template.jinja2')
    model = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    prompt = ChatPromptTemplate.from_messages([('system', read_prompt_file(prompt_file)),
                                               ('human', "{{input}}")],
                                              template_format='jinja2')
    return prompt | model | PydanticOutputParser(pydantic_object=DetectLanguageOutput)