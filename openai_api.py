```python
import openai
import json

class OpenAI_API:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def find_top_blogs(self, subject_or_industry):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Find the top 5 blogs for {subject_or_industry}",
            temperature=0.5,
            max_tokens=100
        )
        blogs = self._parse_response(response)
        return blogs

    def get_key_words(self, summary):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Summarize the following text in 5 key words: {summary}",
            temperature=0.5,
            max_tokens=10
        )
        key_words = self._parse_response(response)
        return key_words

    def rewrite_post(self, summary, key_words):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Using the summary and key words {key_words}, write a new post based on the following summary: {summary}",
            temperature=0.5,
            max_tokens=500
        )
        rewritten_post = self._parse_response(response)
        return rewritten_post

    def _parse_response(self, response):
        response_json = json.loads(str(response))
        return response_json['choices'][0]['text'].strip()
```