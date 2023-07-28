from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def main():
    print("Translator App")
    print("==============")
    source_lang = "en"  # Source language code (e.g., "en" for English)
    target_lang = "es"  # Target language code (e.g., "es" for Spanish)
    
    while True:
        text = input("Enter text to translate (or 'q' to quit): ")
        if text.lower() == 'q':
            break
        translation = translate_text(text, source_lang, target_lang)
        print(f"Translation: {translation}\n")

    print("Thank you for using the Translator App!")

if __name__ == '__main__':
    main()
