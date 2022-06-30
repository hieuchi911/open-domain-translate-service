# Translate-Service
Sanic translate service at CT Group.

This repo stores sanic app for translation (between Vietnamese and English) models:
- app.py deploys NlpHUST model
- app_opus.py deploys Helsinki-NLP model
- AND an extra notebook for loading and testing the models (NlpHUST model, Helsinki-NLP model, Facebook mBart), and for testing services that deploy translation models (except for Facebook mBart since it consumes a lot resource) along with a blenderbot service

Docker:
- dockerfile in this repo builds docker image that holds environment (requirements.txt) that is runnable for both translate and open-domain-chatbot services. Pretrained models are kept (downloaded and stored) in host machine at ```models/``` folder, not in image.
- later, run this image as separate docker containers for translate service and open-domain-chatbot service
- image name: hieuchi911/open-domain-kit