def repeat(text: str, n: int=2, sep: str=' '):
    """Repeat the text n times.

    Args:
      text: a sentence
      n: the number of repetition
      sep: the separator

    Example:
       >>> repeat('hello', 3)
       'hello hello hello'
    """
    return sep.join([text]*n)

class Parrot:
    """A Parrot :py:func:`repeats <repeat>` what you say."""
    def __init__(self, n: int=1, sep: str=' '):
        """
        Args:
          n: the number of repetition
          sep: the separator
        """
        self._n = n
        self._sep = sep
    def speak(self, text):
        return repeat(text, self._n, self._sep)
    def __call__(self, text):
        return self.speak(text)


if __name__ == '__main__':
    assert repeat('hello') == 'hello hello'
    assert repeat('hello', 3) == 'hello hello hello'
    assert Parrot(3).speak('Polly') == 'Polly Polly Polly'
    assert Parrot(2)('Polly') == 'Polly Polly'
    print('ok')
