import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
# from dotenv import load_dotenv


# load_dotenv()

# apikey = os.environ['apikey']
# url = os.environ['url']


authenticator = IAMAuthenticator('zSQ-Hc4HOrcLX4XolrnJORCGmDd5ayCtJMhmNFjH9ium')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/20da2556-d55a-4a23-ac22-61cc6cb0aad2')

def englishToFrench(english_text):
    """Translates English to French"""
    translation = language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    englishText=translation["translations"][0]["translation"]
    # return frenchtranslation.get("translations")[0].get("translate")
    return englishText
def frenchToEnglish(french_text):
    """Transalates French to English"""
    translation = language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    frenchText=translation['translations'][0]['translation'] 
    return frenchText
# english_to_french("Hello")  