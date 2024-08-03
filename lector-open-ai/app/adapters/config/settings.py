import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
ELASTIC_SEARCH_URL = os.getenv("ELASTIC_SEARCH_URL", "http://192.168.2.232:9200")
