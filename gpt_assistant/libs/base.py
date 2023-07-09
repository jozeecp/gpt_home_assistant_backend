import os


class Base:
    def __init__(self):
        self.home_assistant_url = "http://localhost:8123"
        self.home_assistant_jwt = os.environ.get("HOME_ASSISTANT_JWT")
        self.home_assistant_headers = {
            "Authorization": f"Bearer {self.home_assistant_jwt}",
        }
        self.openai_api_key = os.environ.get("OPENAI_API_KEY")
