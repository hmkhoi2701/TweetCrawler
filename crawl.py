from ast import keyword
import os
import pandas as pd


with open('./keyword/democrat.txt') as file:
    keywords = [line.rstrip() for line in file]
print(keywords)

path = "./raw_data/democrat"
# Check whether the path exists or not
if not os.path.exists(path):
   os.makedirs(path)


### Scraping by Using snscrape's CLI command ###
tweet_count = int(1e7)      # no bounded
since_date = "2022-10-01"   
until_date = "2022-12-31"

for search_words in keywords:
    print("Starting process to scrape tweets containing " + search_words + " ...")
    filename = search_words.replace(' ', '')
    os.system('snscrape --jsonl --max-results {} --since {} twitter-search "{} until:{}"> ./raw_data/democrat/democrat_{}.json'.format(tweet_count, since_date, search_words, until_date, filename))
    print("Scraping tweets containing " + search_words + ": DONE")