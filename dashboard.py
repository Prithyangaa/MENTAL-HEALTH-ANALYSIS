import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv("tweets_with_sentiment.csv")

#Streamlit Page Setup
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

#Title
st.title("📊 Twitter Sentiment Analysis Dashboard")

#Sidebar Filter
sentiment_option = st.sidebar.selectbox("Filter by Sentiment", ["All", "Positive", "Negative", "Neutral"])

#Filter Data
if sentiment_option != "All":
    df = df[df["Sentiment"] == sentiment_option]

#Sentiment Distribution Pie Chart
st.subheader("Sentiment Distribution")
fig, ax = plt.subplots(figsize=(5, 5))
colors = ["green", "red", "gray"]
df["Sentiment"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=colors, startangle=90, ax=ax)
plt.ylabel("")  # Hide y-label
st.pyplot(fig)

#Sentiment Count Bar Chart
st.subheader("Count of Sentiment Categories")
fig, ax = plt.subplots(figsize=(6, 4))
sns.barplot(x=df["Sentiment"].value_counts().index, y=df["Sentiment"].value_counts().values, palette=colors, ax=ax)
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
st.pyplot(fig)

#Display Tweets
st.subheader("Tweets")
st.dataframe(df[["Tweet", "Sentiment"]])
