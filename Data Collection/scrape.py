import praw
import pandas as pd
import os
from dotenv import load_dotenv


def main():
    # Reading in client_id and client_secret
    load_dotenv()
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')

    # Authentication
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password="GTATuesday630",
                         user_agent="eli5 scrape by u/GT-ELI5", username="GT-ELI5")

    # Start scraping data into a pandas dataframe
    subreddit = reddit.subreddit("explainlikeimfive")
    df = pd.DataFrame(columns=['Title', 'Score', 'Answer'])

    i = 0
    for submission in subreddit.top(limit=3):
        df.loc[i] = [submission.title, submission.score, list(submission.comments)[1].body]
        i = i + 1

    # Save as json
    df.to_json(os.path.join('Data Collection', 'eli5.json'))
    print(df)


if __name__ == '__main__':
    main()
