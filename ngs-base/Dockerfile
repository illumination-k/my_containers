FROM conda/miniconda3

LABEL illumination-k <illumination.k.27@gmail.com>

RUN apt-get update --fix-missing && \
    apt-get install -y \ 
        less fish git curl wget \
        libxml2-dev libxslt1-dev build-essential \
        locales && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda update -n base conda && \
    conda install -c bioconda -c conda-forge \
        bedtools \
        deeptools \
        fastqc \
        fastp \
        homer \
        multiqc \
        samtools \
        picard && \
    conda clean --all --yes


RUN mkdir -p /workspace /local_volume 
WORKDIR /workspace

RUN curl -o setup.sh https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.10.0/setup-apt.sh && \
    sh setup.sh

#  言語設定
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

ENV PATH="${PATH}:/workspace/sratoolkit.2.10.0-ubuntu64/bin"

CMD ["fish"]