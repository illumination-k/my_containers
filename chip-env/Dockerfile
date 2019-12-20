FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda install \
    bedtools \
    bowtie2 \
    deeptools \
    -c bioconda -c conda-forge

WORKDIR /local_volume
