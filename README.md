## Documentation: SSH Key Selection and Git Operation Script for GitHub Repositories

### Table of Contents

- [Overview](#overview)
- [Why This Script is Helpful](#why-this-script-is-helpful)
- [Requirements](#requirements)
- [How to Use the Script](#how-to-use-the-script)
  - [Run the Script](#run-the-script)
  - [Optional: Create a Desktop Shortcut](#optional-create-a-desktop-shortcut)
  - [Example Usage](#example-usage)
- [Troubleshooting](#troubleshooting)

---

### Overview

This Python-based tool helps manage multiple SSH keys for GitHub, select Git operations, and specify branches—all within a single workflow. It’s especially useful if you have separate GitHub accounts or repositories requiring different SSH keys.

The repository includes a `.cmd` file for Windows, allowing you to run the Python script easily. Additionally, you can create a desktop shortcut for one-click access.

### Why This Script is Helpful

Switching between multiple GitHub accounts or specific repositories often requires different SSH keys. This tool enables you to:

- Select an SSH key from your `.ssh` directory
- Set a Git author email address dynamically
- Choose a Git operation and specify a branch

The `.cmd` file allows for quick execution of the Python script, making it simple to run this tool whenever needed.

### Requirements

- **Python 3**: Ensure Python 3 is installed on your system.
- **Configured SSH Keys**: You must have SSH keys in your `.ssh` directory, with names starting with `id_rsa`.

### How to Use the Script

#### Run the Script

- **Double-click the `.cmd` file** to open a terminal or run `python select-ssh-key.py` to execute the script.
- Follow the prompts to:
  - Select an SSH key
  - Choose a Git author email
  - Specify the Git operation and branch
- On Windows, the script will prompt you to copy each command individually to your clipboard for easy pasting into the terminal with CTRL+V.

#### Optional: Create a Desktop Shortcut

- **Right-click** on the `.cmd` file and select **Create Shortcut**.
- **Move the shortcut** to your desktop for one-click access to the script.

#### Example Usage

```plaintext
$ python select_ssh_key.py
Select the SSH key file to use:
  1. id_rsa_personal
  2. id_rsa_work
Enter the number of the SSH key file: 2

Select the email address to set for this session:
  1. personal@example.com
  2. work@example.com
Enter the number of the email address: 2

Select the git operation to perform:
  1. pull
  2. push
  3. fetch
Enter the number of the git operation: 1

Select the branch to work with:
  1. main
  2. develop
  3. feature/*
  4. other
Enter the number of the branch: 3
Enter the feature name: feature/new-feature

SSH key:             C:/Users/username/.ssh/id_rsa_work
Git author email:    work@example.com
Git operation:       pull
Git branch:          feature/new-feature

Run the following command to set the authorship before making a git commit:
git config user.email "work@example.com"

Run the following command to use this SSH key:
GIT_SSH_COMMAND="ssh -i C:/Users/username/.ssh/id_rsa_work" git pull origin feature/new-feature

# Windows only
Select a command to copy to the clipboard:
  1. git set user email
  2. git ssh command
Enter the number of the command to copy (or press Enter to skip): 1

Copied git set user email to clipboard (Use CTRL+V to paste into terminal).

Copy another command? (y/n): y

Select a command to copy to the clipboard:
  1. git set user email
  2. git ssh command
Enter the number of the command to copy (or press Enter to skip): 2

Copied git ssh command to clipboard (Use CTRL+V to paste into terminal).

Copy another command? (y/n): n

Exiting.
```

These dynamically generated commands allows custom Git command executions with minimal effort.

### Troubleshooting

- **Python Path Issues**: Ensure Python is added to your system PATH, so the `python` command works from any directory.
- **SSH Key Not Recognized**: Verify that the selected SSH key is registered with your GitHub account (Settings > SSH and GPG keys).
- **Access Denied Errors**: If you see `Permission denied (publickey)`, confirm that you’re using the correct SSH key for the intended GitHub account.

With the `.cmd` file and optional desktop shortcut, running this tool becomes quick and convenient, making it ideal for users managing multiple GitHub accounts or repositories.
