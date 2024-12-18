.. nanobind_example documentation master file, created by
   sphinx-quickstart on Tue Dec 17 14:55:35 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

nanobind_example documentation
==============================

To build this module and documentation::

  pip install . && ( cd docs; make html; )

::

   tree venv-py312-np2/lib/python3.12/site-packages/nanobind_example
   ├── __init__.py
   ├── __pycache__
   │   ├── __init__.cpython-312.pyc
   │   └── basic_py_example.cpython-312.pyc
   ├── basic_py_example.py
   ├── nanobind_example_ext.abi3.so
   ├── nanobind_example_ext.pyi
   └── py.typed


.. todo::

   Add requirements.txt


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference


.. todolist::
