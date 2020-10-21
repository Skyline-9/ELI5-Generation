import praw
import pandas as pd
import os
from dotenv import load_dotenv
from psaw import PushshiftAPI


def main():
    # Reading in client_id, client_secret, username, and password
    load_dotenv()
    client_id = os.getenv('client_id')
    client_secret = os.getenv('client_secret')
    username = os.getenv('username')
    password = os.getenv('password')

    # Authentication
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password,
                         user_agent="eli5 scrape by u/GT-ELI5", username=username)

    # PSAW wrap
    api = PushshiftAPI(reddit)
    gen = api.search_submissions(subreddit='explainlikeimfive', sort_type='score', limit=3)
    gen = list(gen)

    df = pd.DataFrame(columns=['Title', 'Score', 'Answer'])
    for i, submission in enumerate(gen):
        comments = list(submission.comments)

        # Trying to find first non-stickied post (not a mod post)
        index = 0
        while comments[index].stickied:
            index = index + 1
        
        # Add to pandas dataframe
        df.loc[i] = [submission.title, submission.score, comments[index].body]

    df.to_json('data.json')
    print(df)


if __name__ == '__main__':
    main()
