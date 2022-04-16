from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    html = translator.translate(textToTranslate, 'en', 'fr')
    return html
    # Write your code here
    return "Translated text to French"

@app.route("/french_to_english")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    html = translator.translate(textToTranslate, 'fr', 'en')
    return html
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
