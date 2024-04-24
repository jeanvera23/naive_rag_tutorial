
import os
import argparse
# LLM utils
from langchain.vectorstores.chroma import Chroma

# Embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings

# Chat models
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

from dotenv import load_dotenv
load_dotenv()

DB_PATH = "./chroma"

PROMPT_TEMPLATE = """[INST]Answer the question based only on the following context:
Context:
{context}

[/INST]

Question:
{question}
"""


def retrieving_from_db(query_text):
    # Prepare the DB.
    embedding_function = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"),model="text-embedding-ada-002")
    db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)
    
     # Search for the 3 more relevant into the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return
    return results
    
def generating_response(query_text, results):
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOpenAI()
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    return formatted_response
    
def generating_response_localhost(query_text, results):
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOllama(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    return formatted_response