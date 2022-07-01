# Translate-Service

## I. Notebook ```test-sanic-app.ipynb```:
contains code for:
- loading and testing several Machine Translation (MT) models (NlpHUST model, Helsinki-NLP model, Facebook mBart)
- testing sanic apps that serve MT models (except for Facebook mBart since it consumes a lot resource) and a open-domain-chatbot model on host server (sanic app for open-domain-chatbot can be found at https://github.com/hieuchi911/Blender-Bot-Service)

## II. Other python files:
contain sanic apps that serve MT (between Vietnamese and English) models:
- ```app.py``` serves NlpHUST model
- ```app_opus.py``` serves Helsinki-NLP model

To host these sanic services on host machine, execute the following command:

```python -m sanic <name of file that stores the sanic app, e.g if file named app_opus.py, type 'app_opus'>:<name of Sanic object defined in python file> -H <host address> -p <listening port>```

## III. Docker:
- dockerfile in this repo builds docker image that holds environment (requirements.txt) runnable for both translate and open-domain-chatbot services. Pretrained models are kept (i.e downloaded and stored) in host machine at ```models/``` folder, not in the image
- later, run this image as separate docker containers for translate service and open-domain-chatbot service
- image name: hieuchi911/open-domain-kit