```python
import openai
from database_handler import DatabaseHandler

class PostRewriter:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.openai_api_key = "your_openai_api_key"
        openai.api_key = self.openai_api_key

    def get_summarized_posts(self):
        return self.db_handler.fetch_summarized_posts()

    def rewrite_post(self, post):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=post.summary,
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def store_rewritten_post(self, post, rewritten_content):
        rewritten_post = RewrittenPost(
            primary_key=post.primary_key,
            content=rewritten_content
        )
        self.db_handler.store_rewritten_post(rewritten_post)

    def rewrite_posts(self):
        summarized_posts = self.get_summarized_posts()
        for post in summarized_posts:
            rewritten_content = self.rewrite_post(post)
            self.store_rewritten_post(post, rewritten_content)


if __name__ == "__main__":
    rewriter = PostRewriter()
    rewriter.rewrite_posts()
```