import os
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts.chat import ChatPromptTemplate
from pydantic import BaseModel, Field
from chains.prompt_loader import read_prompt_file


class DetectLanguageOutput(BaseModel):
    detected_language: str = Field(description="Detected Language")
    reasoning: str = Field(description="Decision Reasoning")


def get_detect_language_chain(model):
    prompt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "detect_language_template.jinja2")
    model.with_structured_output(DetectLanguageOutput)
    prompt = ChatPromptTemplate.from_messages([("system", read_prompt_file(prompt_file)),
                                               ("human", "{{input_phrase}}")],
                                              template_format="jinja2")
    return prompt | model | PydanticOutputParser(pydantic_object=DetectLanguageOutput)