==================
 Module reference
==================

.. sidebar:: Version information

   :Release: |release|
   :Date: |today|


Nanobind automodule example
***************************

.. automodule:: nanobind_example
   :members:
   :imported-members:
   :undoc-members:


.. todo::

   * :py:func:`add`'s documentation does not show up in automodule?
   * add a nb_class


Nanobind autofunction example
*****************************

Explicitly asking for the doc of a specific function works:

.. autofunction:: nanobind_example.add


In ``help(nanobind_example)``, the function appears in the DATA section (?!)::

   DATA
    add = <nanobind.nb_func object>
        add(a: int, b: int) -> int
