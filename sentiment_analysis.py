import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER for sentiment analysis
nltk.download("vader_lexicon")

#Load the cleaned tweets CSV file
df = pd.read_csv("cleaned_tweets.csv")

#Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

#Function to get sentiment scores
def analyze_sentiment(tweet):
    scores = sia.polarity_scores(tweet)
    if scores["compound"] >= 0.05:
        return "Positive"
    elif scores["compound"] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

#Apply sentiment analysis to each cleaned tweet
df["Sentiment"] = df["Cleaned_Tweet"].apply(analyze_sentiment)

#Save the results
df.to_csv("tweets_with_sentiment.csv", index=False)

#Show the first few rows
print(df.head())
