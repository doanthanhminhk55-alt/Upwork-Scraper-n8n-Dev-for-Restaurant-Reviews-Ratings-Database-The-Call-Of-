# 🧠 Restaurant True Score API  
**Aggregate and score expert + customer restaurant reviews into a single Bayesian True Score (0–100).**

---

## 📋 Overview  
This project builds a **data aggregation and scoring system** for U.S. restaurants, combining reviews from:  
- **Experts:** LA Times, Eater, The Infatuation, Time Out, YouTubers, etc.  
- **Customers:** Yelp, Google Maps, OpenTable, Tripadvisor.  
- **Awards:** Michelin, James Beard, Eater 38, and more.  

It normalizes and deduplicates data, computes a **Bayesian True Score**, and stores results in a **vector database** for intelligent querying.

---

## ⚙️ Features
✅ Scrape and ingest data from expert & customer sources  
✅ Normalize and deduplicate reviews  
✅ Compute Bayesian True Score (0–100)  
✅ Query restaurant ratings through a simple REST API  
✅ Ready for integration into a CMS (WordPress, etc.)  

---

## 🏗️ Tech Stack
| Component | Technology |
|------------|-------------|
| Backend API | **FastAPI (Python)** |
| Data Storage | **FAISS Vector DB** |
| Environment | **Python-dotenv** |
| Review Ingestion | **Custom Python Scripts / n8n Automation** |
| APIs Integrated | Yelp Fusion, Google Places, Michelin, etc. |

---

## 📂 Project Structure
