import os
import gettext
import streamlit as st
from babel.support import Translations
from translate import PyLingoTranslator

# Initialize the translator
translator = PyLingoTranslator()


# function to load translations
def load_translation(lang_code: str):
    locale_dir = os.path.join(os.path.dirname(__file__), 'locales')
    try:
        translation = gettext.translation('messages', locale_dir,
                                          languages=[lang_code])
        translation.install()
        return translation.gettext
    except FileNotFoundError:
        return gettext.gettext  # Fallback to default (English)
    
# Language selection
st.sidebar.title("Language Selection")
selected_language = st.sidebar.selectbox(label="Select your languag",
                                         options=['English', 'Hindi', 'Marathi'])

# Load appropriate translations based on the selected language
if selected_language == 'English':
    _ = load_translation('en')
elif selected_language == 'Hindi':
    _ = load_translation('hi')
elif selected_language == 'Marathi':
    _ = load_translation('mr')


    
# App title
st.title(_("PyLingo Translator"))

# Text input area and file uploader
st.write(_("Enter text below or upload a file:"))
uploaded_file = st.file_uploader(_("Choose a text file"), type=["txt"])

if uploaded_file is not None:
    # Read the file's content
    text = uploaded_file.readlines()
    st.text_area(_("File content:"), value=text, height=200)
    # translated_text = translator.batch_translate(texts=texts, )
else:
    text = st.text_area(_("Enter the text you want to translate:"), "")

# Language selection
language = st.selectbox(_("Select target language:"), ['Hindi', 'Marathi'])

# Buttons for translating and clearing the input
col1, col2 = st.columns([1, 1])
with col1:
    if st.button(_("Translate")):
        if text:
            if language == 'Hindi':
                if isinstance(text, list):
                    translated_text = translator.batch_translate(
                        texts=text, dest_language='hi')
                else:
                    translated_text = translator.translate_to_hindi(text)
            elif language == 'Marathi':
                if isinstance(text, list):
                    translated_text = translator.batch_translate(
                        texts=text, dest_language='mr')
                else:
                    translated_text = translator.translate_to_marathi(text)
            st.success(f"{_('Translated Text')}: {translated_text}")
        else:
            st.error(_("Please enter some text or upload a file for translation!"))

with col2:
    if st.button(_("Clear")):
        st.rerun()  # Rerun the app to clear the text and reset the interface
