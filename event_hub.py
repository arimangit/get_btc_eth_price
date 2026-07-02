import requests
from exchange_rate import return_exchange_rate
from mailer import send_crypto_email

def get_crypto_exchange_rates():
    usd_to_inr = return_exchange_rate()

    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price",
        params={"ids": "bitcoin,ethereum", "vs_currencies": "usd"}
    )
    response.raise_for_status()
    data = response.json()
    btc_price = float(data["bitcoin"]["usd"])
    eth_price = float(data["ethereum"]["usd"])

    return {
        "bitcoin_dollar": f"Current Bitcoin Price in USDT: ${btc_price:.2f}",
        "bitcoin_inr": f"Current Bitcoin Price in INR: ₹{btc_price * usd_to_inr:.2f}",
        "ethereum_dollar": f"Ethereum Price (USDT): ${eth_price:.2f}",
        "ethereum_inr": f"Ethereum Price in INR: ₹{eth_price * usd_to_inr:.2f}",
        "usd_to_inr": f"USD to INR: ₹{usd_to_inr:.2f}",
    }

if __name__ == "__main__":
    rates = get_crypto_exchange_rates()
    for key, value in rates.items():
        print(value)
    send_crypto_email(rates, recipient="manari.cold001@simplelogin.com", subject="Hello from Python")
