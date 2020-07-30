FROM conda/miniconda3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get clean

# v1.10 2020/3/4
RUN conda update -n base -c defaults conda && \
    conda install -c bioconda fastp

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume
