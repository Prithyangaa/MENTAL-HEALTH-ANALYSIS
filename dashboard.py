import streamlit as st
import matplotlib.pyplot as plt
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK's Sentiment Lexicon
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment and determine mood
def analyze_text(text):
    sentiment_scores = sia.polarity_scores(text)
    compound = sentiment_scores["compound"]

    # Mapping compound score to emotions
    if compound >= 0.7:
        mood = "Ecstatic"
    elif compound >= 0.4:
        mood = "Happy"
    elif compound >= 0.1:
        mood = "Content"
    elif -0.1 < compound < 0.1:
        mood = "Neutral"
    elif compound <= -0.1 and compound > -0.4:
        mood = "Worried"
    elif compound <= -0.4 and compound > -0.7:
        mood = "Sad"
    elif compound <= -0.7:
        mood = "Angry"
    else:
        mood = "Unknown"

    # Mood Explanation Dictionary (without emojis for consistency)
    mood_explanation = {
        "Ecstatic": "Your text is highly positive! You seem excited and full of energy.",
        "Happy": "Your text has a positive tone, indicating a good mood or optimism.",
        "Content": "Your message shows mild positivity, suggesting satisfaction and calmness.",
        "Neutral": "Your text does not strongly lean towards any emotion.",
        "Worried": "Your text contains words suggesting slight worry or concern.",
        "Sad": "Your text has negative undertones, indicating sadness or disappointment.",
        "Angry": "Your text expresses strong negative emotions like frustration or anger.",
        "Unknown": "Unable to determine sentiment clearly."
    }

    return mood, mood_explanation[mood], sentiment_scores

# Streamlit UI
st.title("🧠 Mental Health Sentiment Analyzer 💡")
st.write("Enter text to analyze its **tone, mood, and sentiment breakdown.**")

# User input + button
user_input = st.text_area("Type your thoughts:", height=150)
submit_button = st.button("Analyze Mood")

if submit_button and user_input:
    mood, explanation, scores = analyze_text(user_input)

    # Add emojis dynamically for mood
    mood_with_emoji = {
        "Ecstatic": "Ecstatic 🎉",
        "Happy": "Happy 😊",
        "Content": "Content 🙂",
        "Neutral": "Neutral 😐",
        "Worried": "Worried 😟",
        "Sad": "Sad 😞",
        "Angry": "Angry 😡",
        "Unknown": "Unknown 🤔"
    }

    # Display Mood & Explanation
    st.write("## 🎭 Your Mood:")
    st.write(f"**{mood_with_emoji[mood]}**")
    st.write(f"🔍 *{explanation}*")

    # Sentiment Scores Pie Chart
    st.write("### 📊 Sentiment Breakdown:")
    labels = ["Positive 😊", "Negative 😞", "Neutral 😐"]
    values = [scores["pos"], scores["neg"], scores["neu"]]
    colors = ["#66b3ff", "#ff6666", "#99ff99"]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
    ax.axis("equal")
    st.pyplot(fig)
