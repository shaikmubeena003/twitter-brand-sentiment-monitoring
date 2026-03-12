import pandas as pd

data = pd.read_csv("twitter.csv")

print(data.head())
print(data.shape)
data["sentiment"] = data["label"].map({
    0: "Positive",
    1: "Negative"
})

print(data.head())
import re

def clean_tweet(text):
    
    text = re.sub("@[A-Za-z0-9_]+","",text)  # remove usernames
    text = re.sub("#","",text)               # remove hashtags
    text = re.sub("http\S+","",text)         # remove links
    text = re.sub("[^A-Za-z ]","",text)      # remove special chars
    
    return text.lower()

data["clean_tweet"] = data["tweet"].apply(clean_tweet)

print(data.head())
data.to_csv("clean_twitter_data.csv",index=False)

import sqlite3

# connect to database (creates file if not exists)
conn = sqlite3.connect("twitter_sentiment.db")

# store dataframe into SQL table
data.to_sql("tweets", conn, if_exists="replace", index=False)

print("Data stored in database successfully!")

conn.close()

import sqlite3
import pandas as pd

conn = sqlite3.connect("twitter_sentiment.db")

query = "SELECT * FROM tweets LIMIT 5"

result = pd.read_sql(query, conn)

print(result)

conn.close()
