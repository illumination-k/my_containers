FROM python:3.8

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 libjson-maybexs-perl  libxml-libxml-perl && \
    mkdir -p /local_volume /workspace

WORKDIR /workspace

RUN pip install -U pip && \
    pip install biopython

RUN wget https://anaconda.org/bioconda/sra-tools/2.10.1/download/linux-64/sra-tools-2.10.1-pl526haddd2b5_0.tar.bz2 && \
    tar jxvf sra-tools-2.10.1-pl526haddd2b5_0.tar.bz2 && \
    rm -rf sra-tools-2.10.1-pl526haddd2b5_0.tar.bz2 && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove && apt-get clean

ENV PATH $PATH:/workspace/bin

WORKDIR /local_volume

