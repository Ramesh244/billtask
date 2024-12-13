import requests

def fetch_twitter_posts(access_token):
    url = "https://api.twitter.com/2/users/me/tweets"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', [])
    return {"error": response.json().get("message", "Unable to fetch data.")}
