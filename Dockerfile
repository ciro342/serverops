FROM jrei/systemd-ubuntu:latest

WORKDIR /app

RUN apt update && \
    apt install -y openssh-server && \
    mkdir -p /run/sshd

RUN useradd -m -s /bin/bash ciro && \
    echo "ciro:123" | chpasswd

RUN systemctl enable ssh

EXPOSE 22