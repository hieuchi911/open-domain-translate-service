# Translate-Service
Sanic translate service at CT Group.

This repo stores sanic app for translation (between Vietnamese and English) models:
- app.py deploys NlpHUST model
- app_opus.py deploys Helsinki-NLP model
- AND an extra notebook for loading and testing the models (NlpHUST model, Helsinki-NLP model, Facebook mBart), as well as testing services that deploy these models (except for Facebook mBart since its too resource consuming)