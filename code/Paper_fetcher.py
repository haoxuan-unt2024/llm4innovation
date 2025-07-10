import openreview
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import os
from tqdm import tqdm
import json

OPENREVIEW_USERNAME = "username"
OPENREVIEW_PASSWORD = "password"

class PaperFetcherWithRatingStats:

    def __init__(self, conference_name: str, year: str):
        print("Initialing OpenReview ...")
        self.client = openreview.api.OpenReviewClient(
            baseurl="https://api2.openreview.net",
            username=OPENREVIEW_USERNAME,
            password=OPENREVIEW_PASSWORD,
        )

        self.conference_name = conference_name
        self.year = year
        self.venue_id = f"{conference_name}.cc/{year}/Conference"
        self.root_dir = os.path.join("../Data", conference_name, year)
        self.paper_dir = os.path.join(self.root_dir, "papers")
        os.makedirs(self.paper_dir, exist_ok=True)

        group = self.client.get_group(self.venue_id)
        content = group.content
        self.submission_invitation = content["submission_id"]["value"]
        self.review_invitation_name = content["review_name"]["value"]

    def fetch_submissions(self):
        print("Fetching paper submission information...")
        submissions = self.client.get_all_notes(invitation=self.submission_invitation, details="directReplies")
        print(f"Retrieved {len(submissions)} submissions")
        return submissions

    def extract_rating_stats(self, paper_id):
        reviews = self.client.get_all_notes(forum=paper_id)
        ratings = []
        for reply in reviews:
            if any(inv.endswith(f"/-/{self.review_invitation_name}") for inv in reply.invitations):
                rating_data = reply.content.get("rating", {})
                if isinstance(rating_data, dict) and "value" in rating_data:
                    try:
                        rating = float(str(rating_data["value"]).split(":")[0].strip())
                        ratings.append(rating)
                    except ValueError:
                        continue
        if ratings:
            return ratings, np.mean(ratings), np.std(ratings)
        else:
            return [], None, None

    def process_papers(self):
        submissions = self.fetch_submissions()
        papers_data = []

        for submission in tqdm(submissions, desc="Extracting Score"):
            paper_id = submission.id
            title = submission.content.get("title", {}).get("value", "Unknown Title")
            abstract = submission.content.get("abstract").get("value")
            ratings, avg_rating, std_rating = self.extract_rating_stats(paper_id)
            if avg_rating is not None:
                papers_data.append({
                    "id": paper_id,
                    "title": title,
                    "abstract": abstract,
                    "ratings" : ratings,
                    "average_rating": avg_rating,
                    "std_rating": std_rating
                })

        df = pd.DataFrame(papers_data)
        csv_path = os.path.join(self.paper_dir, f"{self.conference_name}{self.year}_papers_avg_rating.csv")
        df.to_csv(csv_path, index=False, encoding="utf-8")
        print(f"Average rating stores at {csv_path}")
        return df
    
# Examples 
fetcher = PaperFetcherWithRatingStats("NeurIPS", "2024")
df = fetcher.process_papers()