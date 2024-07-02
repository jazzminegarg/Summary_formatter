import re
import sys

# Prompt the user for input
print("Please paste your text below (Press Enter then Ctrl+D or Ctrl+Z on Windows to finish):")

# Read all the input at once
user_input = sys.stdin.read()

# Split the input into lines
lines = user_input.split('\n')

# Process the first line to remove only the brackets


# Regular expression pattern to match anything between brackets and parentheses for other lines
pattern = r'\[.*?\]|\(.*?\)'

# Remove anything between brackets and parentheses in all other lines
cleaned_lines = [re.sub(pattern, '', line) for line in lines[4:]]

# Combine the processed first line and the cleaned remaining lines
cleaned_text = '\n'.join(cleaned_lines)

# Print the cleaned text
print("\nCleaned text:")
print(cleaned_text)
