import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary resources for NLTK
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")

#Load the CSV file
df = pd.read_csv("tweets.csv")

#Check the column name
print(df.columns)

if "Tweet" not in df.columns:
    print("Error: 'Tweet' column not found! Check column names.")
    exit()

#Function to clean tweets
def clean_tweet(tweet):
    tweet = str(tweet).lower()  # Convert to lowercase
    tweet = re.sub(r"http\S+|www\S+|https\S+", "", tweet, flags=re.MULTILINE)  # Remove URLs
    tweet = re.sub(r"@\w+", "", tweet)  # Remove mentions (@usernames)
    tweet = re.sub(r"#\w+", "", tweet)  # Remove hashtags
    tweet = re.sub(r"[^a-zA-Z\s]", "", tweet)  # Remove special characters, numbers, punctuation
    tokens = word_tokenize(tweet)  # Tokenize words
    tokens = [word for word in tokens if word not in stopwords.words("english")]  # Remove stopwords
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatize words
    return " ".join(tokens)

#Apply cleaning to the "Tweet" column
df["Cleaned_Tweet"] = df["Tweet"].apply(clean_tweet)

#Save the cleaned data
df.to_csv("cleaned_tweets.csv", index=False)

print(df.head())
