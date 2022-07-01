FROM gitpod/workspace-python-3.9

USER root

RUN curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.gpg | sudo apt-key add - 
     && curl -fsSL https://pkgs.tailscale.com/stable/ubuntu/focal.list | sudo tee /etc/apt/sources.list.d/tailscale.list \
     && apt-get update \
     && apt-get install -y tailscale

USER gitpod

ENV POETRY_HOME=/home/gitpod/.poetry
ENV PATH="${POETRY_HOME}/bin":$PATH

RUN curl -sSL https://install.python-poetry.org | python3 - 

ENV POETRY_VIRTUALENVS_CREATE=true
ENV POETRY_VIRTUALENVS_IN_PROJECT=true