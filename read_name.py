import re

# Read the HTML file
with open('baby2008.html', 'r') as f:
    html = f.read()

# Define the regex pattern to extract names
pattern = r'<td>([A-Za-z]+)</td>'

# Find all matches
matches = re.findall(pattern, html)

# Print the names
print(matches)

