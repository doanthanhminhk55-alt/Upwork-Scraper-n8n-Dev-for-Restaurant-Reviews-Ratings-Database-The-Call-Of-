from fetchers.yelp_fetcher import get_yelp_restaurants
from fetchers.google_ftecher import get_google_restaurants
from normalizer import normalize_data
from scorer import bayesian_true_score
from vector_store import create_or_update_index

import pandas as pd

def run_ingestion(city="Los Angeles"):
    yelp_data = get_yelp_restaurants(city)
    google_data = get_google_restaurants(city)
    df = normalize_data(yelp_data, google_data)
    df["true_score"] = df.apply(lambda r: bayesian_true_score(r["rating"], r["review_count"]), axis=1)
    create_or_update_index(df)
    df.to_csv(f"result_{city.replace(' ', '_')}.csv", index=False)
    print(f"✅ Data ingested for {city}, saved to CSV.")