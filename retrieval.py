from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL, TOP_K


def build_vector_store():

    docs = []

    folder = Path("knowledge_base")

    for file in folder.glob("*.md"):
        loader = TextLoader(str(file), encoding="utf-8")
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore


def retrieve(question: str):

    vectorstore = build_vector_store()

    results = vectorstore.similarity_search(
        question,
        k=TOP_K
    )

    return results