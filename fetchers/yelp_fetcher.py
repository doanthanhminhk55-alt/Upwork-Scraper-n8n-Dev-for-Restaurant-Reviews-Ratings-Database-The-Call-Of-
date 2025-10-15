import os, requests

YELP_API_KEY = os.getenv("YELP_API_KEY")
BASE_URL = "https://api.yelp.com/v3/businesses/search"

def get_yelp_restaurants(city="Los Angeles", term="restaurant", limit=5):
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {"term": term, "location": city, "limit": limit}
    response = requests.get(BASE_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json().get("businesses", [])
    results = []
    for b in data:
        results.append({
            "name": b["name"],
            "rating": b.get("rating"),
            "review_count": b.get("review_count"),
            "source": "Yelp",
            "city": city
        })
    return results