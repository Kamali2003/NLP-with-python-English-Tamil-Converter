import asyncio
from googletrans import Translator

async def translate_to_tamil(text="hii"):
    try:
        # Initialize the Translator
        async with Translator() as translator:

            # Detect the source language (English)
            detected = await translator.detect(text)
            detected_lang = detected.lang  

            # Check if the detected language is English
            if detected_lang == 'en':
                tamil  = await translator.translate(text, dest='ta')                
                # kannada = await translator.translate(text, dest='kn')
                # telugu = await translator.translate(text, dest='te')
                # hindi = await translator.translate(text, dest='hi')
                return [tamil.text, kannada.text, telugu.text, hindi.text]
            else:
            return "Source language is not English"
            # print(f"Detected Language: {detected_lang}")
    except Exception as e:
        print(f"Translation Error: {str(e)}")

if __name__ == "__main__":
    english_text = "I am happy"
    translated = asyncio.run(translate_to_tamil(english_text))
    
    print(f"English: {english_text}")
    print(f"Tamil: {translated[0]}")

    # print(translated)