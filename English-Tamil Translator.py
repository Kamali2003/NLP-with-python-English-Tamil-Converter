!pip install googletrans==3.1.0a0

from googletrans import Translator, LANGUAGES

def translate_to_tamil(text):
    try:
        # Initialize the Translator
        translator = Translator()

        # Detect the source language (English)
        detected_lang = translator.detect(text).lang

        # Check if the detected language is English
        if detected_lang == 'en':
            # Translate the text to Tamil
            translation = translator.translate(text, src='en', dest='ta')

            # Return the translated text
            return translation.text
        else:
            # If the source language is not English, return an error message
            return "Source language is not English"

    except Exception as e:
        return f"Translation Error: {str(e)}"

if __name__ == "__main__":
    english_text = "I am happy"

    tamil_translation = translate_to_tamil(english_text)
    print(f"English: {english_text}")
    print(f"Tamil: {tamil_translation}")
