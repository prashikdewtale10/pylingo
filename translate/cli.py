"""
cli.py
------

Command-line interface (CLI) for PyLingo translation package.

This module provides a command-line interface to interact with the PyLingo \
    translation package.
It allows users to translate text or batch process text files for translation \
    from the terminal,
with support for both Hindi and Marathi as target languages.

Features:
---------
- Translate text directly from the command line using a simple argument format.
- Batch process a text file for translations.
- Automatically detects language and returns the translated output.
- Includes support for multiple translation commands using subparsers.

Usage:
------
Run the PyLingo CLI directly from the terminal by executing the following \
    commands:

Basic translation:
    $ pylingo "Hello world!" --to hi

Batch translation from file:
    $ pylingo --batch path/to/textfile.txt --to mr

Run the Streamlit web app:
    $ streamlit run gui/pylingo_gui.py

Arguments:
----------
- `text`: Text string to be translated.
- `--to`: Specify the target language. Options are 'hi' for Hindi or 'mr' \
          for Marathi.
- `--batch`: Optional. Specify the file path for batch translation from a \
             text file.

Example:
--------
To translate "Good morning" into Hindi:
    $ pylingo "Good morning!" --to hi

To batch translate all text in a file to Marathi:
    $ pylingo --batch translations.txt --to mr

Author:
-------
Prashik Dewtale, 2024

"""


import argparse
import logging
from translate import PyLingoTranslator


# setup logger
logger = logging.getLogger(__name__)


def batch_translate_file_reader(translator: PyLingoTranslator, input_file: str,
                                output_file: str, dest_language: str):
    """
    Reads input from file, translates it, and writes output to another file
    """
    # Reading file contends
    logger.info("Reading input file text")
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        logger.error("File is empty")
        print("Input file is empty.")

    # translate lines
    logger.info("Pefroming batch translations")
    translations = translator.batch_translate(
        texts=lines,
        dest_language=dest_language
    )

    # Writing translations to the output file.
    logger.info("Writing translations to outpur file")
    with open(output_file, 'w', encoding="utf-8") as file:
        for translation in translations:
            file.write(translation + '\n')


def translate_text(translator: PyLingoTranslator, text: str,
                   dest_language: str):
    """Translates a single text to the destination language."""
    if dest_language == "hi":
        translated_text = translator.translate_to_hindi(text=text)
    else:
        translated_text = translator.translate_to_marathi(text=text)
    print(f"Translated text: {translated_text}")


def main():
    """
    Main function for translating text to Hindi or Marathi using command-line \
        arguments.
    The script accepts text input from the user and translates it to the \
        specified
    language ('hi' for Hindi or 'mr' for Marathi) using the \
        `PyLingoTranslator` class.

    Command-line Arguments
    ----------------------
    text : str
        The text to be translated.
    --to : str
        The target language for translation. Must be 'hi' for Hindi or 'mr'\
            for Marathi.
    Example
    -------
    To translate "Hello" to Hindi:
    $ python script.py "Hello" --to hi

    To translate "Hello" to Marathi:
    $ python script.py "Hello" --to mr
    """
    logger.info("Starting the PyLingo CLI.")
    parser = argparse.ArgumentParser(
        description='Translate text to Hindi or Marathi.')
    subparsers = parser.add_subparsers(dest="command",
                                       help="Available commands")
    translator = PyLingoTranslator()

    # subparser for transaling a single text
    translate_parser = subparsers.add_parser(
        'translate', help="Translate a single text")
    translate_parser.add_argument(
        '--text', type="str",
        help="Text to translate", required=True)
    translate_parser.add_argument(
        '--to', type="str", choices=["hi", 'mr'],
        required=True,
        help="Target language: 'hi' for Hindi, 'mr' for Marathi")

    # subparser for batch translating text files
    batch_parser = subparsers.add_parser(
        "batch",
        help="Batch translate from a text file")
    batch_parser.add_argument(
        "--input", type=str, required=True,
        help='Input file for batch translation')
    batch_parser.add_argument(
        "--output", type=str, required=True,
        help='Output file for storing batch translations')
    batch_parser.add_argument(
        '--to', type=str, choices=['hi', 'mr'],
        required=True,
        help="Target language: 'hi' for Hindi, 'mr' for Marathi")

    # Parse the arguments
    args = parser.parse_args()

    if args.command == "translate":
        translate_text(translator, args.text, args.to)
    elif args.command == "batch":
        batch_translate_file_reader(translator, args.input,
                                    args.output, args.to)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
