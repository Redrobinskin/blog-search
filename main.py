```python
from openai_api import find_top_blogs
from web_scraper import scrape_blogs
from database_handler import store_posts, fetch_new_posts
from post_summarizer import summarize_posts
from post_rewriter import rewrite_posts
from markdown_formatter import format_posts
from continuous_scraper import loop_scrape

def get_user_input():
    subject_or_industry = input("Please enter a subject or industry: ")
    return subject_or_industry

def main():
    subject_or_industry = get_user_input()
    top_blogs = find_top_blogs(subject_or_industry)
    new_posts = scrape_blogs(top_blogs)
    store_posts(new_posts)
    while True:
        new_posts = fetch_new_posts()
        if not new_posts:
            top_blogs = loop_scrape(subject_or_industry)
            new_posts = scrape_blogs(top_blogs)
            store_posts(new_posts)
        else:
            summarized_posts = summarize_posts(new_posts)
            rewritten_posts = rewrite_posts(summarized_posts)
            format_posts(rewritten_posts)

if __name__ == "__main__":
    main()
```