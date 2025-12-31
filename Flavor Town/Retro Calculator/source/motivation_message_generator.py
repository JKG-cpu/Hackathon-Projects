from .settings import *

class MMGenerator:
    def __init__(self, file_path: str) -> None:
        self.MessageLoader = MessageLoader(file_path)
        self.data = self.MessageLoader.data.split("\n")
    
    def get_random_quote(self) -> str:
        return random.choice(self.data)