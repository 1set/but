FROM 1set/butlite
LABEL maintainer="an9an63@gmail.com"

ARG ROOT_PATH=/root
ARG GO_PATH=/go

ENV GOPATH=${GO_PATH}
ENV GOBIN=${GO_PATH}/bin
ENV PATH=$PATH:$GOBIN

WORKDIR ${ROOT_PATH}

RUN set -eux; \
    apt-get update && apt-get install -y --no-install-recommends gpg-agent && curl -sL https://deb.nodesource.com/setup_12.x | bash - ; \
    add-apt-repository -y ppa:longsleep/golang-backports && add-apt-repository -y ppa:deadsnakes/ppa && apt-get update \
        && apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev gcc golang-go go-dep nodejs \
            python3.8-dev python3.8-distutils python3-pip python3-setuptools \
        && apt-get clean && rm -rf /var/lib/apt/lists/* ; \
    go get -u github.com/kardianos/govendor ; \
    python3.8 -m pip install -U pip setuptools wheel ; \
    cd /usr/bin && \
        ln -sf python3.8 python && \
        ln -sf pip3.8 pip;

CMD ["/bin/zsh"]
