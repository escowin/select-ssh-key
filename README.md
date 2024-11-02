Here’s the updated documentation to reflect the new features and changes in the code, including the selection of Git operations, email authorship, and copying the full command to the clipboard.

---

## Documentation: SSH Key Selection and Git Operation Script for GitHub Repositories

### Overview

This Python script assists in managing multiple SSH keys, setting Git author email, selecting operations, and targeting branches for GitHub repositories. It is useful for switching between GitHub accounts (e.g., personal and work) or managing separate repositories that require different SSH keys.

The script lists available SSH keys in your `.ssh` directory, prompts for an email address to set as the Git author, lets you select a Git operation (e.g., `pull`, `push`), and specifies a branch. It then constructs and copies a combined command to your clipboard for easy pasting and execution.

### Why This Script is Helpful

When working with multiple GitHub accounts or repositories, each associated with a unique SSH key, switching between them can be cumbersome. This script provides an efficient way to choose the correct SSH key, set an author email, specify a Git operation, and pick a branch, all in one go without needing to reconfigure global SSH settings or Git settings.

#### Common Scenarios
- **Separate GitHub Accounts**: Easily switch between SSH keys for accessing personal and work GitHub accounts.
- **Key-Specific Repositories**: Use the correct SSH key, Git operation, and branch to avoid authentication or history issues.
- **Email Authorship**: Set the Git author email dynamically, which is especially useful when contributing across multiple accounts.

### Requirements

- **Python 3**: Ensure Python 3 is installed.
- **Configured SSH Keys**: You must have SSH keys stored in your `.ssh` directory. This script automatically excludes `.pub` files (public keys).

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

4. **Select the Git Author Email**:
   - Choose the email address you’d like to set as the author for this session.
   - The script includes a list of emails that can be customized in the `EMAILS` variable.

5. **Specify the Git Operation**:
   - After selecting the SSH key and email, you’ll be prompted to enter the Git operation you want to perform (`pull`, `push`, or `fetch`).

6. **Choose the Branch**:
   - You’ll be prompted to select a branch:
     - `main`
     - `develop`
     - `other` (enter a custom branch name when prompted)

7. **Copy and Paste the Command**:
   - On Windows, the SSH command is copied to the clipboard in the format:
     ```plaintext
     GIT_SSH_COMMAND="ssh -i <ssh_key_path>" git <operation> origin <branch>
     ```
   - Paste this command into your terminal with `Ctrl + V` (or `Cmd + V` on macOS) to execute it directly.

### Example

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
  3. other
Enter the number of the branch: 3
Enter the branch name: feature/new-feature

SSH key:             C:/Users/username/.ssh/id_rsa_work
Git author email:    work@example.com
Git operation:       git pull

Run the following command to use this SSH key and git operation:
GIT_SSH_COMMAND="ssh -i C:/Users/username/.ssh/id_rsa_work" git pull origin feature/new-feature

The SSH command has been copied to the clipboard. You can now paste it into the terminal.

```

These two commands streamline work across multiple repositories and accounts.

### Notes

- **Windows Users**: The combined command is automatically copied to the clipboard.
- **Cross-Platform Compatibility**: The script works on macOS and Linux as well; on these systems, copy the command manually from the terminal.

### Troubleshooting

- **SSH Key Not Recognized**: Make sure the selected SSH key is registered with your GitHub account. Add or manage SSH keys on GitHub under **Settings > SSH and GPG keys**.
- **Access Denied Errors**: If you see `Permission denied (publickey)`, verify you’re using the correct SSH key for the intended GitHub account.

This script simplifies the management of multiple SSH keys, Git operations, and author emails, making it easy to work across multiple accounts and repositories without modifying global configurations.