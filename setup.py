from setuptools import setup, find_packages

setup(
    name="create-flask-app",
    version="1.0.0",
    packages=find_packages(),
    license="MIT",
    author="Arsalan Mohseni",
    author_email="arsalandeveloper961@gmail.com",
    description="A Python package that makes it easy to create a new Flask app.",
    long_description=open("README.md").read(),
    url="https://github.com/amsy001/create-flask-app",
    install_requires=[
        "Flask"
    ],
    entry_points={
        "console_scripts": [
            "create-flask-app=create_flask_app.cli:create_flask_app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
