from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from chains.response.response_chain import get_combined_response_chain


load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)


app = FastAPI(
    title="Translation App Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)


add_routes(
    app,
    get_combined_response_chain(model),
    path="/translate",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)