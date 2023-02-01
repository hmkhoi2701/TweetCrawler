import os
import pandas as pd
import sys

keyword = sys.argv[1] + ' ' + sys.argv[2]

path = "/kaggle/working/TweetCrawler/data"
# Check whether the path exists or not
if not os.path.exists(path):
   os.makedirs(path)


### Scraping User Profile (Optional) ###
all_info = []
filename = keyword.replace(' ', '')
info = pd.read_json('/kaggle/working/TweetCrawler/raw_data/democrat/democrat_{}.json'.format(filename), lines=True)[['user']]
rows = []
for idx in range(len(info['user'])):
    row = info['user'][idx]
    for key in row.keys():
        row[key] = [row[key]]
    rows.append(pd.DataFrame.from_dict(row))
all_info.append(pd.concat(rows))
info_df = pd.concat(all_info, ignore_index=True)[['id', 'location']]


### Combine all content of tweets and necessary features ###
frames = []
filename = keyword.replace(' ', '') 
df = pd.read_json('/kaggle/working/TweetCrawler/raw_data/democrat/democrat_{}.json'.format(filename), lines=True)[['id', 
                                                                                        'url', 
                                                                                        'date', 
                                                                                        'rawContent',
                                                                                        'hashtags', 
                                                                                        'replyCount', 
                                                                                        'retweetCount', 
                                                                                        'likeCount']]
df['key'] = keyword
frames.append(df)
tweets_df = pd.concat(frames, ignore_index=True)
final = pd.concat([tweets_df, info_df], axis=1)
final['subject'] = 'Democrat'
final.to_csv('/kaggle/working/K_crawl_democrat.csv')
