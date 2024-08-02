class ExampleRepository:
    def __init__(self):
        self.data = {}

    def save(self, key: str, value: str):
        self.data[key] = value

    def get(self, key: str) -> str:
        return self.data.get(key, None)
