import praw


def main():
    reddit = praw.Reddit(client_id="1tuEGFxlLsiqEA", client_secret="Z0yvyOrukSKcX4hh_SUoep3oD5Q",
                         password="GTATuesday630",
                         user_agent="eli5 scrape by u/GT-ELI5",
                         username="GT-ELI5")

    subreddit = reddit.subreddit("explainlikeimfive")
    for submission in subreddit.top(limit=1):
        print(submission.title)
        print(submission.score)
        print(submission.comments[0])


if __name__ == '__main__':
    main()
