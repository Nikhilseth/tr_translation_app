from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from langsmith import traceable

from chains.detect_language.detect_language import get_detect_language_chain
from chains.translate.translate import get_translation_chain
from chains.detect_tone.detect_tone import get_detect_tone_chain


@traceable()
def get_combined_response_chain(model):
    return (
        RunnablePassthrough()
        | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone")
        } | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone"),
            "detected_language": get_detect_language_chain(model)
        } | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone"),
            "detected_language": itemgetter("detected_language"),
            "detected_tone": get_detect_tone_chain(model)
        } | {
            "translation_output": get_translation_chain(model),
            "detected_language": itemgetter("detected_language"),
            "detected_tone": itemgetter("detected_tone"),
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone")
        })