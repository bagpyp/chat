import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.organization = "org-kctmVuxoQeFXrW8GJiicb5zI"
openai.api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    openai.Model.list()