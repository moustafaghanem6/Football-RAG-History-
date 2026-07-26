import re

def preprocess_text(text):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def clean_documents(documents):
    cleaned_docs = []
    for doc in documents:
        cleaned_content = preprocess_text(doc["content"])
        cleaned_docs.append({
            "source": doc["source"],
            "content": cleaned_content
        })
    print("تم تنظيف ومعالجة جميع المستندات بنجاح.")
    return cleaned_docs

if __name__ == "__main__":
    from importlib import import_module
    doc_module = import_module("01_documents")
    raw_docs = doc_module.load_documents()
    cleaned = clean_documents(raw_docs)
    print(f"عدد المستندات بعد التنظيف: {len(cleaned)}")