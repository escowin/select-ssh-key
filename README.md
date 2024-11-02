## Documentation: SSH Key Selection and Git Operation Script for GitHub Repositories

### Table of Contents

1. [Overview](#overview)
2. [Why This Script is Helpful](#why-this-script-is-helpful)
3. [Requirements](#requirements)
4. [How to Use the Script](#how-to-use-the-script)
   - [Run the Script](#run-the-script)
   - [Optional: Create a Desktop Shortcut](#optional-create-a-desktop-shortcut)
   - [Example Usage](#example-usage)
5. [Troubleshooting](#troubleshooting)

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

- **Double-click the `.cmd` file** to open a terminal or run `python select-ssh-key.py`` to execute the script.
- Follow the prompts to:
  - Select an SSH key
  - Choose a Git author email
  - Specify the Git operation and branch
- The script will copy the SSH command to your clipboard (on Windows), making it easy to paste and run in your terminal.

#### Optional: Create a Desktop Shortcut

- **Right-click** on the `.cmd` file and select **Create Shortcut**.
- **Move the shortcut** to your desktop for one-click access to the script.

#### Example Usage

1. **Run the `.cmd` file**: Double-click `run-select-ssh-key.cmd` to start.
2. **Follow the Prompts**:
   - Select an SSH key by number.
   - Choose an email address from a predefined list.
   - Enter the Git operation (e.g., `pull`, `push`) and specify the branch.
3. **Copy and Paste**: The script generates and copies a combined command to your clipboard in the format:
   ```plaintext
   set email command; git ssh command
   ```
   Paste this into your terminal to set the email and execute the Git command in one step.

### Troubleshooting

- **Python Path Issues**: Ensure Python is added to your system PATH, so the `python` command works from any directory.
- **SSH Key Not Recognized**: Verify that the selected SSH key is registered with your GitHub account (Settings > SSH and GPG keys).
- **Access Denied Errors**: If you see `Permission denied (publickey)`, confirm that you’re using the correct SSH key for the intended GitHub account.

With the `.cmd` file and optional desktop shortcut, running this tool becomes quick and convenient, making it ideal for users managing multiple GitHub accounts or repositories.
