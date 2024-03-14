import requests
import time

API_URL = "https://api.coincap.io/v2/assets"


def get_all_coins():
    try:
        r = requests.get(API_URL)
        if r.status_code == 200:
            data = r.json()
            names = [i["name"] for i in data["data"]]
            print("\n".join(names))
    except requests.RequestException as e:
        print("Error getting data: ", e)


def get_coin_info(coin_name):
    try:
        url = f"{API_URL}/{coin_name}"
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()["data"]
    except requests.RequestException as e:
        print(f"Error getting data for {coin_name}: {e}")
    return None


def get_all_coins_rates():
    try:
        r = requests.get(API_URL)
        if r.status_code == 200:
            data = r.json()
            for coin in data["data"]:
                print(f"\n{coin['name']} : {coin['priceUsd']} USD")
    except requests.RequestException as e:
        print("Error getting data: ", e)


def get_specific_coin_data():
    coin_name = input("Enter coin`s name: ").lower()
    coin_data = get_coin_info(coin_name)
    write_log("Get specific coin data", f"Coin name: {coin_name}")
    if coin_data:
        keys_of_interest = [
            "name",
            "rank",
            "symbol",
            "supply",
            "maxSupply",
            "marketCapUsd",
            "volumeUsd24Hr",
            "changePercent24Hr",
            "vwap24Hr",
        ]
        for key in keys_of_interest:
            print(f"\n{key} : {coin_data.get(key)} ")


def get_specific_coin_rate():
    coin_name = input("Enter coin`s name: ").lower()
    coin_data = get_coin_info(coin_name)
    write_log("Get specific coin rate", f"Coin name: {coin_name}")
    if coin_data:
        print(f"\n{coin_data['name']} rate is {coin_data['priceUsd']} USD")


def write_log(action, details):
    current_time = time.time()
    log_filename = f"log_{int(current_time)}.txt"
    with open(log_filename, "a") as f:
        f.write(f"{action}: {details}\n")


def main():
    user_name = input("Enter your name: ")
    print(f"\nHello {user_name}!")
    while True:
        print("\nMenu")
        print("1. Get all coins")
        print("2. Get all coins rate")
        print("3. Get specific coin data")
        print("4. Get specific coin rate")
        print("5. Quit")

        choice = input("\nChoose the number from the list: ")

        if choice == "1":
            get_all_coins()
            write_log("Get all coins", "No additional details")
        elif choice == "2":
            get_all_coins_rates()
            write_log("Get all coins", "No additional details")
        elif choice == "3":
            get_specific_coin_data()
        elif choice == "4":
            get_specific_coin_rate()
        elif choice == "5":
            print(f"\nBye, {user_name}!")
            write_log("Quit", "No additional details")
            break
        else:
            print("\nWrong number was entered")


if __name__ == "__main__":
    main()
