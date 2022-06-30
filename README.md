# Translate-Service
Sanic translate service at CT Group.

This repo stores sanic app for translation (between Vietnamese and English) models:
- app.py deploys NlpHUST model
- app_opus.py deploys Helsinki-NLP model
- AND an extra notebook for loading and testing the models (NlpHUST model, Helsinki-NLP model, Facebook mBart), as well as testing services that deploy these models (except for Facebook mBart since it consumes a lot resource)

Docker:
- dockerfile in this repo build docker image that holds environment (requirements.txt) for translate and blender bot services, pretrained models are kept (downloaded and stored) in host machine, not in image
- image name: hieuchi911/open-domain-kit