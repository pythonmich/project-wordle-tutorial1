class LetterState:
    def __init__(self, character: str) -> None:
        self.character: str = character
        self.is_in_word: bool = False
        self.is_in_position: bool = False

    def __repr__(self) -> str:
        return f'{self.character} is_in_word: {self.is_in_word} is_in_position: {self.is_in_position}'