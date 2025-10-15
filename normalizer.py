import pandas as pd

def normalize_data(yelp_data, google_data):
    df = pd.DataFrame(yelp_data + google_data)
    df["name"] = df["name"].str.strip().str.lower()
    df["city"] = df["city"].str.lower()

    agg = df.groupby(["name", "city"]).agg({
        "rating": "mean",
        "review_count": "sum",
        "source": lambda x: ", ".join(set(x))
    }).reset_index()
    return agg