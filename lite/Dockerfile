FROM ubuntu:18.04
LABEL maintainer="an9an63@gmail.com"

ARG ROOT_PATH=/root

WORKDIR ${ROOT_PATH}

RUN set -eux; \
    apt-get update \
        && apt-get install -y --no-install-recommends software-properties-common apt-transport-https ca-certificates \
            zsh time curl wget less openssh-client git tmux zip unzip p7zip-full vim htop iftop rsync lynx \
            iproute2 iputils-ping iputils-tracepath dnsutils net-tools ngrep netcat \
        && apt-get clean && rm -rf /var/lib/apt/lists/* ; \
    wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O /tmp/install-oh-my-zsh.sh \
        && zsh /tmp/install-oh-my-zsh.sh && rm -vf /tmp/install-oh-my-zsh.sh

COPY resource/.* ${ROOT_PATH}/

ENTRYPOINT zsh
