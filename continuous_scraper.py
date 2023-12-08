```python
import time
from openai_api import find_top_blogs
from web_scraper import scrape_blogs
from database_handler import store_posts, fetch_new_posts
from post_summarizer import summarize_posts
from post_rewriter import rewrite_posts
from markdown_formatter import format_posts

def loop_scrape(subject_or_industry):
    while True:
        # Step 2: Find top 5 blogs
        top_blogs = find_top_blogs(subject_or_industry)

        for blog in top_blogs:
            # Step 3: Scrape each blog for the most recent posts
            new_posts = scrape_blogs(blog)

            # Step 4: Store these fetched posts in the database
            store_posts(new_posts)

            # Step 5: Fetch these posts from the database and summarize each post
            new_posts = fetch_new_posts()
            summarized_posts = summarize_posts(new_posts)

            # Step 7: Using the summary and each key word, write a new post
            rewritten_posts = rewrite_posts(summarized_posts)

            # Step 8: Fetch any new "rewritten_posts" and format them in markdown
            format_posts(rewritten_posts)

        # Sleep for a while before starting the next iteration
        time.sleep(3600)
```