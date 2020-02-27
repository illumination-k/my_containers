FROM conda/miniconda3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get clean

RUN conda install -c bioconda samtools

RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "samtools" ]
CMD [ "--version" ]