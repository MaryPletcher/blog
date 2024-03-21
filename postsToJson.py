import os
import json
import re

# Define the path to the folder containing Markdown files
markdown_folder = "posts"

# Define an empty list to store post data
posts = []

# Iterate through each Markdown file in the folder
for filename in os.listdir(markdown_folder):
    if filename.endswith(".md"):
        # Read the contents of the Markdown file
        with open(os.path.join(markdown_folder, filename), "r") as file:
            content = file.read()

        # Extract title, body, and date from the Markdown content
        title_match = re.search(r"title:\s*(.*)", content)
        body_match = re.search(r"body:\s*(.*?)\ndate:", content, re.DOTALL)
        date_match = re.search(r"date:\s*(.*)", content)

        if title_match and body_match and date_match:
            title = title_match.group(1).strip()
            body = body_match.group(1).strip()
            date = date_match.group(1).strip()

            # Create a dictionary representing the post and append it to the posts list
            post = {
                "title": title,
                "content": body,
                "date": date
            }
            posts.append(post)

# Write the posts list to a JSON file
with open("posts.json", "w") as json_file:
    json.dump(posts, json_file, indent=2)
