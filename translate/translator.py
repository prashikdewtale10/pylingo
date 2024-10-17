"""
translator.py
-------------
@author: Prashik Dewtale

"""

from googletrans import Translator


class PyLingoTranslator:
    """
    A simple translator class that provides translation functionality for 
    Marathi and Hindi using the Google Translate API.

    Methods
    -------
    translate(text: str, dest_language: str) -> str
        Translates the given text into the specified destination language.
    
    translate_to_hindi(text: str) -> str
        Translates the given text into Hindi.
    
    translate_to_marathi(text: str) -> str
        Translates the given text into Marathi.
    """
    
    def __init__(self):
        """
        Initializes the PyLingoTranslator class with a Google Translate API Translator.
        """
        self.translator = Translator()

    def translate(self, text: str, dest_language: str) -> str:
        """
        Translates the given text to the destination language ('hi' for Hindi or 'mr' for Marathi).

        Parameters
        ----------
        text : str
            The text that needs to be translated.
        dest_language : str
            The target language code ('hi' for Hindi, 'mr' for Marathi).

        Returns
        -------
        str
            The translated text.

        Raises
        ------
        ValueError
            If the input text is empty or if the destination language is not 'hi' or 'mr'.
        RuntimeError
            If the translation fails due to any other errors from the API.
        """
        if not text:
            raise ValueError("Input text cannot be empty.")
        
        # Todo: making languages list configurable
        if dest_language not in ["hi", "mr"]:
            raise ValueError("Destination language must be 'hi' for Hindi or 'mr' for Marathi")
        
        try:
            translation = self.translator.translate(text, dest=dest_language)
            return translation.text
        except Exception as e:
            raise RuntimeError(f"Translation failed: {e}")
    
    def translate_to_hindi(self, text: str) -> str:
        """
        Translates the given text to Hindi.

        Parameters
        ----------
        text : str
            The text that needs to be translated.

        Returns
        -------
        str
            The translated text in Hindi.
        """
        return self.translate(text, 'hi')
    
    def translate_to_marathi(self, text: str) -> str:
        """
        Translates the given text to Marathi.

        Parameters
        ----------
        text : str
            The text that needs to be translated.

        Returns
        -------
        str
            The translated text in Marathi.
        """
        return self.translate(text, 'mr')

    # Batch translation feature can be implemented here
