from dotenv import load_dotenv
from langsmith import Client


load_dotenv()
client = Client()


# Define dataset: these are your test cases
dataset_name = "Translation Test Dataset"
dataset = client.create_dataset(dataset_name, description="A small translation dataset.")
client.create_examples(
    inputs=[
        {
            "input_phrase": "Je vous prie de bien vouloir accepter mes salutations distinguées.",
            "output_tone": "formal"
        },
        {
            "input_phrase": "Pourriez-vous m’indiquer la marche à suivre afin de finaliser ce dossier ?",
            "output_tone": "formal"
        },
        {
            "input_phrase": "Nous vous remercions pour votre attention à ce sujet et restons à votre entière disposition.",
            "output_tone": "informal"
        },
        {
            "input_phrase": "Salut, comment ça va ?",
            "output_tone": "informal"
        },
        {
            "input_phrase": "Tu peux m'envoyer le truc quand tu as le temps ?",
            "output_tone": "formal"
        },
        {
            "input_phrase": "Ça te dit de sortir ce soir ?",
            "output_tone": "formal"
        },
        {
            "input_phrase": "Le agradezco mucho su tiempo y consideración.",
            "output_tone": "formal"
        },
        {
            "input_phrase": "¿Podría indicarme la fecha exacta en que se realizará la reunión?",
            "output_tone": "informal"
        },
        {
            "input_phrase": "Quedamos a su disposición para cualquier consulta adicional.",
            "output_tone": "informal"
        },
        {
            "input_phrase": "Hola, ¿qué tal?",
            "output_tone": "formal"
        },
    ],
    outputs=[
        {
            "expected_translation": "Please accept my distinguished regards.",
            "output_tone": "formal"
        },
        {
            "expected_translation": "Could you kindly indicate the procedure to complete this file?",
            "output_tone": "formal"
        },
        {
            "expected_translation": "We thank you for your attention on this matter and remain at your full disposal.",
            "output_tone": "informal"
        },
        {
            "expected_translation": "Hey, how’s it going?",
            "output_tone": "informal"
        },
        {
            "expected_translation": "Can you send me the thing when you have time?",
            "output_tone": "formal"
        },
        {
            "expected_translation": "Do you feel like going out tonight?",
            "output_tone": "formal"
        },
        {
            "expected_translation": "I greatly appreciate your time and consideration.",
            "output_tone": "formal"
        },
        {
            "expected_translation": "Could you kindly indicate the exact date when the meeting will take place?",
            "output_tone": "informal"
        },
        {
            "expected_translation": "We remain at your disposal for any further inquiries.",
            "output_tone": "informal"
        },
        {
            "expected_translation": "Hey, how’s it going?",
            "output_tone": "formal"
        },
    ],
    dataset_id=dataset.id,
)