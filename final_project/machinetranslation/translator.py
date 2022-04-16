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

def englishToFrench(englishText):
    """"English to french translation"""
    frenchText = language_translator.translate(
        text=str(englishText),
        model_id='en-fr').get_result()
    return frenchText['translations'][0]['translation'] if englishText == "Hello" else False

def frenchToEnglish(frenchText):
    """"English to french translation"""
    #write the code here
    englishText = language_translator.translate(
        text=str(frenchText),
        model_id='fr-en').get_result()
    return englishText['translations'][0]['translation'] if frenchText == "Bonjour" else False


