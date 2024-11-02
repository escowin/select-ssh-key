## SSH Key Selection and Git Operation Script for GitHub Repositories

### Overview

This Python script assists users in managing multiple SSH keys for GitHub accounts, selecting Git operations, and choosing target branches. It’s ideal for those who need to interact with different GitHub accounts (e.g., personal and work) or switch between various repositories, each requiring different SSH keys.

The script lists available SSH keys in your `.ssh` directory, allows you to choose one by number, and prompts you to specify the Git operation and branch. It then constructs a `GIT_SSH_COMMAND` command based on your selections, making it easy to switch between SSH keys, operations, and branches without reconfiguring global SSH settings.

### Why This Script is Helpful

When managing multiple GitHub accounts, each SSH key is associated with only one account, allowing GitHub to recognize which account you’re using. This script provides an efficient way to choose which SSH key, Git operation, and branch to use for a particular repository without manually updating configurations.

#### Common Scenarios
- **Separate Accounts**: Quickly switch between SSH keys for accessing work and personal GitHub accounts.
- **Key-Specific Repositories**: Ensure you’re using the correct SSH key and Git operation for specific repositories, avoiding authentication or history-related issues.

### Requirements

- **Python 3**: Ensure Python 3 is installed.
- **Configured SSH Keys**: You must have SSH keys stored in your `.ssh` directory. The script automatically excludes `.pub` files (public keys).

### How to Use the Script

1. **Save the Script**: Copy the Python script and save it as `select_ssh_key.py`.
   
2. **Run the Script**:
   Open a terminal and run the script with:
   ```bash
   python select_ssh_key.py
   ```

3. **Choose an SSH Key**:
   - The script lists available SSH keys (those starting with `id_rsa`).
   - Enter the number corresponding to the SSH key you wish to use.

4. **Specify the Git Operation**:
   - After selecting the SSH key, you’ll be prompted to enter the Git operation you want to perform (e.g., `pull`, `push`, `fetch`).
   
5. **Choose the Branch**:
   - You’ll be prompted to select a branch. Options include:
     - `main`
     - `develop`
     - `other`
   - If you select “other,” the script will prompt you to enter the branch name manually.

6. **Copy and Paste the Command**:
   - The script displays the command and copies it to your clipboard (on Windows). Paste the command into your terminal with `Ctrl + V` (or `Cmd + V` on macOS) to execute it.

### Example

```plaintext
$ python select_ssh_key.py
Select the SSH key file to use:
  1. id_rsa_personal
  2. id_rsa_work
Enter the number of the SSH key file: 2
Enter the Git operation (e.g., pull, push, fetch): pull
Select the branch to work with:
  1. main
  2. develop
  3. other
Enter the number of the branch: 3
Enter the branch name: feature/new-feature

Using SSH key: C:/Users/username/.ssh/id_rsa_work
Run the following command to use this SSH key:
GIT_SSH_COMMAND="ssh -i C:/Users/username/.ssh/id_rsa_work" git pull origin feature/new-feature
The command has been copied to your clipboard. You can now paste it into your terminal.
```

The command sets `GIT_SSH_COMMAND` with the selected SSH key, Git operation, and branch, allowing you to execute a custom Git command with minimal effort.

### Notes

- **Windows Users**: The script automatically copies the command to your clipboard.
- **Cross-Platform Compatibility**: This script works on macOS and Linux as well; on these systems, you’ll need to copy the command manually.

### Troubleshooting

- **SSH Key Not Recognized**: Make sure the SSH key you select is registered with your GitHub account. You can add or manage SSH keys on GitHub by going to **Settings > SSH and GPG keys**.
- **Access Denied Errors**: If you see `Permission denied (publickey)`, verify you’re using the correct SSH key for the intended GitHub account.

This script simplifies the management of multiple SSH keys, Git operations, and branch selections, making it easy to work across multiple accounts and repositories without modifying global configurations.