FROM 1set/butlite:latest
LABEL maintainer="an9an63@gmail.com"

ARG ROOT_PATH=/root
ARG GO_PATH=/go

ENV GOPATH=${GO_PATH}
ENV GOBIN=${GO_PATH}/bin
ENV PATH=$PATH:$GOBIN:/usr/local/go/bin
ENV GO111MODULE=on

WORKDIR ${ROOT_PATH}

RUN set -eux; \
    apt-get update && apt-get install -y --no-install-recommends gpg-agent ; \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - ; \
    cd /tmp ; \
	curl -sL -o go.tgz "https://golang.org/dl/go1.15.5.linux-amd64.tar.gz" && \
		echo "9a58494e8da722c3aef248c9227b0e9c528c7318309827780f16220998180a0d *go.tgz" | sha256sum -c - ; \
		tar -C /usr/local -xzf go.tgz && rm -f go.tgz && go version && mkdir -p ${GO_PATH} ; \
    apt-get update && apt-get install -y --no-install-recommends \
        build-essential gcc g++ make figlet \
        nodejs \
        libssl-dev libffi-dev python3-dev python3-pip python3-setuptools \
        && apt-get clean && rm -rf /var/lib/apt/lists/* ; \
    python3.8 -m pip install -U pip setuptools ; \
    cd /usr/bin && \
        ln -sf python3.8 python ;

CMD ["/bin/zsh"]
