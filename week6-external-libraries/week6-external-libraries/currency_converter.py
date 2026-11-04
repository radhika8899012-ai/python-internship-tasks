import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            rates = data["rates"]
            rate = rates[to_currency.upper()]
            converted = amount * rate

            print("Exchange Rate:", rate)
            print("Converted Amount:", round(converted, 2), to_currency.upper())
        else:
            print("Unable to get exchange rate.")

    except requests.exceptions.RequestException:
        print("Internet connection error!")
    except KeyError:
        print("Invalid currency code!")


amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g. USD): ")
to_currency = input("To currency (e.g. INR): ")

convert_currency(amount, from_currency, to_currency)
