FROM conda/miniconda3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get install -y -q wget unzip && \
    apt-get clean

RUN mkdir -p /workspace
WORKDIR /workspace

RUN conda install -c anaconda openjdk && \
    wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip && \
    unzip snpEff_latest_core.zip && \
    rm -f snpEff_latest_core.zip

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume