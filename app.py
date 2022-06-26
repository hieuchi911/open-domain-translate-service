from sanic import Sanic, response
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

app = Sanic("NMT-Server")

@app.before_server_start
async def load_model(app):
    global EN_VI_MODEL, EN_VI_TOKENIZER, VI_EN_MODEL, VI_EN_TOKENIZER, DEVICE

    if torch.cuda.is_available():
        DEVICE = torch.device("cuda")

        print('There are %d GPU(s) available.' % torch.cuda.device_count())

        print('We will use the GPU:', torch.cuda.get_device_name(0))
    else:
        print('No GPU available, using the CPU instead.')
        DEVICE = torch.device("cpu")

    # Initialize the tokenizer, model for English to Vietnamese Translation
    EN_VI_MODEL = T5ForConditionalGeneration.from_pretrained("models/t5-en-vi-small")
    EN_VI_TOKENIZER = T5Tokenizer.from_pretrained("models/t5-en-vi-small")
    EN_VI_MODEL.to(DEVICE)

    # Initialize the tokenizer, model for  Vietnamese to English Translation
    VI_EN_MODEL = T5ForConditionalGeneration.from_pretrained("models/t5-vi-en-small")
    VI_EN_TOKENIZER = T5Tokenizer.from_pretrained("models/t5-vi-en-small")
    VI_EN_MODEL.to(DEVICE)



@app.route('/en-to-vi', methods=['POST'])
async def en_to_vi(request):
    global EN_VI_MODEL, EN_VI_TOKENIZER
    src = request.json["text"]
    tokenized_text = EN_VI_TOKENIZER.encode(src, return_tensors="pt").to(DEVICE)
    EN_VI_MODEL.eval()
    summary_ids = EN_VI_MODEL.generate(
                        tokenized_text,
                        max_length=128, 
                        num_beams=5,
                        repetition_penalty=2.5, 
                        length_penalty=1.0, 
                        early_stopping=True)
    output = EN_VI_TOKENIZER.decode(summary_ids[0], skip_special_tokens=True)

    return response.text(output)

@app.route('/vi-to-en', methods=['POST'])
async def vi_to_en(request):
    global VI_EN_MODEL, VI_EN_TOKENIZER, DEVICE
    src = request.json["text"]
    tokenized_text = VI_EN_TOKENIZER.encode(src, return_tensors="pt").to(DEVICE)
    VI_EN_MODEL.eval()
    summary_ids = VI_EN_MODEL.generate(
                        tokenized_text,
                        max_length=256, 
                        num_beams=5,
                        repetition_penalty=2.5, 
                        length_penalty=1.0, 
                        early_stopping=True
                    )
    output = VI_EN_TOKENIZER.decode(summary_ids[0], skip_special_tokens=True)

    return response.text(output)


if __name__ == '__main__':
    app.run()