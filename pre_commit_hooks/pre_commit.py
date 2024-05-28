#!/usr/bin/env python3

import sys
import subprocess

# Define minimum commit message length
MIN_LENGTH = 15

def main():
    # Get the commit message
    commit_message = subprocess.check_output(['git', 'log', '--format=%B', '-n', '1', 'HEAD']).decode().strip()
    
    # Check if the commit message is empty or too short
    if not commit_message:
        print("Error: Commit message cannot be empty.")
        sys.exit(1)
    elif len(commit_message) < MIN_LENGTH:
        print(f"Error: Commit message must have at least {MIN_LENGTH} characters.")
        sys.exit(1)

if __name__ == "__main__":
    main()
