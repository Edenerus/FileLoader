FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV POETRY_HOME /opt/poetry
ENV PATH $POETRY_HOME/bin:$PATH
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VERSION=1.6.1

WORKDIR /app/

COPY poetry.lock .
COPY pyproject.toml .

RUN apt -y update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]

EXPOSE 8000

CMD ["gunicorn", "todolist.wsgi", "-w", "4", "-b", "0.0.0.0:8000"]