import requests

def return_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["rates"]["INR"]
