import argparse
from translate import PyLingoTranslator

def main():
    """
    Main function for translating text to Hindi or Marathi using command-line arguments.

    The script accepts text input from the user and translates it to the specified 
    language ('hi' for Hindi or 'mr' for Marathi) using the `PyLingoTranslator` class.

    Command-line Arguments
    ----------------------
    text : str
        The text to be translated.
    --to : str
        The target language for translation. Must be 'hi' for Hindi or 'mr' for Marathi.
    
    Example
    -------
    To translate "Hello" to Hindi:
    $ python script.py "Hello" --to hi

    To translate "Hello" to Marathi:
    $ python script.py "Hello" --to mr
    """
    parser = argparse.ArgumentParser(
        description='Translate text to Hindi or Marathi.')
    parser.add_argument('text', type=str, help="Text to translate")
    parser.add_argument("--to", type=str, choices=['hi', 'mr'],
                        required=True,
                        help="Target language: 'hi' for Hindi, 'mr' for Marathi")   
    args = parser.parse_args()  
    translator = PyLingoTranslator()
    
    if args.to == 'hi':
        translated_text = translator.translate_to_hindi(args.text)
    else:
        translated_text = translator.translate_to_marathi(args.text)
    
    print(f'Translated text: {translated_text}')


if __name__ == '__main__':
    main()
