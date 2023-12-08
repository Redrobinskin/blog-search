Shared Dependencies:

1. Variables:
   - `subject_or_industry`: The user's input for a particular subject or industry.
   - `top_blogs`: The top 5 blogs for the given subject or industry.
   - `new_posts`: The most recent posts fetched from the blogs.
   - `summarized_posts`: The summarized version of the new posts.
   - `rewritten_posts`: The rewritten version of the summarized posts.

2. Data Schemas:
   - `Post`: A schema representing a blog post, with fields for the unique primary key, the post content, the date, and the summarized status.
   - `SummarizedPost`: A schema representing a summarized post, with fields for the unique primary key, the summary, the key words, and the sources for further research.
   - `RewrittenPost`: A schema representing a rewritten post, with fields for the unique primary key and the rewritten content.

3. Function Names:
   - `get_user_input()`: Function to request the user's input for a particular subject or industry.
   - `find_top_blogs()`: Function to find the top 5 blogs for a given subject or industry.
   - `scrape_blogs()`: Function to scrape the blogs for the most recent posts.
   - `store_posts()`: Function to store the fetched posts in the database.
   - `fetch_new_posts()`: Function to fetch new posts from the database.
   - `summarize_posts()`: Function to summarize the fetched posts.
   - `get_key_words()`: Function to get the key words from the summarized posts.
   - `rewrite_posts()`: Function to rewrite the summarized posts.
   - `format_posts()`: Function to format the rewritten posts in markdown.
   - `loop_scrape()`: Function to continuously scrape for new posts.

4. Database Tables:
   - `new_posts`: Table to store the fetched posts.
   - `summarized_posts`: Table to store the summarized posts.
   - `rewritten_posts`: Table to store the rewritten posts.

5. File Names:
   - `post1.md`, `post2.md`, `post3.md`, `post4.md`, `post5.md`: Markdown files to store the formatted rewritten posts.

6. Folder Names:
   - `posts`: Folder to store the markdown files.