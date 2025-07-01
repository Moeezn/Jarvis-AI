# Backend/Translator.py
import requests

def translate_text(text, target_language='en'):
    """
    Translate text to the specified target language using LibreTranslate API
    
    Args:
        text: Text to translate
        target_language: Target language code (e.g., 'fr', 'es', 'ja')
    
    Returns:
        Translated text or error message
    """
    try:
        # Map common language names to codes
        lang_map = {
            'french': 'fr',
            'spanish': 'es',
            'german': 'de',
            'japanese': 'ja',
            'chinese': 'zh',
            'hindi': 'hi',
            'english': 'en',
            'arabic': 'ar',
            'russian': 'ru',
            'portuguese': 'pt',
            'korean': 'ko',
            'urdu': 'ur'
        }
        
        # Convert language name to code if needed
        lang_code = lang_map.get(target_language.lower(), target_language.lower())
        
        # Use LibreTranslate API (public instance)
        url = "https://libretranslate.com/translate"
        payload = {
            'q': text,
            'source': 'auto',
            'target': lang_code,
            'format': 'text'
        }
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        
        translation = response.json().get('translatedText', '')
        return translation if translation else "Translation not available"
    
    except requests.exceptions.RequestException as e:
        return f"Translation service unavailable: {str(e)}"
    except Exception as e:
        return f"Translation error: {str(e)}"