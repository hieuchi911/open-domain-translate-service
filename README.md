# Translate-Service

## I. Notebook `test-sanic-app.ipynb`:
contains code for:
- loading and testing several Machine Translation (MT) models (NlpHUST model, Helsinki-NLP model, Facebook mBart). Once load model from huggingface, pretrained models will be downloaded and cached in host machine at `models/` folder in this project
- testing sanic apps that serve MT models (except for Facebook mBart since it consumes a lot resource) and a open-domain-chatbot model on host server (sanic app for open-domain-chatbot can be found at https://gitlab.com/ct_group1/chatbot/other-services/Blender-Bot-Service)

## II. Other python files:
contain sanic apps that serve MT (between Vietnamese and English) models:
- `app.py` serves NlpHUST model
- `app_opus.py` serves Helsinki-NLP model

To host these sanic services on host machine, execute following command:
  >```
  > python -m sanic <name of file that stores sanic app, e.g if file named app_opus.py, type 'app_opus'>:<name of Sanic object defined in python file> -H <host address> -p <listening port>
  >```

## III. Docker:
- dockerfile in this repo builds docker image that holds environment (requirements.txt) runnable for both translate and open-domain-chatbot services.
- docker image: hieuchi911/open-domain-kit. Only 2 files needed to build this image: dockerfile and `requirements.txt`.
- to run docker services for translate service:
  - run the image, binding the container's working directory with directory containing sanic app file (e.g in this repo, `app.py` or `app_opus.py`) and `models/` folder for translate service (similarly for open-domain-chatbot service).
  - run sanic service in the container
  - these steps is shown in following example:
    >```
    > sudo docker run --name en-vi-translate -p 8001:8000 -v "./actions/Translate-Service/:/python-docker/" hieuchi911/open-domain-kit python -m sanic app:app -H 0.0.0.0 -p 8000
    >```
    ,where:
    - `-v "./actions/Translate-Service/:/python-docker/"` maps host machine's directory that stores sanic app and `models/` folder (`./actions/Translate-Service/`) with the container's working directory (`/python-docker/`)
    - `python -m sanic app:app -H 0.0.0.0 -p 8000` set up sanic service to listen at port 8000 in the container at container startup
    - `-p 8001:8000` maps port `8000` in container to port `8001` in local machine, so requests from outside should be sent to port `8001`
  - Example above corresponds to following docker-compose service block:
    >```
    >en-vi-translate:
    >    image: "hieuchi911/open-domain-kit:latest"
    >    expose:
    >       - 8001
    >    volumes:
    >       - ./actions/Translate-Service:/python-docker
    >    command: ["python", "-m", "sanic", "app:app", "-H", "0.0.0.0", "-p", "8000"]
    >```
