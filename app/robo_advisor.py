# app/robo_advisor.py

# import my packages
import requests
import csv
import json
import os
import datetime
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="OOPS")

# this is where I will put my functions!

"""
to_usd function formats number in standard USD-formatted strings (ex. $500,000.99)
"""
def to_usd(amount):
    return "${0:,.2f}".format(amount)

"""
compile_url function tests to ensure the function accepts a stock symbol input parameter, and constructs the expected request url.
"""
def compile_url(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    #if symbol or API key is wrong
    if "Error Message" in response.text:
        print("Unfortunately, that stock ticker symbol does not exist in our database. Please try again.")
        exit()
    parsed_response = json.loads(response.text)
    return parsed_response

"""
transform_response function 
"""
def transform_response(parsed_response):
    # parsed_response should be a dictionary representing the original JSON response
    # it should have keys: "Meta Data" and "Time Series Daily"
    tsd = parsed_response["Time Series (Daily)"]

    rows = []
    for date, daily_prices in tsd.items():
        row = {
            "timestamp": date,
            "open": float(daily_prices["1. open"]),
            "high": float(daily_prices["2. high"]),
            "low": float(daily_prices["3. low"]),
            "close": float(daily_prices["4. close"]),
            "volume": int(daily_prices["5. volume"])
        }
        rows.append(row)

    return rows


"""
write_to_csv function writes the information to a csv file
rows should be a list of dictionaries
csv_filepath should be a string filepath pointing to where the data should be written
"""
def write_to_csv(rows, csv_filepath):

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_filepath, "w", newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for row in rows:
            writer.writerow(row)
    return True

"""
create_graph function will create a line graph of the data using matplotlib
"""
def create_graph(high_prices):
    plt.plot(high_prices)
    plt.suptitle('High Prices of the Stock Over Days')
    plt.ylabel('price of the stock')
    plt.xlabel('days')
    plt.show()

"""
the calculations function defines how the recommendation will be calculated
"""
def calculations(latest_close, recent_low):
    difference = (float(latest_close) - float(recent_low))/float(recent_low)
    return difference



# now I must put my if name = main conditional

if __name__ == "__main__":

    #get the input
    SYMBOL = input("Please input a valid stock ticker: ") #the resulting value is a string

    #figure out the length of the input for data validation
    if len(SYMBOL) > 4 or len(SYMBOL) < 1:
        print("Your stock ticker symbol must be between 1-4 characters!")
        exit()

    #figure out if the variable is an integer for error checking
    has_errors = False

    try:
        int_variable = int(SYMBOL)
        has_errors = True
    except:
        pass
    if has_errors == True:
        print("Stock ticker symbol cannot have integers in it!")
        exit()

    # I USE A FUNCTION HERE
    parsed_response = compile_url(SYMBOL)

    # how to get latest day, latest close, recent high and low
    last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

    # I USE ANOTHER FUNCTION HERE
    rows = transform_response(parsed_response)

    latest_close = rows[0]["close"]
    high_prices = [row["high"] for row in rows] # list comprehension for mapping purposes!
    low_prices = [row["low"] for row in rows] # list comprehension for mapping purposes!


    #get the high and low price from each day using min and max
    recent_high = max(high_prices)
    recent_low = min(low_prices)

    #best way to get a CSV file path

    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")
    write_to_csv(rows, csv_filepath)

    #info output
    print("-------------------------")
    print("SELECTED SYMBOL: " + SYMBOL)
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    #datetime function
    today = datetime.datetime.today()
    print("REQUEST AT: " + today.strftime("%Y-%m-%d %I:%M %p"))
    #continue to print the information from the parsed response
    print("-------------------------")
    print(f"LATEST DAY: {last_refreshed}")
    print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print("-------------------------")

    #You are free to develop your own custom recommendation algorithm. This is perhaps one of the most fun and creative parts of this project. 
    #One simple example algorithm would be (in pseudocode):
    #If the stock's latest closing price is less than 20% above its recent low, "Buy", else "Don't Buy".

    #here is the calculation
    difference_floor = .20

    if(calculations(latest_close, recent_low) > difference_floor):
        print("RECOMMENDATION: DO NOT BUY!")
        print("RECOMMENDATION REASON: THE LATEST CLOSE OF THIS STOCK PRICE IS MORE THAN 20% HIGHER THAN ITS RECENT LOW.")
    else:
        print("RECOMMENDATION: BUY!")
        print("RECOMMENDATION REASON: THE LATEST CLOSE OF THIS STOCK PRICE IS LESS THAN 20% HIGHER THAN ITS RECENT LOW.")
    print("-------------------------")
    print(f"WRITING DATA TO CSV: {csv_filepath}")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")

    create_graph(high_prices)