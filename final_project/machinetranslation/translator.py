"""IBM Translaor"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator("wPcjBoB1XHZT9Og9c2kF5Z5wgSF6ZNFfuvNJUhEIpjP8")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/1f63ba55-aaea-46b7-8134-6b58312c4fdd")

def english_to_french(english_text):
    """"English to french translation"""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation'] if english_text == "Hello" else False

def french_to_english(french_text):
    """"English to french translation"""
    #write the code here
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text['translations'][0]['translation'] if french_text == "Bonjour" else False



print(english_to_french("Hello"))
print(french_to_english("Bonjour"))
print(english_to_french("Hola"))
print(french_to_english("Hola"))
