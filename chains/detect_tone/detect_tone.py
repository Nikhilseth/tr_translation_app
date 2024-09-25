import os
from langchain_core.prompts.chat import ChatPromptTemplate
from pydantic import BaseModel, Field
from chains.prompt_loader import read_prompt_file


class DetectToneOutput(BaseModel):
    detected_tone: str = Field(description="Detected Language")
    reasoning: str = Field(description="Detected Language")


def get_detect_tone_chain(model):
    prompt_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "detect_tone_template.jinja2")
    model.with_structured_output(DetectToneOutput)
    prompt = ChatPromptTemplate.from_messages([("system", read_prompt_file(prompt_file)),
                                               ("human", "{{input_phrase}}")],
                                              template_format="jinja2")
    return prompt | model