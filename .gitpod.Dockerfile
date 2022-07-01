FROM gitpod/workspace-python-3.9

USER gitpod

ENV POETRY_HOME=/home/gitpod/.poetry
ENV PATH="${POETRY_HOME}/bin":$PATH

RUN curl -sSL https://install.python-poetry.org | python3 - 

ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true