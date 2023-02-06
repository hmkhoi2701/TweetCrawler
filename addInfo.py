import os
import pandas as pd
import sys

side = sys.argv[1]
keyword = sys.argv[2] + ' ' + sys.argv[3]

path = "/kaggle/working/TweetCrawler/data"
# Check whether the path exists or not
if not os.path.exists(path):
   os.makedirs(path)


### Scraping User Profile (Optional) ###
all_info = []
filename = keyword.replace(' ', '')
info = pd.read_json('/kaggle/working/TweetCrawler/raw_data/{}/{}.json'.format(side,filename), lines=True)[['user']]
rows = []
for idx in range(len(info['user'])):
    row = info['user'][idx]
    for key in row.keys():
        row[key] = [row[key]]
    rows.append(pd.DataFrame.from_dict(row))
all_info.append(pd.concat(rows))
info_df = pd.concat(all_info, ignore_index=True)[['id', 'location']]
info_df.rename(columns = {'id':'user_id'}, inplace=True)


### Combine all content of tweets and necessary features ###
frames = []
filename = keyword.replace(' ', '') 
df = pd.read_json('/kaggle/working/TweetCrawler/raw_data/{}/{}.json'.format(side, filename), lines=True)[['id', 
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
final['subject'] = side
final.to_csv(f'/kaggle/working/Crawl_{side}_{sys.argv[2]}_{sys.argv[3]}.csv')
