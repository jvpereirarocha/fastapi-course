## About the project
This project is a simple CRUD project of a task manager application, only for studies purposes.

## Instructions to run
1. Install Python 3.11 to run this project. If you want to manage multiple versions of python, use [pyenv](https://github.com/pyenv/pyenv). Pyenv works like the [NVM](https://github.com/nvm-sh/nvm) on Linux, but for Python language
2. Clone or fork this repository
3. Install poetry. Follow the official documentation to install [here](https://python-poetry.org/docs/)
4. Run the command ```poetry shell``` to create a new virtual environment and the command ```poetry install``` to install all project dependencies
5. Set up the application server with the command ```task run``` or directly with the command ```fastapi dev fast_course/main.py``` provided by Fast API

Notes:
In this project, I'm using the [taskipy](https://github.com/taskipy/taskipy) library to execute common tasks
such as running the suit test and format my files using [ruff](https://docs.astral.sh/ruff/). Feel free to use any tool you want

This repository is a hands-on project of the course [FastAPI do ZERO](https://fastapidozero.dunossauro.com/)
