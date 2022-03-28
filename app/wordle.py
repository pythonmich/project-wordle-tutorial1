from letter_state import LetterState


class Wordle:

    MAX_ATTEMPTS: int = 6
    WORD_LENGTH: int = 5 

    def __init__(self, secret: str) -> None:
        self.secret: str = secret.upper()
        self.attempts = []
    
    def add_attempt(self, word: str) -> None:
        self.attempts.append(word)

    # when we use it we don't have to make a function call
    @property
    def is_solved(self) -> bool:
        # self.attempts[len(self.attempts)-1]
        return len(self.attempts).__gt__(0) and self.attempts[len(self.attempts)-1].__eq__(self.secret)
    
    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)
        
    @property
    def can_attempt(self) -> bool:
        return self.remaining_attempts.__gt__(0) and not self.is_solved

    def guess(self, word: str) -> None:
        results = []

        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character=character)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character.__eq__(self.secret[i])
            results.append(letter)

        return results