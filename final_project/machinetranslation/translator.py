import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Initial parameters / constants
load_dotenv()
APIKEY_WATSON = os.environ['apikey']
URL_WATSON = os.environ['url']
VERSION_WATSON = '2018-05-01'


# Other methods:
def english_to_french(api_watson: LanguageTranslatorV3, english_text: str = '') -> str:
    """Translate from English to French.
    :param api_watson: LanguageTranslatorV3 instance.
    :param english_text: str - Text in English to be translated.
    :return str: Text translated to French
    """
    french_text: str = ''

    if english_text:
        translation = api_watson.translate(
            text=english_text,
            model_id='en-fr'
        ) .get_result()

        # Get only the text:
        french_text = translation['translations'][0].get('translation')

    return french_text


def french_to_english(api_watson: LanguageTranslatorV3, french_text: str = '') -> str:
    """Translate from French to English.
    :param api_watson: LanguageTranslatorV3 instance.
    :param french_text: str - Text in French to be translated.
    :return str: Text translated to French
    """
    english_text: str = ''

    if french_text:
        # Only if text to translate is not null
        translation = api_watson.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()

        # Get only the text:
        english_text = translation['translations'][0].get('translation')

    return english_text


# Watson-related methods ====================================
def create_watson_api() -> LanguageTranslatorV3:
    """Create a LanguageTranslator instance
    :return: LanguageTranslatorV3 object
    """
    # IBM Watson config
    authenticator = IAMAuthenticator(APIKEY_WATSON)

    language_translator = LanguageTranslatorV3(
        version=VERSION_WATSON,
        authenticator=authenticator
    )
    language_translator.set_service_url(URL_WATSON)

    return language_translator


def get_translated_text(translation_response) -> str:
    """Return translated text.
    :param translation_response: Full response from API.
    :return str: Translated text only."""
    return translation_response['translations'][0].get('translation')
# END Watson related =================================


if __name__ == '__main__':
    watson_api = create_watson_api()
