from fastapi import FastAPI, Body
import requests, chromadb
from sentence_transformers import SentenceTransformer

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
CHROMA_URL = "http://localhost:8000"
embedder = SentenceTransformer("all-MiniLM-L6-v2")

chroma_client = chromadb.HttpClient(host="localhost", port=8000)
chroma_client.heartbeat()

try:
    memory = chroma_client.get_collection("memory")
except:
    memory = chroma_client.create_collection("memory")

@app.post("/chat")
def chat(input_text: str = Body(..., embed=True)):
    # Step 1: Retrieve relevant memories
    query_emb = embedder.encode([input_text])[0].tolist()
    results = memory.query(query_embeddings=[query_emb], n_results=3)
    context = "\n".join(r for r in results.get("documents", [[]])[0])

    # Step 2: Combine input + memory into final prompt
    prompt = f"Context from past:\n{context}\n\nUser: {input_text}\nAssistant:"

    # Step 3: Query Ollama locally
    resp = requests.post(OLLAMA_URL, json={"model": "mistral-nemo:12b", "prompt": prompt, "stream": False})
    reply = resp.json()["response"]

    # Step 4: Save this exchange into memory
    doc = f"User: {input_text}\nAssistant: {reply}"
    emb = embedder.encode([doc])[0].tolist()
    memory.add(documents=[doc], embeddings=[emb], ids=[input_text[:32]])

    return {"reply": reply}
