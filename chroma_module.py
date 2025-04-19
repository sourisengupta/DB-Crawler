import chromadb
from chromadb.utils import embedding_functions

client = chromadb.PersistentClient(path="./chroma_db")

def add_to_vector_store(collection_name, documents):
    collection = client.get_or_create_collection(name=collection_name)
    for i, doc in enumerate(documents):
        collection.add(
            documents=[doc],
            ids=[f"doc_{i}"]
        )

def search_similar(collection_name, query_text):
    collection = client.get_or_create_collection(name=collection_name)
    results = collection.query(
        query_texts=[query_text],
        n_results=3
    )
    return results