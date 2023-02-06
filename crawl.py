import os
import pandas as pd
import sys

side = sys.argv[1]

keyword = sys.argv[2] + ' ' + sys.argv[3]

path = f"/kaggle/working/TweetCrawler/raw_data/{side}"
# Check whether the path exists or not
if not os.path.exists(path):
   os.makedirs(path)

tweet_count = int(1e7)
since_date = sys.argv[4]   
until_date = sys.argv[5]

print("Starting process to scrape tweets containing " + keyword + " ...")
filename = keyword.replace(' ', '')
os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> /kaggle/working/TweetCrawler/raw_data/{}/{}.json'.format(tweet_count, since_date, keyword, until_date, side, filename))
print("Scraping tweets containing " + keyword + ": DONE")
