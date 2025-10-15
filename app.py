from fastapi import FastAPI
from ingest_worker import run_ingestion
from vector_store import query_restaurant

app = FastAPI(title="Restaurant True Score API")

@app.get("/ingest/{city}")
def ingest(city: str):
    run_ingestion(city)
    return {"status": "ok", "city": city}

@app.get("/qa/{query}")
def qa(query: str):
    results = query_restaurant(query)
    return {"query": query, "matches": results}