import os
import pandas as pd

def load_documents(data_dir="Data"):
    documents = []
    if not os.path.exists(data_dir):
        print(f"المجلد {data_dir} غير موجود!")
        return documents

    for filename in os.listdir(data_dir):
        file_path = os.path.join(data_dir, filename)
        if filename.endswith((".xlsx", ".xls")):
            try:
                df = pd.read_excel(file_path)
                content = df.to_string(index=False)
                documents.append({"source": filename, "content": content})
                print(f"تم تحميل ملف الإكسل بنجاح: {filename}")
            except Exception as e:
                print(f"خطأ في قراءة ملف الإكسل {filename}: {e}")
        elif filename.endswith(".txt"):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    documents.append({"source": filename, "content": content})
                print(f"تم تحميل الملف النصي بنجاح: {filename}")
            except Exception as e:
                print(f"خطأ في قراءة الملف {filename}: {e}")
    return documents

if __name__ == "__main__":
    docs = load_documents()
    print(f"\nإجمالي عدد المستندات التي تم تحميلها: {len(docs)}")