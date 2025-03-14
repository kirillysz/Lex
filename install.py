import os
import subprocess
import sys

def create_virtual_env(env_name = "venv"):
    print("Создание Venv...")

    try:
        subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
        print("Создал успешно")
    except Exception as _err:
        raise _err
    
def activate_virtual_env(env_name = "venv"):
    if os.name == "nt":
        activate_script = os.path.join(env_name, "Scripts", "activate")
    else:
        activate_script = os.path.join(env_name, "bin", "activate")


    print("Активация Venv")

    try:
        subprocess.run([activate_script], shell=True, check=True)
        print(f"Venv '{env_name}' активировано.")
    except Exception as _err:
        raise _err
    
def install_requirements(requirements_file = "requirements.txt"):
    print(f"Установка зависимостей из файла '{requirements_file}'")

    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_file], check=True)
        print(f"Зависимости установлены.")
    except Exception as _err:
        raise _err
    
def main():
    env_name = "venv"
    requirements_file = "requirements.txt"

    activate_virtual_env(env_name)
    install_requirements(requirements_file)

if __name__ == "__main__":
    main()