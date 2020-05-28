FROM debian

LABEL maintainer="illumination-k <illumination.k.27@gmail.com>"

RUN apt-get update --fix-missing && \
    apt-get install -y git build-essential autoconf autogen make pkg-config gcc cmake gfortran zlib1g-dev \
        libgsl0-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log && \
    mkdir -p /workspace  

WORKDIR /workspace

RUN git clone https://github.com/MotomuMatsui/gs.git

WORKDIR /workspace/gs

RUN make

ENV PATH=/workspace/gs/MMseqs2/build/bin:$PATH
ENV PATH=/workspace/gs:$PATH

RUN useradd koke1000

USER koke1000
WORKDIR /home/koke1000