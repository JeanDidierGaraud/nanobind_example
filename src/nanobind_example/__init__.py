from .nanobind_example_ext import add, __doc__, Bird
# force load stub (necessary until https://github.com/sphinx-doc/sphinx/issues/7630 is resolved):
from ._nanobind_example_ext_stub import *

from .basic_py_example import repeat, Parrot

class Canary(Bird):
    def yell(self) -> str:
        "The canary speaks loudly."
        return 'CUICUI'

class Macaw(Parrot):
    pass

# If ..automodule doesn't use option :imported-members:, you need to give _all_ explicitly:
#__all__ = ['add', 'repeat', 'Parrot']
