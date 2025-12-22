from pathlib import Path


class Settings:
    def __init__(self, debug=False, database_url="sqlite:///:memory:"):
        self.debug = debug
        self.database_url = database_url
        self.BASE_DIR = Path.cwd().resolve()

    def __repr__(self):
        return f"Settings(debug={self.debug}, database_url='{self.database_url}')"

settings = Settings()