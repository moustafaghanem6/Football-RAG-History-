import os
import chromadb
from importlib import import_module

def create_vector_store():
    doc_mod = import_module("01_documents")
    prep_mod = import_module("02_preprocessing")
    chunk_mod = import_module("03_chunking")
    embed_mod = import_module("04_vector_representation")

    print("جاري تحميل ومعالجة وتجهيز المستندات...")
    raw_docs = doc_mod.load_documents()
    cleaned_docs = prep_mod.clean_documents(raw_docs)
    chunks = chunk_mod.split_documents_into_chunks(cleaned_docs)

    client = chromadb.PersistentClient(path="./chroma_db")
    collection_name = "rag_collection"
    
    try:
        client.delete_collection(name=collection_name)
    except Exception:
        pass

    collection = client.create_collection(name=collection_name)

    print("جاري حساب الـ Embeddings وحفظها في ChromaDB...")
    for i, chunk in enumerate(chunks):
        text = chunk["content"]
        if not text.strip():
            continue
        vector = embed_mod.get_embedding(text)
        
        # التصحيح هنا: استخدام chunk["source"] مباشرة
        collection.add(
            ids=[f"id_{i}"],
            embeddings=[vector],
            documents=[text],
            metadatas=[{"source": chunk["source"], "chunk_id": chunk["chunk_id"]}]
        )

    print(f"تم تخزين {len(chunks)} جزء بنجاح داخل قاعدة بيانات ChromaDB!")

if __name__ == "__main__":
    create_vector_store()