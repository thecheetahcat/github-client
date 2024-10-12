# GitHub Account Manager (GHClient)

This Python-based GitHub Account Manager allows you to easily manage multiple GitHub accounts, switch between them, and create new repositories in specified directories. It interacts with the GitHub CLI (`gh`) and helps automate common GitHub operations.

## Features
- Check current GitHub authentication status.
- Switch between multiple GitHub accounts.
- Initialize new repositories in any directory and push them to GitHub.
- Customize repository visibility (public/private).
  
## Prerequisites
This tool is designed for **Linux** and **macOS** systems (although it might work on Windows with adjustments).

Before using this client, ensure that:
- You have Python 3 installed.
- You have the GitHub CLI (`gh`) installed.
- You have SSH keys configured for GitHub.

### Installing the GitHub CLI
To install the GitHub CLI on your system, follow these steps:

#### For Linux (Debian/Ubuntu-based distributions):
1. **Install GitHub CLI via apt**:
    ```bash
    sudo apt update
    sudo apt install gh
    ```

2. **Authenticate with GitHub**:
    Once installed, log into GitHub via the CLI:
    ```bash
    gh auth login
    ```

#### For macOS:
1. **Install GitHub CLI via Homebrew**:
    ```bash
    brew install gh
    ```

2. **Authenticate with GitHub**:
    After installation, log into GitHub:
    ```bash
    gh auth login
    ```

For other operating systems, or if you encounter any issues, refer to the official GitHub CLI documentation: [GitHub CLI Installation Guide](https://cli.github.com/manual/installation)

### Setting Up SSH Keys for GitHub

This tool uses **SSH** to interact with GitHub, so you'll need to set up SSH keys and configure GitHub to accept them.

#### 1. **Generate an SSH Key**
If you haven't already set up an SSH key, generate one with the following command:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Replace `your_email@example.com` with the email address associated with your GitHub account.

When prompted for the location to save the key, you can press Enter to accept the default path (`~/.ssh/id_ed25519`), or specify a custom path if you're managing multiple accounts.

#### 2. Add Your SSH Key to the SSH Agent
Next, you'll need to ensure your SSH agent is running and add your SSH key to the agent:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If you're using a custom key file, replace `~/.ssh/id_ed25519` with the correct path.

#### 3. Add the SSH Key to Your GitHub Account
Copy your SSH key to your clipboard:

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy  # For macOS
cat ~/.ssh/id_ed25519.pub | xclip   # For Linux with xclip installed
```

Then, log into GitHub and navigate to **Settings > SSH and GPG keys**, and click **New SSH key**. Paste your public key and save it.

#### 4. Configure SSH for Multiple GitHub Accounts (Optional)
If you're managing multiple GitHub accounts, you can configure your ~/.ssh/config file to differentiate between them.

Edit (or create) the SSH config file:

```bash
nano ~/.ssh/config
```

Add a configuration for each account:

```bash
Host <your-hostname>
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_<unique-id>

Host <your-hostname>
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_<unique-id>

Host <your-hostname>
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_<unique-id>
```

This setup allows you to use different SSH keys for different GitHub accounts. When adding a remote to a repository, you'd use the hostnames defined here, like so:

```bash
git remote add origin git@<your-hostname>:<username>/<repository>.git
```

#### 5. Test Your SSH Configuration
To ensure everything is set up correctly, you can test the connection with:

```bash
ssh -T git@github.com
```

If you've configured multiple accounts, you can test each one:

```bash
ssh -T git@<your-hostname>
ssh -T git@<your-hostname>
ssh -T git@<your-hostname>
```

You should see a message like:

```bash
Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.
```

Now your system is set up to use SSH with multiple GitHub accounts, and you can easily switch between them using this tool.

## Project Setup

1. **Clone the Repository**:
    Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/gh-client.git
    cd gh-client
    ```

2. **Edit the Configuration File**:
    The configuration file (`config.json`) contains your GitHub accounts. Before running the client, open the file and configure it with your account names and host names:
    
    ```json
    {
      "accounts": [
        {
          "account_name": "<your-account>",
          "host_name": "<your-hostname>"
        },
        {
          "account_name": "<your-account>",
          "host_name": "<your-hostname>"
        },
        {
          "account_name": "<your-account>",
          "host_name": "<your-hostname>"
        }
      ]
    }
    ```

    Replace `example_config.json` with `config.json` and update `account_name` and `host_name` with your actual GitHub accounts.

## Usage

Once the configuration is set, run the program by executing the following command in the terminal:

```bash
python3 main.py
```

### Menu Options
The menu will guide you through the available options:

1. **Check status**: Displays the currently authenticated GitHub accounts and statuses.
2. **Login**: Initiates a login sequence for GitHub accounts via the GitHub CLI.
3. **Activate account**: Allows you to switch between the GitHub accounts specified in the configuration file.
4. **Create new repository**: Initializes a Git repository in a specified directory, creates a new repository on GitHub, and pushes the local repository to GitHub.
5. **Quit**: Exits the program.

### Creating a Repository
When choosing the option to create a new repository, you will be prompted to:

- Specify the directory where the repository should be initialized.
- Provide a name for the new GitHub repository.
- Choose whether the repository should be public or private.
- Enter a commit message.

The program will handle the rest, initializing the repository, adding files, and pushing the initial commit to GitHub.

## Error Handling
If you enter invalid input or encounter errors (such as a directory not existing or an invalid account), the program will guide you with appropriate error messages. It also includes custom exceptions for issues like:

- Directory not found.
- Invalid GitHub account.

## License
This project is open-source under the MIT License.