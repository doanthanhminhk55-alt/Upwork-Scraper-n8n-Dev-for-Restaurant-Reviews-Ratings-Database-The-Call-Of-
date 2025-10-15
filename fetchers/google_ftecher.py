import os, requests

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_google_restaurants(city="Los Angeles", query="restaurants", limit=5):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"query": f"{query} in {city}", "key": GOOGLE_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json().get("results", [])
    results = []
    for b in data[:limit]:
        results.append({
            "name": b["name"],
            "rating": b.get("rating"),
            "review_count": b.get("user_ratings_total"),
            "source": "Google",
            "city": city
        })
    return results
