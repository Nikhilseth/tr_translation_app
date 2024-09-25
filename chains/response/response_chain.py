from operator import itemgetter
from langchain_core.runnables import RunnablePassthrough
from chains.detect_language.detect_language import get_detect_language_chain
from chains.translate.translate import get_translation_chain
from chains.detect_tone.detect_tone import get_detect_tone_chain


def get_combined_response_chain():
    return (
        RunnablePassthrough()
        | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone")
        }
        | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone"),
            "detected_language": get_detect_language_chain()
        } | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone"),
            "detected_language": itemgetter("detected_language"),
            "detected_tone": get_detect_tone_chain()
        }
        | {
            "input_phrase": itemgetter("input_phrase"),
            "output_tone": itemgetter("output_tone"),
            "detected_language": itemgetter("detected_language"),
            "detected_tone": itemgetter("detected_tone"),
            "translation_output": get_translation_chain()
        })