from string import ascii_lowercase, punctuation
from abc import ABC, abstractmethod
from exceptions import (
    MinimumLengthException,
    NoDigitException,
    NoLowerCaseException,
    EspecialCharacterException,
)


class Validator(ABC):

    @abstractmethod
    def validate(self, content) -> None:
        """
        This is the interface of the validation interface.
        :param content: the text to be validated
        :return: None if the text is valid or raise an Exception otherwise.
        """


class LengthValidator(Validator):
    def __init__(self):
        self.minimum_length = 8

    def validate(self, content):
        if self.minimum_length > len(content):
            msg = f"Passwords must have at least {self.minimum_length} characters!"
            raise MinimumLengthException(detail=msg)
        return None


class DigitValidator(Validator):
    def __init__(self):
        self.digit_set = {digit for digit in "0123456789"}

    def validate(self, content):
        content_set = {character for character in content}
        if self.digit_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 digit!"
            raise NoDigitException(detail=msg)
        return None


class LowerCaseValidator(Validator):
    def __init__(self):
        self.lower_case_set = {character for character in ascii_lowercase}

    def validate(self, content):
        content_set = {character for character in content}
        if self.lower_case_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 lower case letter!"
            raise NoLowerCaseException(detail=msg)
        return None


class EspecialCharacterValidator(Validator):
    def __init__(self):
        self.especial_set = {character for character in punctuation}

    def validate(self, content):
        content_set = {character for character in content}
        if self.especial_set.isdisjoint(content_set):
            msg = "Passwords must have at least 1 especial character!"
            raise EspecialCharacterException(detail=msg)
        return None