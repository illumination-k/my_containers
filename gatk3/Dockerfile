FROM conda/miniconda3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update --fix-missing && \
    apt-get clean

RUN conda install -c bioconda gatk

RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT [ "gatk" ]
CMD [ "--version" ]