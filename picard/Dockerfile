FROM conda/miniconda3

RUN apt-get update --fix-missing && \
    apt-get install -y -q locales && \
    apt-get clean

RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# v2.22.0
RUN conda install -c bioconda picard

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir -p /local_volume
WORKDIR /local_volume

ENTRYPOINT [ "picard" ]
CMD [ "MarkDuplicates", "--version" ]