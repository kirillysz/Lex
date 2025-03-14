import os
import subprocess
import sys
import requests
import zipfile

def create_virtual_env(env_name="venv"):
    print("Создание Venv...")

    try:
        subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
        print("Создал успешно")
    except Exception as _err:
        raise _err

def activate_and_install(env_name="venv", requirements_file="requirements.txt"):
    if os.name == "nt":
        activate_script = os.path.join(env_name, "Scripts", "activate")
    else:
        activate_script = os.path.join(env_name, "bin", "activate")

    print("Активация Venv и установка зависимостей")

    try:
        if os.name == "nt":
            command = f'{activate_script} && pip install -r {requirements_file}'

            subprocess.run(command, shell=True, check=True)
        else:
            command = f'source {activate_script} && pip install -r {requirements_file}'
            subprocess.run(command, shell=True, executable='/bin/bash', check=True)

        print(f"Зависимости установлены в Venv '{env_name}'.")
    except Exception as _err:
        raise _err

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


def main():
    env_name = "venv"
    requirements_file = "requirements.txt"

    create_virtual_env(env_name)
    activate_and_install(env_name, requirements_file)
    install_vosk_model()


if __name__ == "__main__":
    main()
