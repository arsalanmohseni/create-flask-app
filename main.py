from os import system

print("Hi !")


def main() -> None:
    print("Installing pipenv...")
    system("pip install pipenv")
    print("Pipenv installed successfully.")
    system("mkdir {name}")
    system("cd {name}")
    with open("main.py", "w") as f:
        f.write(
            "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run(debug=True)"
        )
    print("Creating virtual environment...")
    system("pipenv shell")
    print("Virtual environment created successfully.")
    print("Installing requirements...")
    system("pipenv install flask")
    print("Requirements installed successfully.")
    print("Installing is succesfully done!")
    print("Creating a new Flask app...")
    name = input("Enter the name of the app: ")
    print("Flask app created successfully.")
    print("Flask app is ready to use!")
    print("You can now run the app using the command 'pipenv run python main.py'")
    print("Thanks for using create-flask-app!")


if __name__ == "__main__":
    main()
