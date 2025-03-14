import requests
import os
import zipfile

def install_vosk_model(model_url="https://alphacephei.com/vosk/models/vosk-model-small-ru-0.4.zip"):
    file_name = 'model.zip'
    model_dir = 'model'

    if os.path.exists(model_dir):
        print(f"Модель уже установлена в '{model_dir}'")
        return

    print(f"Загрузка модели Vosk из '{model_url}'")

    response = requests.get(model_url)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(f"Модель загружена в '{file_name}'")

    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall()
        os.rename("vosk-model-small-ru-0.4", "model")

    print("Модель установлена.")
    os.remove(file_name)