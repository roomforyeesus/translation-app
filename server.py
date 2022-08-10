from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    english_text = request.args.get('textToTranslate')
    french_text= translator.englishToFrench(english_text)
    return french_text

@app.route("/frenchToEnglish")
def french_to_english():
    french_text = request.args.get('textToTranslate')
    english_text=translator.frenchToEnglish(french_text)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)