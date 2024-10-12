from gh_client import GHClient
import os
import json


with open(f"{os.path.dirname(os.path.abspath(__file__))}/config.json", "r") as config_file:
    config_data = json.load(config_file)

ACCOUNTS = {account.get("account_name"): account.get("host_name") for account in config_data.get("accounts", [])}


if __name__ == '__main__':
    client = GHClient(ACCOUNTS)
    client.menu()
