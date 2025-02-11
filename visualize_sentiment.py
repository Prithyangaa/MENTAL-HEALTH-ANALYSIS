import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the dataset
df = pd.read_csv("tweets_with_sentiment.csv")

#Count the number of each sentiment
sentiment_counts = df["Sentiment"].value_counts()

#Pie Chart - Sentiment Distribution
plt.figure(figsize=(6, 6))
colors = ["green", "red", "gray"]
sentiment_counts.plot(kind="pie", autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Sentiment Distribution")
plt.ylabel("")  # Hide y-label
plt.savefig("sentiment_pie_chart.png")  # Save the chart
plt.show()

#Bar Chart - Sentiment Count
plt.figure(figsize=(6, 4))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette=colors)
plt.title("Count of Sentiment Categories")
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.savefig("sentiment_bar_chart.png")  # Save the chart
plt.show()
