<img src="./logo/logo.png" width="200">


Pythonlings is a multilingual utility to help newcomers learn Python through exercises, with a variety of themes!

## Setup your language

Actually, the following languages are supported:

- en (default)
- pt

To choose your language, just export `PYTHONLINGS_LANGUAGE` with the desired language.
Example:


    export PYTHONLINGS_LANGUAGE=pt

## Install dependencies

    poetry install


## Usage

    poetry shell
    python -m pythonlings start


## Tests

    poetry run pytest
