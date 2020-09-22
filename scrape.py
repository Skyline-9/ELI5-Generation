import requests
import pandas as pd
import json
import csv
import time
import datetime


def get_pushshift_data(data_type, **kwargs):
    """
    Gets data from Reddit using the Pushshift API

    Parameters
    ----------
    data_type: string
        'comment' if you are searching for comments
        'submission' if you are searching for submissions

    **kwargs: keyword arguments
        These arguments are interpreted as a payload. Here are the following allowed parameters:

        q: search term
        duration: timeframe as an Epoch value or integer (i.e. 30d for 30 days)
        after: return results after this date specified as an Epoch value or integer (i.e. 30d for 30 days)
        before: return results before this date specified as an Epoch value or integer (i.e. 30d for 30 days)
        size: number of results to return
        sort_type: string denoting what to sort by ("score", "num_comments", "created_utc")
        sort: sort in a specific order ("asc" or "desc")
        aggs: aggregation summary ["author", "link_id", "created_utc", "subreddit"]
        subreddit: string containing the specific subreddit to search

        More details on PushShift API's documentation

    Returns
    -------
    data : array_like
        Data
    """
    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)

    # data = json.loads(request.text)
    return request.json()


def main():
    data_type = "submission"  # Comments or Submissions
    query = "coronavirus"  # Add your query
    duration = "365d"  # Select the timeframe. Epoch value or Integer + "s,m,h,d"
    size = 1000  # Maximum 1000 comments
    sort_type = "score"  # Sort by score (Accepted: "score", "num_comments", "created_utc")
    sort = "desc"  # Sort descending
    aggs = "author"  # "author", "link_id", "created_utc", "subreddit"
    subreddit = "explainlikeimfive"

    data = get_pushshift_data(data_type=data_type, q=query, after=duration, size=size, sort_type=sort_type, sort=sort,
                              subreddit=subreddit)

    # Called selftext
    data = data.get("data")[1]['selftext']
    print(data)

    # df = pd.DataFrame.from_records(data)[0:10]
    # print(df)


if __name__ == '__main__':
    main()
