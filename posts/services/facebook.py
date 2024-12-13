import requests

def fetch_facebook_posts(access_token):
    url = "https://graph.facebook.com/me/posts"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    return {"error": response.json().get("message", "Unable to fetch data.")}
