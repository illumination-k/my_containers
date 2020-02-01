FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda install \
    bowtie2 \
    samtools \
    deeptools \
    -c bioconda -c conda-forge

ADD ./pipeline.sh /workspace
WORKDIR /local_volume
