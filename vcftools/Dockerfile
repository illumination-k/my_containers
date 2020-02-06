FROM ubuntu:latest

LABEL maintainer="illumination-k <illumination.k.27@gmail.com>"

RUN apt-get update --fix-missing && \
    apt-get install -y git curl locales build-essential autoconf autogen make pkg-config\
        zlib1g-dev \
        libgsl0-dev \
        libbz2-dev \
        liblzma-dev \
        libcurl4-openssl-dev \
        libperl-dev && \
    apt-get -qq -y autoremove && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /var/log/dpkg.log 

#  言語設定
RUN echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen ja_JP.UTF-8

ENV LANG=ja_JP.UTF-8
ENV LC_CTYPE=ja_JP.UTF-8
ENV LANGUAGE=ja_JP.UTF-8
ENV LC_ALL=ja_JP.UTF-8

RUN mkdir -p /workspace/bin /local_volume
WORKDIR /workspace/bin/
RUN git clone https://github.com/vcftools/vcftools.git && \
    git clone https://github.com/samtools/htslib.git && \
    git clone https://github.com/samtools/bcftools.git

WORKDIR /workspace/bin/vcftools 
RUN ./autogen.sh && \
    ./configure make && \
    make install

WORKDIR /workspace/bin/htslib 
RUN autoheader && autoconf && ./configure --enable-libgsl --enable-perl-filters && make

WORKDIR /workspace/bin/bcftools 
RUN autoheader && autoconf && ./configure --enable-libgsl --enable-perl-filters && make

ENV PATH="${PATH}:/workspace/bin/bcftools"
ENV PATH="${PATH}:/workspace/bin/htslib"

WORKDIR /local_volume