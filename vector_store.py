import os, pickle, faiss
from sentence_transformers import SentenceTransformer
import numpy as np

VECTOR_INDEX_PATH = os.getenv("VECTOR_INDEX_PATH", "faiss.index")
META_PATH = os.getenv("META_PATH", "meta.pkl")

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_or_update_index(data):
    vectors = model.encode(data["name"].tolist())
    index = faiss.Index2Layer(vectors.shape[1])
    index.add(np.array(vectors, dtype=np.float32))
    faiss.write_index(index, VECTOR_INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(data.to_dict(orient="records"), f)
    print("✅ Vector DB updated.")

def query_restaurant(name_query, top_k=3):
    index = faiss.read_index(VECTOR_INDEX_PATH)
    with open(META_PATH, "rb") as f:
        meta = pickle.load(f)
    vectors = model.encode([name_query])
    D, I = index.sreach(np.array(vectors, dtype=np.float32), top_k)
    return [meta[i] for i in I[0]]
