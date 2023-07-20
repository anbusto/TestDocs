Usage
==================

Here some information about PyRIID!

Installation
==================

These instructions assume you meet the following requirements:

- Python version: 3.8 to 3.10
- Operating systems: Windows, Mac, or Ubuntu

A virtual environment is recommended.

Tests and examples are ran via Actions on many combinations of Python version and operating system.
You can verify support for your platform by checking the workflow files.

########
For Use
########

To use the latest version on PyPI (note: changes are currently slower to appear here), run:

.. code-block:: 

    pip install riid


**For the latest features, run:**

.. code-block:: 

    pip install git+https://github.com/sandialabs/pyriid.git@main


################
For Development
################

If you are developing PyRIID, clone this repository and run:

.. code-block:: 

    pip install -e ".[dev]"


**If you have trouble with Pylance resolving imports for an editable install, try this:**

.. code-block:: 

    pip install -e ".[dev]" --config-settings editable_mode=compat
