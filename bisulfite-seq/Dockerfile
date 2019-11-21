ARG BASE_CONTAINER=conda/miniconda3
FROM ${BASE_CONTAINER}

LABEL maintainer="illumination-k <illumination.k.27@gmail.com>"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8


# R pre-requisites
RUN apt-get update --fix-missing && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


RUN conda update -n base -c defaults conda&& \
    conda install \
        fastqc \
        fastp \
        bowtie2 \
        bismark \
        samtools \
        picard \
        multiqc \
        -c bioconda -c conda-forge

RUN mkdir -p /workspace && \
    mkdir -p /local_volume

WORKDIR /workspace
