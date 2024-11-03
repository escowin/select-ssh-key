import os
import sys
from datetime import datetime

# Constants
SSH_DIR = os.path.join(os.path.expanduser("~"), ".ssh")
EMAILS = ["personal@example.com", "work@example.com"]
GIT_OPERATIONS = ["pull", "push", "fetch"]
GIT_BRANCHES = ["main", "develop", "feature/*", "other"]

# Startup message
def display_startup_message():
    current_year = datetime.now().year
    print(f"\n:: SSH Key Selection Script ::\n:: © {current_year} Edwin M. Escobar ::\n")

# List available SSH keys in the directory, excluding .pub files
def list_ssh_keys():
    return [f for f in os.listdir(SSH_DIR) if f.startswith("id_rsa") and not f.endswith(".pub")]

# Prompt user to select SSH key
def select_ssh_key(ssh_keys):
    print("Select the SSH key file to use:")
    for index, key in enumerate(ssh_keys, start=1):
        print(f"  {index}. {key}")
    try:
        choice = int(input("Enter the number of the SSH key file: ")) - 1
        if 0 <= choice < len(ssh_keys):
            return os.path.join(SSH_DIR, ssh_keys[choice]).replace("\\", "/")
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

# Prompt user to select email
def select_email():
    print("\nSelect the email address to set for this session:")
    for index, email in enumerate(EMAILS, start=1):
        print(f"  {index}. {email}")
    try:
        choice = int(input("Enter the number of the email address: ")) - 1
        if 0 <= choice < len(EMAILS):
            return EMAILS[choice]
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

# Prompt user to select Git operation
def select_git_operation():
    print("\nSelect the git operation to perform:")
    for index, operation in enumerate(GIT_OPERATIONS, start=1):
        print(f"  {index}. {operation}")
    try:
        choice = int(input("Enter the number of the git operation: ")) - 1
        if 0 <= choice < len(GIT_OPERATIONS):
            return GIT_OPERATIONS[choice]
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

# Prompt user to select branch
def select_branch():
    print("\nSelect the branch to work with:")
    for index, branch in enumerate(GIT_BRANCHES, start=1):
        print(f"  {index}. {branch}")
    try:
        choice = int(input("Enter the number of the branch: ")) - 1
        if 0 <= choice < len(GIT_BRANCHES):
            selected_branch = GIT_BRANCHES[choice]
            
            # Handle "feature/*" selection
            if selected_branch == "feature/*":
                feature_name = input("Enter the feature name: ").strip()
                return f"feature/{feature_name}"
            
            # Handle "other" selection
            elif selected_branch == "other":
                return input("Enter the branch name: ").strip()
            
            # Return standard branch names (e.g., "main", "develop")
            return selected_branch
        else:
            print("Invalid choice. Exiting.")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit(1)

# Display commands and optionally copy to clipboard
def display_commands(ssh_key_path, selected_email, git_operation, branch):
    set_email_command = f'git config user.email "{selected_email}"'
    git_ssh_command = f'GIT_SSH_COMMAND="ssh -i {ssh_key_path}" git {git_operation} origin {branch}'

    print(f"\nSSH key:            {ssh_key_path}")
    print(f"Git author email:   {selected_email}")
    print(f"Git operation:      {git_operation}")
    print(f"Git branch:         {branch}")
    print("\nRun the following command to set the authorship before making a git commit:")
    print(set_email_command)
    print("\nRun the following command to use this SSH key and git operation:")
    print(git_ssh_command)

    # Copy commands to clipboard if on Windows
    if sys.platform == "win32":
        commands_to_copy = {
            "1": ("git set user email", set_email_command),
            "2": ("git ssh command", git_ssh_command),
        }
        copy_to_clipboard(commands_to_copy)

# Prompt user to copy commands to clipboard (Windows only)
def copy_to_clipboard(commands):
    while True:
        print("\nSelect a command to copy to the clipboard:")
        for key, (desc, cmd) in commands.items():
            print(f"  {key}. {desc}")

        selection = input("Enter the number of the command to copy (or press Enter to skip): ").strip()
        if selection in commands:
            command_desc, command = commands[selection]
            os.system(f'echo {command.strip()} | clip')
            print(f"\nCopied {command_desc} to clipboard (Use CTRL+V to paste into terminal).")

            another = input("\nCopy another command? (y/n): ").strip().lower()
            if another != "y":
                break
        else:
            print("Invalid selection or no selection made.")
            break

# Main script execution
if __name__ == "__main__":
    display_startup_message()

    ssh_keys = list_ssh_keys()
    ssh_key_path = select_ssh_key(ssh_keys)
    selected_email = select_email()
    git_operation = select_git_operation()
    branch = select_branch()

    display_commands(ssh_key_path, selected_email, git_operation, branch)

    print("\nExiting.")