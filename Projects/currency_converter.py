from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    data = list(data.items())
    data.sort()

    return data
   
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencrSymbol", "")
        print(f"{_id} - {name} - {symbol}")
def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ulrta&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()

    if len(data) == 0:
        print('Invalid currencies!')
        return
    
    rate = list(data.values())[0]
    print(f"{currency1} -> {currency2} = {rate}")

    return 

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print('Invalid amount!')
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    
    return converted_amount

def main():
    currencies = get_currencies()
    print("Welcome to the currenct converter.")
    print("List - list the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchnge rate of two currencies\n")

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount to convert in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to compare: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

main()

# data = get_currencies()
# printer.pprint(data)
# rate = exchange_rate('USA', 'CAD')
# printer.pprint(rate)