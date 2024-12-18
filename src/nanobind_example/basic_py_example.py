def repeat(text: str, n: int=2, sep: str=' ') -> str:
    """Repeat the text n times.

    Args:
      text: a sentence
      n: the number of repetition
      sep: the separator

    Returns:
      the repeated sentence

    Example:
       >>> repeat('hello', 3)
       'hello hello hello'
    """
    return sep.join([text]*n)

class Parrot:
    """A Parrot :py:func:`repeats <repeat>` what you say."""
    def __init__(self, name: str='Titi', n: int=1, sep: str=' '):
        """
        Args:
          name: the name of this bird
          n: the number of repetition
          sep: the separator
        Example:
           >>> p = Parrot('Polly', 2)
           >>> p('wanna cracker')
           'Polly says: cuicui (wanna cracker wanna cracker)'
        """
        self._name = name
        self._n = n
        self._sep = sep
    def speak(self, text: str) -> str:
        return self._name + " says: cuicui (" + repeat(text, self._n, self._sep) + ")"
    def __call__(self, text):
        return self.speak(text)


if __name__ == '__main__':
    assert repeat('hello') == 'hello hello'
    assert repeat('hello', 3) == 'hello hello hello'
    assert Parrot(3).speak('Polly') == 'Polly Polly Polly'
    assert Parrot(2)('Polly') == 'Polly Polly'
    print('ok')
