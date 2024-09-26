from dotenv import load_dotenv
from langsmith import Client
from langsmith.evaluation import evaluate
from langchain_openai import ChatOpenAI

from chains.detect_tone.detect_tone import get_detect_tone_chain
from chains.response.response_chain import get_combined_response_chain


load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)
client = Client()


# Define your evaluator
def tone_match(run, example):
    evaluation_chain = get_detect_tone_chain(model)
    expected_tone = example.inputs.get("output_tone")
    evaluated_tone = evaluation_chain.invoke({"input_phrase": run.outputs.get("translation_output").translation_output}).detected_tone
    return {"score": expected_tone == evaluated_tone, "key": "tone_match"}


dataset_name = "Translation Test Dataset"
experiment_results = evaluate(
    get_combined_response_chain(model).invoke,
    data=dataset_name,
    evaluators=[tone_match],
    experiment_prefix="translation-tone-experiment"
)