import sys
import requests

# if len(sys.argv) != 2:
#     sys.exit("Missing command-line argument")

try:
    user_input = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r.json()

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin_value_in_usd = response["bpi"]["USD"]["rate_float"]
    total_amount = bitcoin_value_in_usd * user_input
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("RequestException")
