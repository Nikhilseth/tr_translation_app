import os
from langchain_core.prompts.chat import ChatPromptTemplate
from pydantic import BaseModel, Field
from chains.prompt_loader import read_prompt_file


class TranslationOutput(BaseModel):
    translation_output: str = Field(description="Translation Output")


def get_translation_chain(model):
    prompt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "translate_template.jinja2")
    model.with_structured_output(TranslationOutput)
    prompt = ChatPromptTemplate.from_messages([("system", read_prompt_file(prompt_file)),
                                               ("human", "{{input_phrase}}")],
                                              template_format="jinja2")
    return prompt | model
