
# **Mental Health Analysis Web Application**

## **Overview**
This project aims to help users analyze the tone, mood, and sentiment of text input in real-time, providing valuable insights into mental health and emotional states. The web application leverages Natural Language Processing (NLP) techniques to classify text into various emotional categories such as Happy, Sad, Angry, and more. This tool can be used to detect underlying emotional trends in text, such as social media posts, messages, or personal reflections.

## **Features**
- **Text Input Box:** Users can enter text to be analyzed for its tone and mood.
- **Sentiment Analysis:** The app analyzes the sentiment of the text and provides a detailed breakdown of the detected mood.
- **Emotional Classification:** Various moods are detected, including happy, sad, neutral, angry, etc.
- **Interactive Data Visualization:** Bar graphs and charts to represent the distribution of detected moods.

## **Technology Stack**
- **Python 3.x**
- **Streamlit**: For creating the web application interface.
- **Natural Language Toolkit (NLTK)**: Used for tokenization, sentiment analysis, and mood detection.
- **Pandas**: For handling and processing data.
- **Matplotlib & Seaborn**: For creating visualizations.
- **Scikit-learn**: For advanced sentiment analysis algorithms.

## **Installation**

### Prerequisites:
To run this project locally, ensure that you have the following installed:
- **Python 3.x**
- **pip** (Python's package installer)

### Install Required Libraries:
```bash
pip install streamlit pandas nltk matplotlib seaborn scikit-learn
```

## **How to Run**

1. Clone the repository:
    ```bash
    git clone https://github.com/Prithyangaa/MENTAL-HEALTH-ANALYSIS.git
    ```

2. Navigate into the project directory:
    ```bash
    cd MENTAL-HEALTH-ANALYSIS
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run dashboard.py
    ```

4. Open the app in your browser at [localhost:8501](http://localhost:8501).

## **Live Demo**
You can access the live version of the web application using the following link:  
[**Mental Health Analysis Web App**](https://mental-health-analysis-c8dbb3c86lc9zpxjdc3zva.streamlit.app/)

## **Usage Instructions**
- Once the app is running, simply type or paste any text in the provided text box.
- Click on the **Analyze** button to view the mood and sentiment analysis of the entered text.
- The application will display the emotional classification and sentiment breakdown along with a bar chart for easier interpretation.

## **Contributing**
Feel free to contribute to this project. To get started:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a pull request.

## **Licenses**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
