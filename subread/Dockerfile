FROM conda/miniconda3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get clean

#v1.0.1
RUN conda install -c bioconda -c conda-forge subread

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume
