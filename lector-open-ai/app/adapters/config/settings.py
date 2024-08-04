import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
ELASTIC_SEARCH_URL = "http://192.168.2.232:9200"
DOCUMENT_AI_API_KEY_CONNECTION = './secret-key-document-ai.json'
OPEN_AI_API_KEY_CONNECTION = 'secret-key-open-ai.json'
