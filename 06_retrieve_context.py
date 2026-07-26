import chromadb
from importlib import import_module

def retrieve_relevant_context(query, n_results=3):
    embed_mod = import_module("04_vector_representation")
    
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="rag_collection")
    
    query_vector = embed_mod.get_embedding(query)
    
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n_results
    )
    
    retrieved_docs = []
    if results and "documents" in results and results["documents"]:
        docs = results["documents"][0]
        metadatas = results["metadatas"][0]
        
        for doc, meta in zip(docs, metadatas):
            retrieved_docs.append({
                "content": doc,
                "source": meta.get("source", "Unknown")
            })
            
    return retrieved_docs

if __name__ == "__main__":
    test_query = "Who is the top scorer?"
    contexts = retrieve_relevant_context(test_query)
    print(f"نتائج البحث عن: '{test_query}'")
    for idx, c in enumerate(contexts):
        print(f"\n--- نتيجة {idx+1} (من ملف: {c['source']}) ---")
        print(c['content'][:200])