def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def split_documents_into_chunks(documents, chunk_size=500, overlap=50):
    chunked_data = []
    for doc in documents:
        chunks = chunk_text(doc["content"], chunk_size, overlap)
        for i, chunk in enumerate(chunks):
            chunked_data.append({
                "source": doc["source"],
                "chunk_id": i,
                "content": chunk
            })
    print(f"تم تقسيم المستندات إلى {len(chunked_data)} جزء (Chunk) بنجاح.")
    return chunked_data

if __name__ == "__main__":
    from importlib import import_module
    doc_mod = import_module("01_documents")
    prep_mod = import_module("02_preprocessing")
    
    docs = prep_mod.clean_documents(doc_mod.load_documents())
    chunks = split_documents_into_chunks(docs)
    print(f"إجمالي عدد الـ Chunks: {len(chunks)}")