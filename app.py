from doctest import debug
from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data['text']
        target_lang = data['target_lang']

        translation = translator.translate(text, dest=target_lang)
        translated_text = translation.text

        response = {
            'original_text': text,
            'translated_text': translated_text,
            'source_language': translation.src,
            'target_language': target_lang
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
