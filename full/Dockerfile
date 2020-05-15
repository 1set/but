FROM 1set/butlite:latest
LABEL maintainer="an9an63@gmail.com"

ARG ROOT_PATH=/root
ARG GO_PATH=/go

ENV GOPATH=${GO_PATH}
ENV GOBIN=${GO_PATH}/bin
ENV PATH=$PATH:$GOBIN

WORKDIR ${ROOT_PATH}

RUN set -eux; \
    apt-get update && apt-get install -y --no-install-recommends gpg-agent ; \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - ; \
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential gcc figlet \
        nodejs \
        golang-go go-dep \
        libssl-dev libffi-dev python3-dev python3-pip python3-setuptools \
        && apt-get clean && rm -rf /var/lib/apt/lists/* ; \
    python3.8 -m pip install -U pip setuptools ; \
    cd /usr/bin && \
        ln -sf python3.8 python ;

CMD ["/bin/zsh"]
