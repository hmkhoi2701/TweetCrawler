import os
import pandas as pd

with open('/kaggle/working/TweetCrawler/keyword/democrat.txt') as file:
    keywords = [line.rstrip() for line in file]
print(keywords)

path = "/kaggle/working/TweetCrawler/data"
# Check whether the path exists or not
if not os.path.exists(path):
   os.makedirs(path)


### Scraping User Profile (Optional) ###
all_info = []
for search_words in keywords:
    filename = search_words.replace(' ', '')
    info = pd.read_json('/kaggle/working/TweetCrawler/raw_data/democrat/democrat_{}.json'.format(filename), lines=True)[['user']]
    rows = []
    for idx in range(len(info['user'])):
        row = info['user'][idx]
        for key in row.keys():
            row[key] = [row[key]]
        rows.append(pd.DataFrame.from_dict(row))
    all_info.append(pd.concat(rows))
info_df = pd.concat(all_info, ignore_index=True)[['username', 'location']]


### Combine all content of tweets and necessary features ###
frames = []
for search_word in keywords:
    filename = search_word.replace(' ', '') 
    df = pd.read_json('/kaggle/working/TweetCrawler/raw_data/democrat/democrat_{}.json'.format(filename), lines=True)[['id', 
                                                                                            'url', 
                                                                                            'date', 
                                                                                            'rawContent',
                                                                                            'hashtags', 
                                                                                            'replyCount', 
                                                                                            'retweetCount', 
                                                                                            'likeCount']]
    df['key'] = search_word
    frames.append(df)
tweets_df = pd.concat(frames, ignore_index=True)
final = pd.concat([tweets_df, info_df], axis=1)
final['subject'] = 'Democrat'
final.to_csv('/kaggle/working/crawl_democrat.csv')