```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class WebScraper:
    def __init__(self, blogs):
        self.blogs = blogs

    def get_recent_posts(self):
        new_posts = []
        for blog in self.blogs:
            response = requests.get(blog)
            soup = BeautifulSoup(response.text, 'html.parser')
            posts = soup.find_all('article')
            for post in posts:
                title = post.find('h2').text
                date = post.find('time')['datetime']
                date = datetime.strptime(date, '%Y-%m-%d').date()
                if date == datetime.today().date():
                    primary_key = title[:3].upper() + date.strftime('%d%m%Y')
                    new_posts.append({
                        'primary_key': primary_key,
                        'title': title,
                        'content': post.find('p').text,
                        'date': date,
                        'summarized': 'N'
                    })
        return new_posts
```