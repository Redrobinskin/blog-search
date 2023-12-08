```python
import openai
from database_handler import DatabaseHandler

class PostSummarizer:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def summarize_posts(self):
        new_posts = self.db_handler.fetch_new_posts()
        for post in new_posts:
            if post['summarized'] == 'N':
                summary = self.get_summary(post['content'])
                key_words = self.get_key_words(summary)
                self.db_handler.store_summarized_post(post['id'], summary, key_words)
                self.db_handler.update_post_as_summarized(post['id'])

    def get_summary(self, content):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=content,
            temperature=0.3,
            max_tokens=100
        )
        return response.choices[0].text.strip()

    def get_key_words(self, summary):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"{summary}\n\nKeywords:",
            temperature=0.3,
            max_tokens=5
        )
        return response.choices[0].text.strip().split(',')

if __name__ == "__main__":
    summarizer = PostSummarizer()
    summarizer.summarize_posts()
```