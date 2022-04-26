from sanic import Sanic
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from sanic.response import json


app = Sanic("NMT-Server")

@app.before_server_start
async def load_model(app):
    global EN_VI_MODEL, EN_VI_TOKENIZER, VI_EN_MODEL, VI_EN_TOKENIZER
    # Initialize the tokenizer, model for English to Vietnamese Translation
    EN_VI_TOKENIZER = AutoTokenizer.from_pretrained("models/opus-mt-en-vi")
    EN_VI_MODEL = AutoModelForSeq2SeqLM.from_pretrained("models/opus-mt-en-vi")
    
    # Initialize the tokenizer, model for  Vietnamese to English Translation
    VI_EN_TOKENIZER = AutoTokenizer.from_pretrained("models/opus-mt-vi-en")
    VI_EN_MODEL = AutoModelForSeq2SeqLM.from_pretrained("models/opus-mt-vi-en")


@app.route('/en-to-vi', methods=['POST'])
async def en_to_vi(request):
    global EN_VI_MODEL, EN_VI_TOKENIZER
    text = request.json["text"]
    tokenized_text = EN_VI_TOKENIZER.prepare_seq2seq_batch([text], return_tensors='pt')

    # Perform translation and decode the output
    translation = EN_VI_MODEL.generate(**tokenized_text)
    translated_text = EN_VI_TOKENIZER.batch_decode(translation, skip_special_tokens=True)[0]

    # Print translated text
    print(translated_text)

    return json({'text': translated_text})

@app.route('/vi-to-en', methods=['POST'])
async def vi_to_en(request):
    global VI_EN_MODEL, VI_EN_TOKENIZER
    print("\n\nrequest:", request, "\n\n")
    text = request.json["text"]

    tokenized_text = VI_EN_TOKENIZER.prepare_seq2seq_batch([text], return_tensors='pt')
    translation = VI_EN_MODEL.generate(**tokenized_text)
    translated_text = VI_EN_TOKENIZER.batch_decode(translation, skip_special_tokens=True)[0]

    # Print translated text
    print(translated_text)

    return json({'text': translated_text})


if __name__ == '__main__':
    app.run()