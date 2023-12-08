```python
import os
from database_handler import DatabaseHandler

class MarkdownFormatter:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.posts_folder = "posts"

    def fetch_rewritten_posts(self):
        return self.db_handler.fetch_rewritten_posts()

    def format_post(self, post):
        formatted_post = f"# {post['title']}\n\n{post['content']}"
        return formatted_post

    def write_to_file(self, post, formatted_post):
        filename = f"{post['primary_key']}.md"
        filepath = os.path.join(self.posts_folder, filename)

        with open(filepath, 'w') as file:
            file.write(formatted_post)

    def format_posts(self):
        rewritten_posts = self.fetch_rewritten_posts()

        for post in rewritten_posts:
            formatted_post = self.format_post(post)
            self.write_to_file(post, formatted_post)

if __name__ == "__main__":
    formatter = MarkdownFormatter()
    formatter.format_posts()
```