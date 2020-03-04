FROM conda/miniconda3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get clean

# v2.7.3a
RUN conda install -c bioconda star

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume

ENTRYPOINT [ "STAR" ]
CMD [ "--version" ]