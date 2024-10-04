FROM python:3.12

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-dev

COPY .env /app/

COPY moneyflowbot /app/moneyflowbot

CMD ["poetry", "run", "python", "moneyflowbot/main.py"]
