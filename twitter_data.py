import requests
import pandas as pd


bearer_token = "AAAAAAAAAAAAAAAAAAAAAN31xwEAAAAA9PqwHwA0OFK21H%2BkRw3nZ7u7w80%3DayxFZXgsA2SzrnYtkEF61XX0tvx7KC8xXtAE0afUT75HRKXmqR"  # Replace with your actual Bearer Token

search_url = "https://api.twitter.com/2/tweets/search/recent"
query = "mental health"  # Search keyword or phrase
max_results = 10  # Max tweets per request

headers = {
    "Authorization": f"Bearer {bearer_token}",
}
params = {
    "query": query,  
    "tweet.fields": "text,created_at",  
    "max_results": max_results,
}

#Make the API request
response = requests.get(search_url, headers=headers, params=params)

if response.status_code == 200:
    tweets = response.json()
    #Process the response and save tweets to a DataFrame
    if "data" in tweets: 
        data = [{"Tweet": tweet["text"], "Created_At": tweet["created_at"]} for tweet in tweets["data"]]
        df = pd.DataFrame(data)

        #Save DataFrame to a CSV file
        df.to_csv("tweets.csv", index=False)
        print("Tweets have been saved to tweets.csv!")
    else:
        print("No tweets found for the given query.")
else:
    print(f"Failed to fetch tweets: {response.status_code} - {response.text}")
