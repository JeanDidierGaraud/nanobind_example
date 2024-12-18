from .nanobind_example_ext import add, __doc__, Bird

from .basic_py_example import repeat, Parrot

class Canary(Bird):
    def yell(self) -> str:
        "The canary speaks loudly."
        return 'CUICUI'

class Macaw(Parrot):
    pass

# If ..automodule doesn't use option :imported-members:, you need to give _all_ explicitly:
#__all__ = ['add', 'repeat', 'Parrot']
