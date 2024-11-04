from actions.utils.config import ACCOUNTS
from actions.utils.helpers import run_command
from actions.utils.errors import DirectoryNotFound, InvalidAccount
import os
from typing import Dict


def create_new_repository() -> None:
    """
    Creates a new repository with the correct author.

    :return: None
    """
    directory = _enter_directory()
    account_data = _choose_account()
    _initialize_repository(directory, account_data)
    _add_origin_and_files_to_repository(account_data)
    _commit_and_push_repository()


def _enter_directory(entries: int = 5) -> str:
    tries = entries
    for entry in range(entries):
        directory = os.path.expanduser(input("Enter the directory to create the repository in: "))
        if os.path.exists(directory):
            return directory
        else:
            tries -= 1
            print(f"Directory: {directory} does not exist.\nPlease try again. Attempts remaining: {tries}\n")
    raise DirectoryNotFound


def _choose_account(entries: int = 5) -> Dict[str, str]:
    tries = entries
    _list_accounts()
    for entry in range(entries):
        user_account = input("Enter the account: ")
        if user_account in ACCOUNTS.keys():
            return ACCOUNTS[user_account]
        else:
            tries -= 1
            print(f"Invalid account.\nPlease try again. Attempts remaining: {tries}\n")
    raise InvalidAccount


def _list_accounts() -> None:
    account_num = 0
    for account, data in ACCOUNTS.items():
        account_num += 1
        print(f"{account_num}. {account}")


def _initialize_repository(directory: str, account_data: Dict[str, str]) -> None:
    # enter the directory and initialize the repository
    os.chdir(directory)
    run_command("git init")
    run_command(f'git config user.name "{account_data['user_name']}"')
    run_command(f'git config user.email "{account_data['user_email']}"')


def _add_origin_and_files_to_repository(account_data: Dict[str, str]) -> None:
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
    run_command(f"git remote add origin git@{account_data['user_name']}:{account_data['user_name']}/{repo_name}.git")


def _commit_and_push_repository() -> None:
    # commit and push the repository
    commit_message = input("Enter the commit message: ")
    run_command(f"git commit -m '{commit_message}'")
    run_command(f"git push -u origin master")
