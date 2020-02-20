# app/robo_advisor.py

# import my packages
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")
SYMBOL = "TSLA" #todo: ask for a user input

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #get a USD value here

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={SYMBOL}&apikey={API_KEY}"
print("URL:", request_url)

response = requests.get(request_url)
print(type(response))

print(dir(response))
print(response.status_code)
print(response.text)

# if symbol or API key is wrong
if "Error Message" in response.text:
    print("OOPS couldn't find that symbol, please try again")
    exit()

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Meta Data"]["Time Series (Daily)"]["2019-02-02"]["4. close"]

print(type(parsed_response)) #> dict

















print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")