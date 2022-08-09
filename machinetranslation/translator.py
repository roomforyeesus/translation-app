import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    with open(englishText) as glossary:
        frenchText = language_translator.create_model(
            base_model_id = 'en-fr',
            forced_glossary = glossary,
            name = 'custom-en-fr'
            ).get_result()
        print(json.dumps(frenchText, indent=2))
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    with open(frenchText) as glossary:
        englishText = language_translator.create_model(
            base_model_id = 'fr-en',
            forced_glossary = glossary,
            name = 'custom-fr-en'
            ).get_result()
        print(json.dumps(englishText, indent=2))
    return englishText