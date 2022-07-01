FROM gitpod/workspace-python-3.9

USER gitpod

ENV POETRY_HOME=/workspace/.poetry
ENV PATH=$POETRY_HOME:$PATH

RUN curl -sSL https://install.python-poetry.org | python3 - 

ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
