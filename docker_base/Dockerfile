FROM nvidia/cuda:11.4.2-cudnn8-devel-ubuntu20.04

ARG USER_NAME
ARG PASSWD
ARG UID

RUN groupadd -g $UID $USER_NAME
RUN useradd -rm -d /home/$USER_NAME -s /bin/bash -g $UID -G sudo -u $UID $USER_NAME


# This prevents installers from opening dialog boxes, be careful this setting is inherited!
ENV DEBIAN_FRONTEND noninteractive

#RUN apt-get update && apt-get -y install sudo wget


RUN  apt-key del 7fa2af80
#RUN apt-get install -y wget
#RUN wget https://developer.download.nvidia.com/compute/cuda/repos/$distro/$arch/cuda-keyring_1.0-1_all.deb
#RUN  dpkg -i cuda-keyring_1.0-1_all.deb

RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub

RUN apt-get update && apt-get -y install \
    sudo \
    openssh-server \
    build-essential \
    curl \
    git \
    libgl1-mesa-dev \
    libgl1-mesa-glx \
    libglew-dev \
    libosmesa6-dev \
    software-properties-common \
    net-tools \
    virtualenv \
    xpra \
    cmake \
    ffmpeg \
    net-tools \
    pkg-config \
    protobuf-compiler \
    python3.8 \
    python3-pip \
    tmux \
    wget \
    nano \
    git \
    unzip


RUN mkdir /var/run/sshd
RUN echo 'root:'$PASSWD | chpasswd
RUN echo $USER_NAME:$PASSWD | chpasswd
#RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

#COPY authorized_keys /root/.ssh/authorized_keys

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

WORKDIR /$USER_NAME/project/

RUN sudo chown -R $USER_NAME /home/$USER_NAME

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
