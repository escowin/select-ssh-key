import os
import sys

# Define the SSH directory and project directory
SSH_DIR = os.path.join(os.path.expanduser("~"), ".ssh")

# List available SSH keys in the directory, excluding .pub files
ssh_keys = [f for f in os.listdir(SSH_DIR) if f.startswith("id_rsa") and not f.endswith(".pub")]

# Display SSH key options
print("Select the SSH key file to use:")
for index, key in enumerate(ssh_keys, start=1):
    print(f"  {index}. {key}")

# Prompt the user to select an SSH key
try:
    choice = int(input("Enter the number of the SSH key file: ")) - 1
    if choice < 0 or choice >= len(ssh_keys):
        print("Invalid choice. Exiting.")
        sys.exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    sys.exit(1)

# Get the selected SSH key file path
ssh_key_file = os.path.join(SSH_DIR, ssh_keys[choice])
ssh_key_path = ssh_key_file.replace("\\", "/")

# Prompt the user for the git operation
git_operations = ["pull", "push", "fetch"]
print("Select the git operation to perform:")
for index, operation in enumerate(git_operations, start=1):
    print(f"  {index}. {operation}")

try:
    git_choice = int(input("Enter the number of the git operation: ")) - 1
    if git_choice < 0 or git_choice >= len(git_operations):
        print("Invalid choice. Exiting.")
        sys.exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    sys.exit(1)

# Prompt for branch selection
print("Select the branch to work with:")
print("  1. main")
print("  2. develop")
print("  3. other")

try:
    branch_choice = int(input("Enter the number of the branch: "))
    if branch_choice == 1:
        branch = "main"
    elif branch_choice == 2:
        branch = "develop"
    elif branch_choice == 3:
        branch = input("Enter the branch name: ").strip()
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)
except ValueError:
    print("Invalid input. Please enter a number.")
    sys.exit(1)

# Get the selected git operation
git_operation = git_operations[git_choice]

# Construct the GIT_SSH_COMMAND
GIT_SSH_COMMAND = f'GIT_SSH_COMMAND="ssh -i {ssh_key_path}" git {git_operation} origin {branch}'

print(f"\nUsing SSH key: {ssh_key_path}")
print(f"Selected operation: git {git_operation}")
print("Run the following command to use this SSH key and git operation:")
print(GIT_SSH_COMMAND)

# Copy command to clipboard (for Windows only)
if sys.platform == "win32":
    os.system(f'echo {GIT_SSH_COMMAND.strip()}| clip')
    print("The command has been copied to your clipboard. You can now paste it into your terminal.")
