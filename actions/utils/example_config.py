from typing import Dict

ACCOUNTS_CONFIG = Dict[str, Dict[str, str]]

ACCOUNTS: ACCOUNTS_CONFIG = {
    "<your-account-name1>":
        {
            "user_name": "<your-user-name>",
            "user_email": "<your-email-address>",
            "host_name": "<your-ssh-config-hostname>"
        },
    "<your-account-name2>":
        {
            "user_name": "<your-user-name>",
            "user_email": "<your-email-address>",
            "host_name": "<your-ssh-config-hostname>"
        },
    "<your-account-name3>":
        {
            "user_name": "<your-user-name>",
            "user_email": "<your-email-address>",
            "host_name": "<your-ssh-config-hostname>"
        },
    # ... you may add more accounts here
}
