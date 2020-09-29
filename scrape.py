import requests
import pandas as pd
import json
import time


def crawl_subreddit(subreddit, max_submissions=2000):
    """
    Crawl submissions from a subreddit.

    Parameters
    ----------
    subreddit: string
        The subreddit to crawl.
    max_submissions: integer
        The maximum number of submissions to download.

    Returns
    -------
    A list of submissions.
    """

    submissions = []
    last_page = None
    while last_page != [] and len(submissions) < max_submissions:
        last_page = crawl_page(subreddit, last_page)
        submissions += last_page
        time.sleep(2)

    return submissions[:max_submissions]


def crawl_page(subreddit: str, last_page=None):
    """Crawl a page of results from a given subreddit.

    Parameters
    ----------
    subreddit: string
        The subreddit to crawl.
    last_page: string
        The last downloaded page.

    Returns
    -------
    A page or results.
    """

    url = "https://api.pushshift.io/reddit/search/submission"
    params = {"subreddit": subreddit, "size": 2000, "sort": "desc", "sort_type": "score", "q": "coronavirus"}

    if last_page is not None:
        if len(last_page) > 0:
            # resume from where we left at the last page
            params["before"] = last_page[-1]["created_utc"]
        else:
            # the last page was empty, we are past the last page
            return []

    results = requests.get(url, params)

    if not results.ok:
        # Something wrong happened
        raise Exception("Server returned status code {}".format(results.status_code))

    return results.json()["data"]


def pretty_print_json(file_path):
    """
    Pretty prints the JSON file using 4 spaces as indent

    Parameters
    ----------
    file_path: string
        The file path to the JSON file (including the file.json)

    Returns
    -------
    Nothing
    """

    with open(file_path) as f:
        output = json.load(f)

    with open(file_path, "w") as twitter_data_file:
        json.dump(output, twitter_data_file, indent=4, sort_keys=True)


def main():
    data = crawl_subreddit("explainlikeimfive")
    df = pd.DataFrame(data=data)

    # Display all rows when printing out
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    # Filter only for the columns we care about
    df = df.filter(['id', 'link_flair_text', 'selftext', 'title', 'url', 'score'])

    # Filter out all the removed texts
    df = df[~df['selftext'].str.contains('[deleted]', na=False)]

    # Export to JSON
    df.to_json('Export_DataFrame.json')
    pretty_print_json('Export_DataFrame.json')

    print(df)


if __name__ == '__main__':
    main()
