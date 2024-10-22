# PyLingo Translator

![PyLingo Logo](./path-to-your-logo.png)

**PyLingo** is a lightweight Python package that helps translate text between languages. In this initial version, it supports translations between **English**, **Hindi**, and **Marathi**, using Google Translate API. PyLingo also offers a command-line interface (CLI) and a web interface for ease of use.

## Features

- **Text Translation**: Translate text between English, Hindi, and Marathi.
- **Batch Translation**: Translate multiple lines or files in one go.
- **Streamlit Web Interface**: A simple web-based UI for translation tasks.
- **Error Handling**: Validation for input text and language selection.
- **Command-Line Interface**: Use PyLingo directly from the terminal for translations.
- **Localization Support**: Provides full localization support in Hindi and Marathi for the UI.

## Installation

You can install PyLingo from [PyPI](https://pypi.org/project/pylingo/) using `pip`:

```bash
pip install pylingo
```

## Usage

### 1. Using PyLingo in Python

To use PyLingo in your Python script:

```python
from pylingo.translator import PyLingoTranslator

translator = PyLingoTranslator()

# Translate text to Hindi
translated_text = translator.translate_to_hindi("Hello, how are you?")
print(translated_text)  # Output: "नमस्ते, आप कैसे हैं?"

# Translate text to Marathi
translated_text = translator.translate_to_marathi("Good morning!")
print(translated_text)  # Output: "शुभ प्रभात!"
```

### 2. Using the Command-Line Interface (CLI)

You can also use PyLingo from the command line:

```bash
pylingo --text "Good morning!" --to hi
```

For batch translation:

```bash
pylingo --batch myfile.txt --to mr
```

### 3. Streamlit Web Interface
To run the web interface using Streamlit:

```bash
streamlit run gui/pylingo_gui.py
```
