from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench() -> str:
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    watson_api = translator.create_watson_api()

    return translator.english_to_french(watson_api, textToTranslate)


@app.route("/frenchToEnglish")
def frenchToEnglish() -> str:
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    watson_api = translator.create_watson_api()

    return translator.french_to_english(watson_api, textToTranslate)


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
