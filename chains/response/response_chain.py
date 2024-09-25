from operator import itemgetter, attrgetter
from langchain_core.runnables import RunnablePassthrough
from chains.detect_language.detect_language import get_detect_language_chain
from chains.translate.translate import get_translation_chain


def get_combined_response_chain():
    return (
        RunnablePassthrough()
        | {"input_phrase": itemgetter("input_phrase")}
        | {
            "input_phrase": itemgetter("input_phrase"),
            "detected_language": get_detect_language_chain()
        } | {
            "input_phrase": itemgetter("input_phrase"),
            "detected_language": itemgetter("detected_language"),
            "translation_output": get_translation_chain()
        })