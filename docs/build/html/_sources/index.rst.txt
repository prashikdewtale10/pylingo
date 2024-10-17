Welcome to PyLingo's documentation!
===================================

PyLingo is a simple and intuitive Python package designed to provide seamless text translation between English and two major Indian languages: Hindi and Marathi. This package leverages the Google Translate API to deliver reliable translations, making it easy for developers to integrate multilingual support into their applications.

Key Features
------------

- **Translate to Hindi and Marathi**: PyLingo supports translation from English to Hindi ('hi') and Marathi ('mr'), ensuring high-quality translations for these languages.
- **Simple API**: The PyLingoTranslator class offers a simple and easy-to-use interface with methods for translating text.
- **Command-line Interface**: PyLingo can be used from the command line, enabling quick translations without writing additional code.
- **Error Handling**: Built-in error handling for invalid inputs and translation failures to ensure robustness.

Why PyLingo?
------------

With the growing demand for multilingual applications in India, PyLingo simplifies the task of incorporating language translation for Hindi and Marathi. Whether you're building a website, chatbot, or any other application that requires multilingual support, PyLingo provides a convenient solution.

Installation
------------

To install PyLingo, you can use `pip`. Here’s how to do it:


1. **Install from PyPI** :

   To install the package from PyPI, run:

   .. code-block:: bash

      pip install pylingo

Quick Example
-------------

Here's how you can translate text from English to Hindi or Marathi:

.. code-block:: python

    from pylingo.translator import PyLingoTranslator

    # Create an instance of the translator
    translator = PyLingoTranslator()

    # Translate text to Hindi
    hindi_text = translator.translate_to_hindi("Hello")
    print(hindi_text)

    # Translate text to Marathi
    marathi_text = translator.translate_to_marathi("Hello")
    print(marathi_text)

CLI Usage
---------

You can also use PyLingo from the command line to quickly translate text. 

Example: Translate "Hello" to Hindi:

.. code-block:: bash

    $ python -m pylingo "Hello" --to hi

Example: Translate "Hello" to Marathi:

.. code-block:: bash

    $ python -m pylingo "Hello" --to mr

The `--to` option specifies the target language:
- Use `'hi'` for Hindi
- Use `'mr'` for Marathi

The translation result will be printed directly in the terminal.





.. toctree::
   :maxdepth: 2
   :caption: Contents:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
