import os

def clean_markdown_file(filepath):
    """
    Reads a Markdown file, removes trailing whitespace from each line,
    and overwrites the original file with the cleaned content.

    Args:
        filepath (str): The path to the Markdown file (e.g., 'README.md').
    """
    try:
        # Read all lines from the file
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        cleaned_lines = []
        for line in lines:
            # Remove trailing whitespace (spaces, tabs, newlines) from each line
            cleaned_lines.append(line.rstrip() + '\n')

        # Overwrite the original file with the cleaned content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(cleaned_lines)

        print(f"Successfully cleaned trailing whitespace from '{filepath}'.")
        print("Please commit and push this updated file to GitHub.")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please ensure the file name is correct and you are running the script in the same directory as the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # --- Instructions for Use ---
    print("--- README.md Formatting Fixer ---")
    print("This script will remove extra spaces at the end of lines in your Markdown file.")
    print("This often fixes rendering issues on platforms like GitHub.")
    print("----------------------------------")

    # You can change 'README.md' to the exact name of your file if it's different.
    # For example: filename_to_clean = 'my_project_readme.md'
    filename_to_clean = 'README.md'

    # Call the function to clean the file
    clean_markdown_file(filename_to_clean)
