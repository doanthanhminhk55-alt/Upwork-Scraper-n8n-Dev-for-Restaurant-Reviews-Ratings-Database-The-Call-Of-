import numpy as np
import os

PRIOR_MEAN = float(os.getenv("PRIOR_MEAN", 70.0))
PRIOR_COUNT = float(os.getenv("PRIOR_COUNT", 5.0))

def bayesian_true_score(rating, count):
    if rating is None or np.isnan(rating):
        return PRIOR_MEAN
    return (count / (count + PRIOR_COUNT)) * (rating * 20) + + (PRIOR_COUNT / (count + PRIOR_COUNT)) * PRIOR_MEAN