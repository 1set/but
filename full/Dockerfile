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
    add-apt-repository ppa:longsleep/golang-backports && apt-get update \
        && apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev gcc golang-go go-dep nodejs python3-dev python3-pip python3-setuptools \
        && apt-get clean && rm -rf /var/lib/apt/lists/* ; \
    go get -u github.com/kardianos/govendor; \
    cd /usr/bin && \
        ln -sf python3 python && \
        ln -sf pip3 pip;

CMD ["/bin/zsh"]
