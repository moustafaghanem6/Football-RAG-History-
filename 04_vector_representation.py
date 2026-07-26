from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    vector = model.encode(text).tolist()
    return vector

if __name__ == "__main__":
    sample_text = "تجربة تحويل النص إلى متجه رقمي"
    vec = get_embedding(sample_text)
    print(f"تم توليد المتجه بنجاح، طول المتجه (Dimension): {len(vec)}")