==================
 Module reference
==================

.. sidebar:: Version information

   :Release: |release|
   :Date: |today|

.. contents::
   :local:



Nanobind autosummary example
****************************

.. currentmodule:: nanobind_example
.. autosummary::

   Parrot
   Bird
   add


Nanobind automodule example
***************************

The module provides a Bird (nanobind) and a Parrot (pure python).

.. automodule:: nanobind_example
   :members:
   :imported-members:
   :undoc-members:
   :show-inheritance:

.. todo::

   * :py:func:`add`'s documentation does not show up in automodule?
   * :py:meth:`Bird` shows self in its prototype
   * :py:meth:`Bird.speak` is ok in autofunction
   * :py:meth:`Bird.speak` does not show prototype?
   * :py:meth:`Bird.speak` does not show the typehints?
   * :py:meth:`Bird.peep` is ok in automodule, but duplicates the function's prototype in ``autofunction`` or ``help(Bird)``.
   * :py:meth:`Bird.peep` does not conform to ``autodoc_typehints = "description"``.
   * :py:meth:`Bird.tweet` behaves like speak (ok in autofunction, ko in automodule).
   * stubs (.pyi, py.typed) did not change anything for sphinx: do I need something more here? Did it improve something in VScode?
   * there's an `open sphinx issue <https://github.com/sphinx-doc/sphinx/issues/7630>`__ to use pyi in sphinx.
   * :py:func:`add` in autosummary is a little messed up


Nanobind autofunction example
*****************************

Explicitly asking for the doc of a specific function works:

.. autofunction:: nanobind_example.add


In ``help(nanobind_example)``, the function appears in the DATA section (?!)::

   DATA
    add = <nanobind.nb_func object>
        add(a: int, b: int) -> int


.. comment
   no-index are just here because it'd make duplicates with the other section

.. autofunction:: nanobind_example.Bird.speak
   :no-index:
.. autofunction:: nanobind_example.Bird.peep
   :no-index:
.. autofunction:: nanobind_example.Bird.tweet
   :no-index:
