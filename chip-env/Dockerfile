FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get install csh && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda install \
    bowtie \
    macs2 \
    ucsc-bedgraphtobigwig \
    chromhmm \
    -c bioconda -c conda-forge

WORKDIR /workspace

WORKDIR /local_volume
