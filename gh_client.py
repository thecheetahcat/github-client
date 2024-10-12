from gh_client_errors import DirectoryNotFound, InvalidAccount
import subprocess
import os
import sys
from typing import Dict


def run_command(command: str):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")


def exit_client():
    print("Thank you.")
    sys.exit(0)


class GHClient:
    def __init__(self, accounts: Dict[str, str]):
        self.accounts = accounts

    @staticmethod
    def check_status():
        run_command("gh auth status")

    @staticmethod
    def login():
        run_command("gh auth login")

    def activate_account(self):
        try:
            user_account = self.get_valid_account("Choose which account you want to activate:")
        except InvalidAccount:
            print("No valid account found. Exiting.")
            return
        run_command(f"gh auth switch --hostname github.com --user {user_account}")

    def get_valid_account(self, message: str):
        print(message)
        return self.choose_account()

    def choose_account(self, entries: int = 5):
        tries = entries
        self.list_accounts()
        for entry in range(entries):
            user_account = input("Enter the account: ")
            if user_account in self.accounts.keys():
                return user_account
            else:
                tries -= 1
                print(f"Invalid account.\nPlease try again. Attempts remaining: {tries}\n")
        raise InvalidAccount

    def list_accounts(self):
        account_num = 0
        for account, host in self.accounts.items():
            account_num += 1
            print(f"{account_num}. {account}")

    def create_new_repository(self):
        try:
            directory = self.enter_directory()
            user_account = self.get_valid_account("Choose the account to push the repository to:")
            self.setup_and_push_repository(directory, user_account)
        except (DirectoryNotFound, InvalidAccount) as Error:
            print(f"Error creating repository: {Error}")
            return

    @staticmethod
    def enter_directory(entries: int = 5):
        tries = entries
        for entry in range(entries):
            directory = os.path.expanduser(input("Enter the directory to create the repository in: "))
            if os.path.exists(directory):
                return directory
            else:
                tries -= 1
                print(f"Directory: {directory} does not exist.\nPlease try again. Attempts remaining: {tries}\n")
        raise DirectoryNotFound

    def setup_and_push_repository(self, directory: str, user_account: str):
        self.initialize_repository(directory)
        self.add_origin_and_files_to_repository(user_account)
        self.commit_and_push_repository()

    @staticmethod
    def initialize_repository(directory: str):
        # enter the directory and initialize the repository
        os.chdir(directory)
        run_command("git init")

    def add_origin_and_files_to_repository(self, user_account: str):
        # create the repository and, add the origin and files
        while True:
            repo_name = input("Enter the name for the new GitHub repository: ").strip()
            if repo_name:
                break
            print("Repository name cannot be empty. Please try again.")

        while True:
            flag = input("Do want a public or private repository? (public/private): ").strip().lower()
            if flag in ['public', 'private']:
                break
            print("Invalid option. Please enter 'public' or 'private'.")
        run_command(f"gh repo create {repo_name} --{flag}")
        run_command(f"git remote add origin git@{self.accounts[user_account]}:{user_account}/{repo_name}.git")
        run_command("git add .")

    @staticmethod
    def commit_and_push_repository():
        # commit and push the repository
        commit_message = input("Enter the commit message: ")
        run_command(f"git commit -m '{commit_message}'")
        run_command(f"git push -u origin master")

    def menu(self):
        options = {
            "1": self.check_status,
            "2": self.login,
            "3": self.activate_account,
            "4": self.create_new_repository,
            "5": exit_client
        }

        while True:
            print("\nGitHub Account Manager:")
            for key, value in options.items():
                print(f"{key}. {value.__name__.replace('_', ' ').title()}")

            choice = input("\nEnter your choice: ").strip()
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, please try again.")
