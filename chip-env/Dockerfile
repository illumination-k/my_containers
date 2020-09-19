FROM illumination27/ngs-base:latest

RUN apt-get update --fix-missing && \
    apt-get install -y build-essential && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

RUN conda install \
    chromhmm \
    bowtie2 \
    macs2 \
    ucsc-bedgraphtobigwig \
    -c bioconda -c conda-forge

RUN pip install numpy scipy SICER2
WORKDIR /workspace

WORKDIR /local_volume
