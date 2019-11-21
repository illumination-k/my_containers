ARG BASE_CONTAINER=illumination27/ngs-base:latest
FROM ${BASE_CONTAINER}

LABEL maintainer="illumination-k <illumination.k.27@gmail.com>"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# R pre-requisites
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    gfortran \
    gcc && \
    apt-get autoremove && \
    apt-get autoclean

# bioconda packages
RUN conda update -n base -c defaults conda && \
    conda install \
    bioconductor-tximport \
    salmon \
    hisat2 \
    samtools \
    r-reader \
    r-jsonlite \
    -c bioconda -c conda-forge

ADD ./exec_files /workspace

WORKDIR /workspace

RUN conda clean --all --yes && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log
