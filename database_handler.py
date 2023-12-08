```python
import pymongo

class DatabaseHandler:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["blog_db"]
        self.new_posts = self.db["new_posts"]
        self.summarized_posts = self.db["summarized_posts"]
        self.rewritten_posts = self.db["rewritten_posts"]

    def store_posts(self, posts):
        for post in posts:
            if not self.new_posts.find_one({"_id": post["_id"]}):
                self.new_posts.insert_one(post)

    def fetch_new_posts(self):
        return [post for post in self.new_posts.find({"summarized": "N"})]

    def store_summarized_posts(self, posts):
        for post in posts:
            if not self.summarized_posts.find_one({"_id": post["_id"]}):
                self.summarized_posts.insert_one(post)
                self.new_posts.update_one({"_id": post["_id"]}, {"$set": {"summarized": "Y"}})

    def fetch_summarized_posts(self):
        return [post for post in self.summarized_posts.find()]

    def store_rewritten_posts(self, posts):
        for post in posts:
            if not self.rewritten_posts.find_one({"_id": post["_id"]}):
                self.rewritten_posts.insert_one(post)

    def fetch_rewritten_posts(self):
        return [post for post in self.rewritten_posts.find()]
```