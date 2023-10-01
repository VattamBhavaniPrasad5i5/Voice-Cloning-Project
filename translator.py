from googletrans import Translator, LANGUAGES


def translate_to_telugu(text):
    # Create a Translator object
    translator = Translator()

    # Translate English to Telugu
    translation = translator.translate(text, src="en", dest="te")

    # Return the translated text in Telugu
    return translation.text


def translate_to_hindi(text):
    # Create a Translator object
    translator = Translator()

    # Translate English to Hindi
    translation = translator.translate(text, src="en", dest="hi")

    # Return the translated text in Hindi
    return translation.text


# Example usage:
english_text = "Hello, how are you?"
telugu_translation = translate_to_telugu(english_text)
hindi_translation = translate_to_hindi(english_text)

print("English:", english_text)
print("Telugu:", telugu_translation)
print("Hindi:", hindi_translation)
