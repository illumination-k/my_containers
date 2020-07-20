FROM conda/miniconda3

RUN apt-get update --fix-missing && \
    apt-get clean

# v1.10 2020/3/4
RUN conda update -n base -c defaults conda && \
        conda install -c bioconda \
        rsem \
        star \
        samtools

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume
