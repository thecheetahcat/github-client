from actions import initialize_repository as ir
import sys


def exit_client():
    print("Thank you.")
    sys.exit(0)


def main():
    options = {
        "1": ir.create_new_repository,
        "2": exit_client,
        # ... add more options as you create more actions
    }

    while True:
        print("\nGitHub Client Menu:")
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_', ' ').title()}")

        choice = input("\nEnter your choice: ").strip()
        action = options.get(choice)
        if action:
            action()
        elif choice == "exit":
            exit_client()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
