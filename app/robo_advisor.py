# app/robo_advisor.py

# import my packages
import requests
import csv
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

# if symbol or API key is wrong
# if "Error Message" in response.text:
   # print("OOPS couldn't find that symbol, please try again")
    #exit()

parsed_response = json.loads(response.text)

#how to get latest day, latest close, recent high and low
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

# assumes first day is on top but consider sorting
dates = list(tsd.keys())

latest_day = dates[0]

latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]

#get the high price from each day
high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))


#maximum of all of the high prices
recent_high = max(high_prices)
recent_low = min(low_prices)



#csv_file_path = "prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means open the file for writing
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    #create a loop and write one for each day

    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
            })


# info output


print("-------------------------")
print("SELECTED SYMBOL: " + SYMBOL)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


